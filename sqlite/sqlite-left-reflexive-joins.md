# SQlite Left, Right, and Reflexive Joins

## Data set

The examples on this page refer to an available data set containing [prominent members of Genghis Khan's family](https://knowledge.kitchen/Genghis_Khan%27s_family_tree). This data set consists of:

- a table representing all notable Khans (the khans table)
- a table identifying which of those khans were Great Khans (the khagans table)

## Inner joins

As a reminder, [inner joins](./sqlite-inner-joins.md) enforce referential integrity by their nature. Executing an inner join query only returns results where there are matching rows in the two or more tables queried..

## Outer joins

Outer joins do not enforce referential integrity. An outer join query may return results where there are matching rows in one table, but not in the other related tables.

### Left Joins

- left joins allow the programmer to see all of the results in the source table ... even if there is no match in the related table. - a left join that brings up unmatched results does not necessarily signify problems with the data.

For example, some descendents of Genghis Khan were Khagans (Great Khans). But not all of his descendents were Khagans. Our data is split into two tables: one for information about the Khan family members, and one for information about the Khagans. A left join on the **khans** and **khagans** tables could show all Khans and their status as Khagans. Like an inner join, any Khan who was a Khagan will have all that data from two tables linked up and displayed. But unlike in an inner join, any Khan who was not a Khagan will also be displayed with NULL values in the related khagans table.

1.  inner join shows only those khans who were khagans
    ```sql
    SELECT * FROM khans INNER JOIN khagans ON khans.khan_id=khagans.khan_id;
    ```
1.  left join shows all khans including any related record of that khan as a khagan, if avaialble (or NULLs otherwise)
    ```sql
    SELECT * FROM khans LEFT JOIN khagans ON khans.khan_id=khagans.khan_id;
    ```
1.  left excluding join shows only those khans who do not have a related record as a khagan
    ```sql
    SELECT * FROM khans LEFT JOIN khagans ON khans.khan_id=khagans.khan_id WHERE khagans.khagan_id IS NULL;
    ```

### Right joins

- right joins (which are not supported by SQLite) will bring up records in the related table regardless of whether there is a match
- a right join that brings up unmatched results signifies a serious data problem with the data

Right joins are widely used when data tables that are part of a
relationship are imported into large systems in order to determine the
quantity and nature of problems. These problems are then addressed
either programmatically as we have done in class earlier by "scrubbing"
the data and then reimporting it into the database; or by writing SQL
queries (or scripts that hold the queries) to "scrub" the data when
possible.

For example, if we find a Khagan for whom there is no matching Khan,
then that is a serious lapse in our data integrity.

Right join shows all khagans and their record as khans, if available (or NULLs otherwise)

```sql
SELECT * FROM khans RIGHT JOIN khagans ON
khans.khan_id=khagans.khan_id;
```

Right excluding join shows all khagans who do not have a related record as a khan

```sql
SELECT * FROM khans RIGHT JOIN khagans ON
khans.khan_id=khagans.khan_id WHERE khans.khan_id IS NULL;
```

### Full outer joins

Full outer joins can be thought of the union of a left and a right join
on two tables:

- full outer joins bring up records in either table, regardless of whether there is a match in the other table
- in some relational database systems, there is a command to do a FULL OUTER JOIN. In MySQL, there is no such command, so a full outer join is only achieved by the union of a left and right join.
  - the left join should be inclusive to include all rows from the source table and any data related to them from the related table
  - the right join should be exclusive to include all rows from the related table that do not have matches in the source table

Merge an inclusive left join with an exclusive right join to get a full outer join.

```sql
(SELECT * FROM
khans LEFT JOIN khagans
ON khans.khan_id=khagans.khan_id)
UNION
(SELECT * FROM
khans RIGHT JOIN khagans
ON khans.khan_id=khagans.khan_id
WHERE khans.khan_id IS NULL)
```

**Note:** the `UNION` keyword is used to combine any two queries into one
result set, and is not specific to joins.

## Reflexive joins

There are situations in which one would want to build a join within the
same table. This can only work if there is one relationship. For
example:

- in a table of employees, one might notate who the manager is for each employee and the managers in turn eac have a manager of their own
- in a table of clients who might jointl own accounts, each spouse is spouse to the other person.
- in a table o Mongolian Khans, each Khan may have other Khans as parents.
- in a table o Mongolian Khans, each Khan may have Khan children with other Khans.

Be wary of reflexive joins, because you might in fact need a many-to-many relationship. In the examples above, this could potentially occur:

- an employee can have many managers over time or even report to different managers simultaneously for different projects.
- joint-ownership of an account can change over time.

For example, we can easily find how many children each Khan fathered, if any. Note the inner join on the same table, using aliases to make it easier to read:

```sql
SELECT parents.name AS daddy,
COUNT(children.name) AS num_kids
FROM khans AS parents INNER JOIN khans AS children
ON parents.khan_id = children.father_id
GROUP BY daddy;
```

Or better yet, show not only how many children they had, but what their
names were:

```sql
SELECT parents.name AS daddy,
GROUP_CONCAT(children.name) AS children**,
COUNT(children.name) AS num_kids
FROM khans AS parents INNER JOIN khans children
ON parents.khan_id = children.father_id
GROUP BY daddy;
```

Or perhaps, order Great Khans according to how many prominent children they had. This requires a reflexive join on the khans table mixed with a regular inner join on the khagans table:

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

## SQL joins cheat sheet

This cheat sheet is pulled from the [Code Project website's nice description of SQL joins](http://www.codeproject.com/Articles/33052/Visual-Representation-of-SQL-Joins).

![from [codeproject.com](http://codeproject.com)](./example_data/visual_representations_of_sql_joins.png)
