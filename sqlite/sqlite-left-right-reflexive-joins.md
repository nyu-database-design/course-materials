# SQlite Outer Joins and Reflexive Joins

## Types of joins

### Inner joins

As a reminder, [inner joins](./sqlite-inner-joins.md) enforce referential integrity by their nature. Executing an inner join query only returns results where there are matching rows in the two or more tables queried.

### Outer joins

Outer joins do not enforce referential integrity. An outer join query may return results with records from one table that have no related records in the other tables.

There are two types of outer join:

- left joins
- right joins

The difference is in which table is considered the **source table** (also known as the **driving table**) for the joins. The source table is that table for which records will be included in the query results no matter whether a match in the other table is found.

- In left joins, the table mentioned first in the query (on the left) is the source table.
- In right joins (which are not supported by SQLite), the table mentioned second in the query (on the right) is the source table.

### Left joins

Left joins allow the programmer to see all of the results in the source table ... even if there is no match in the other related table.

- a left join that brings up unmatched results does not necessarily signify problems with the data.

### Right joins

Right joins do not exist in SQLite, but are supported by most other SQL-based relational database systems. In SQLite, we can simply use a left join with the table names in reverse order. So what was the left table becomes the right, and vice-versa... this will become more clear in the example queries below.

## Example data

The examples on this page refer to an available data set containing prominent members of [Genghis Khan's family](https://en.wikipedia.org/wiki/Family_tree_of_Genghis_Khan).

Genghis Khan and some of his descendents were Khagans (Great Khans). But not all of his descendents were Khagans.

Our data is split into two tables:

1. the `khans` table for information about the Khan family members.
1. the `khagans` table for information about those Khans who were Khagans and any special name they used for themselves while they were Khagans.

Thus, to get a full picture of which Khans were Khagans, we would have to merge the data from the two tables.

### khans table

A few lines from the `khans` data:
| khan_id | name | born | died | father_id | mother_id |
| ------- | ------- | ---- | ---- | --------- | --------- |
| 1 | Yesugei | | 1171 | | |
| 2 | Hoelun | | | | |
| 3 | Temüjin | 1162 | 1227 | 1 | 2 |
| 4 | Börte | 1161 | 1230 | | |
| 5 | Jochi | 1181 | 1227 | 3 | 4 |
...

See the [CSV file, khans.csv](./example_data/khans.csv), for the full data.

Create the table:

```sql
CREATE TABLE khans (khan_id INTEGER PRIMARY KEY, name TEXT, born INTEGER, died INTEGER, father_id INTEGER, mother_id INTEGER);
```

Import the data from the CSV file into the table:

```sql
.mode csv
.headers on
.import ./khans.csv khans
```

### khagans table

A few lines from the `khagans` table:

| khagan_id | khan_id | name         |
| --------- | ------- | ------------ |
| 1         | 3       | Genghis Khan |
| 2         | 11      |              |
| 3         | 13      |              |
| 4         | 18      |              |
| 5         | 19      |              |

...

See the [CSV file, khagans.csv](./example_data/khagans.csv), for the full data.

Create the table:

```sql
CREATE TABLE khagans (khagan_id INTEGER PRIMARY KEY, khan_id INTEGER, name TEXT);
```

Import the data from the CSV file into the table:

```sql
.mode csv
.headers on
.import ./khagans.csv khagans
```

## Example queries

### Inner join - all Khans who were Khagans

An inner join on the `khans` and `khagans` tables could show only those Khans who were also Khagans - referential integrity would be enforced. In other words, an inner join would show only those rows from the two tables where a relationship exists in the data.

The following query...

```sql
SELECT * FROM
khans INNER JOIN khagans
ON khans.khan_id=khagans.khan_id;
```

Results in the following data:
| khan_id | name | born | died | father_id | mother_id | khagan_id | khan_id | name |
|---------|---------|------|------|-----------|-----------|-----------|---------|--------------|
| 3 | Temüjin | 1162 | 1227 | 1 | 2 | 1 | 3 | Genghis Khan |
| 11 | Ögedei | 1186 | 1241 | 3 | 4 | 2 | 11 | |
| 13 | Güyük | 1206 | 1248 | 11 | 12 | 3 | 13 | |
| 18 | Möngke | 1209 | 1259 | 16 | 17 | 4 | 18 | |
| 19 | Kublai | 1215 | 1294 | 16 | 17 | 5 | 19 | |
| 21 | Temür | 1265 | 1307 | 20 | | 6 | 21 | |
...

Since inner joins are the most commonly used joins, the query above could also be written in a more shorthand form, where the inner join is implicit, but not mentioned:

```sql
SELECT * FROM
khans, khagans
WHERE khans.khan_id=khagans.khan_id;
```

### Left join - all Khans, including those who were Khagans

A left join on the `khans` and `khagans` tables could show all Khans and their status as Khagans.

Like an inner join, any Khan who was a Khagan will have that data from two tables linked up and displayed. But unlike an inner join, any Khan who was not a Khagan will also be displayed with NULL values in the related `khagans` table.

The following query...

```sql
SELECT * FROM
khans LEFT JOIN khagans
ON khans.khan_id=khagans.khan_id;
```

Results in the following data:
| khan_id | name | born | died | father_id | mother_id | khagan_id | khan_id | name |
|---------|-------------------|------|------|-----------|-----------|-----------|---------|--------------|
| 1 | Yesugei | | 1171 | | | | | |
| 2 | Hoelun | | | | | | | |
| 3 | Temüjin | 1162 | 1227 | 1 | 2 | 1 | 3 | Genghis Khan |
| 4 | Börte | 1161 | 1230 | | | | | |
| 5 | Jochi | 1181 | 1227 | 3 | 4 | | | |
...

Notice that all the records from the `khans` table are present. Some of those `khans` records are linked up with matching rows from the `khagans` table, but some are not. The `khans` table is the **source table**.

### Left join - all Khans who were not Khagans

We can use a left join to check for non-existent relationships, such as those Khans who were not Khagans. This is performed by a query that joins the two tables and requests only those records where the related `khans` table data is not present.

```sql
SELECT * FROM
khans LEFT JOIN khagans
ON khans.khan_id=khagans.khan_id
WHERE khagans.khagan_id IS NULL;
```

Results in the following data:
| khan_id | name | born | died | father_id | mother_id | khagan_id | khan_id | name |
|---------|-------------------|------|------|-----------|-----------|-----------|---------|------|
| 1 | Yesugei | | 1171 | | | | | |
| 2 | Hoelun | | | | | | | |
| 4 | Börte | 1161 | 1230 | | | | | |
| 5 | Jochi | 1181 | 1227 | 3 | 4 | | | |
...

### Left join - all Khagans, including any matching Khans

In the following query, notice how we use `khagans` as the source table - we want to see all `khagans` records, regardless of whether there are any related `khans` records. This left join can show us all Khagans and their related record as Khans, if available (or NULLs otherwise).

Reversing the order of the table names in the left join query in this way allows us to get around the fact that SQLite does not support right joins. A right join would treat the `khagans` table as the source table, which is exactly the same as what we are doing here.

```sql
SELECT * FROM
khagans LEFT JOIN khans
ON khans.khan_id=khagans.khan_id;
```

This results in the following data:
| khagan_id | khan_id | name | khan_id | name | born | died | father_id | mother_id |
|-----------|---------|--------------|---------|---------|------|------|-----------|-----------|
| 1 | 3 | Genghis Khan | 3 | Temüjin | 1162 | 1227 | 1 | 2 |
| 2 | 11 | | 11 | Ögedei | 1186 | 1241 | 3 | 4 |
| 3 | 13 | | 13 | Güyük | 1206 | 1248 | 11 | 12 |
| 4 | 18 | | 18 | Möngke | 1209 | 1259 | 16 | 17 |
| 5 | 19 | | 19 | Kublai | 1215 | 1294 | 16 | 17 |
...

### Left join - all Khagans with no matching Khan

It is often important for data integrity to identify and fix **orphaned data** - records that should have relationships to other records, but do not.

For example, in Genghis' Khan's lineage, all Khagans (Great Leaders) were also Khans. But not all Khans were Khagans. If we find a Khagan for whom there is no matching Khan record, then that is a serious lapse in our data integrity.

The following **excluding** left join query will show us Khagans who do not have a related record as a Khan. This is another case where we use a left join with table names in reverse order to perform a task that a right join could perform in a different database system that supported them.

```sql
SELECT * FROM
khagans LEFT JOIN khans
ON khans.khan_id=khagans.khan_id
WHERE khans.khan_id IS NULL;
```

At the moment, our data integrity is good, so there are no results. But if there were any `khagans` records that referenced a `khans` record that didn't exist, this query would have shown us those results.

Try it yourself by deleting one of the `khans` records that is referred to by one of the `khagans` records.

## Full outer joins

Full outer joins retrieve the full set of records from two tables, including any relationships between them. Conceptually, this would be a standard left join merged with the results of an excluding right join.

In other words, a full outer join is the union of two queries on two tables, let's call them table `a` and table `b`:

- a query to retrieve all the records from table `a`, including any matching data from table `b`.
- a query to retrieve all the records from table `b` that have no matching data in table `a`.

For example:

```sql
SELECT * FROM
khans LEFT JOIN khagans
ON khans.khan_id=khagans.khan_id
UNION ALL
SELECT * FROM
khagans LEFT JOIN khans
ON khans.khan_id=khagans.khan_id
WHERE khans.khan_id IS NULL;
```

This results in the following data:

| khan_id | name    | born | died | father_id | mother_id | khagan_id | khan_id | name         |
| ------- | ------- | ---- | ---- | --------- | --------- | --------- | ------- | ------------ |
| 1       | Yesugei |      | 1171 |           |           |           |         |              |
| 2       | Hoelun  |      |      |           |           |           |         |              |
| 3       | Temüjin | 1162 | 1227 | 1         | 2         | 1         | 3       | Genghis Khan |
| 4       | Börte   | 1161 | 1230 |           |           |           |         |              |
| 5       | Jochi   | 1181 | 1227 | 3         | 4         |           |         |              |

...

## Reflexive joins

There are situations in which one would want to build a join within the same table. This can only work if there is one relationship. For example:

- in a table of employees, one might notate who the manager is for each employee and the managers in turn each have a manager of their own
- in a table of clients who might jointly own accounts, each spouse is spouse to the other person.
- in a table of Mongolian Khans, each Khan may have other Khans as parents.
- in a table o Mongolian Khans, each Khan may have Khan children with other Khans.

Be wary of reflexive joins, because you might in fact need a many-to-many relationship. In the examples above, this could potentially occur:

- an employee can have many managers over time or even report to different managers simultaneously for different projects.
- joint-ownership of an account can change over time.

### Reflexive join - number of children fathered by each male Khan

For example, we can easily find how many children each Khan fathered, if any. Note the inner join on the same table, using aliases to make it easier to read:

```sql
SELECT parents.name AS daddy,
COUNT(children.name) AS num_kids
FROM khans AS parents INNER JOIN khans AS children
ON parents.khan_id = children.father_id
GROUP BY daddy
ORDER BY num_kids DESC;
```

The results are:
| daddy | num_kids |
|------------|----------|
| Yesugei | 6 |
| Tolui | 4 |
| Temüjin | 4 |
| Ögedei | 2 |
| Jochi | 2 |

### Reflexive join - names of children fathered by each female Khan

Or better yet, show not only how many children each woman had, but what their names were:

```sql
SELECT parents.name AS mommy,
GROUP_CONCAT(children.name) AS children,
COUNT(children.name) AS num_kids
FROM khans AS parents INNER JOIN khans children
ON parents.khan_id = children.mother_id
GROUP BY mommy
ORDER BY num_kids DESC;
```

Note the use of the `GROUP_CONCAT` function to concatenate the childrens' names together into a comma-separated list.

This results in the following data:
| mommy | children | num_kids |
|-------------------|--------------------------------|----------|
| Sorghaghtani Beki | Möngke,Kublai,Hulagu,Ariq Böke | 4 |
| Hoelun | Temüjin,Hasar,Hachiun,Temüge | 4 |
| Börte | Jochi,Chagatai,Ögedei,Tolui | 4 |
| Töregene Khatun | Güyük,Kashin | 2 |

...

### Reflexive join - counting prominent children of each male Khan

Or perhaps, order Great Khans according to how many prominent children they had. This requires a reflexive join on the `khans` table mixed with a regular inner join on the `khagans` table:

```sql
SELECT parents.name AS daddy,
GROUP_CONCAT(children.name) AS children,
COUNT(children.name) AS num_kids
FROM khans parents, khans children, khagans
WHERE parents.khan_id = children.father_id
AND parents.khan_id=khagans.khan_id
GROUP BY daddy
ORDER BY num_kids DESC;
```

The results of greatness:
| daddy | children | num_kids |
|---------|-----------------------------|----------|
| Temüjin | Jochi,Chagatai,Ögedei,Tolui | 4 |
| Ögedei | Güyük,Kashin | 2 |
| Kublai | Zhenjin | 1 |

## SQL joins cheat sheet

This cheat sheet is pulled from the [Code Project website's nice description of SQL joins](http://www.codeproject.com/Articles/33052/Visual-Representation-of-SQL-Joins).

Remember that a right join is the same as a left join with the table names in reverse order.

![from [codeproject.com](http://codeproject.com)](./example_data/visual_representations_of_sql_joins.png)
