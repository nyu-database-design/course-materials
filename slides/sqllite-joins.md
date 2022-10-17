---
layout: presentation
title: SQLite Joins
permalink: /slides/sqlite-joins/
---

class: center, middle

# SQLite Joins
Database Design

---

# Agenda

1. [Overview](#overview)
1. [Example Data Set](#data-set)
1. [Primary Keys and Foreign Keys](#keys)
1. [Inner Joins](#inner-joins)
1. [Left Joins](#inner-joins)
1. [Conclusions](#conclusions)

---

name: overview

# Overview

---

name: data-set

# Data Set

---

template: data-set

## Raw data
Everyone's loves employment.  Government jobs are rumoured to be stable, non-demanding, and flush with benefits.

Let's take a look at [New York City job openings](https://data.cityofnewyork.us/City-Government/NYC-Jobs/kpav-sd4t).

- As part of the *open government movement*, New York City publishes data sets exportable in a variety of formats, including SQLite's favorite format - `CSV`.

- Export as CSV and save into a file named `NYC_Jobs.csv`.

---

template: data-set

## Data munging
We will explore job postings and salary ranges.  As usual, the data set needs a bit of munging before we can import it into a database and do our analysis.

- [Click to download](../files/sql_joins/munge.py) a Python script named `munge.py`.

- Place the Python file into the same directory as the `NYC_Jobs.csv` file.

- Run the Python script.  It will produce two new files: 

    -  `agencies_data.csv` - a list of agencies within NYC government

    - `jobs_data.csv` - information about each job opening in NYC government, including the agency to which it belongs

    - We will import each of these CSV files into its own *database table*

---

template: data-set

## Create tables
Start by setting up the two tables within SQLite to *match the fields in the CSVs*.  First for `jobs`:

```sqlite3
DROP TABLE IF EXISTS jobs;
CREATE TABLE jobs (
    id INTEGER PRIMARY KEY,
    job_id INTEGER NOT NULL,
    agency_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    salary_range_from INTEGER NOT NULL,
    salary_range_to INTEGER NOT NULL
);
```

... and then for `agencies`:

```sqlite3
DROP TABLE IF EXISTS agencies;
CREATE TABLE agencies (
	 id INTEGER PRIMARY KEY,
	 title TEXT NOT NULL
);
```

---

template: data-set

## Import data
Import the data from each CSV file into its corresponding table.

- First make sure SQLite is set to read CSVs with comma-separators:

    ```sqlite3
    .mode csv
    .separator ","
    ```

- import the jobs data into the `jobs` table:
```sqlite3
.import /Users/foobar/some_directory/jobs_data.csv jobs
```

- import the agencies data into the `agencies` table:
```sqlite3
.import /Users/foobar/some_directory/agencies_data.csv agencies
```

---

template: data-set

## Check the data
Before going any further, check that the data has imported successfully into SQLite.

Inspect the `jobs` tables:

```sqlite3
.headers on
select * from jobs;
```

--

The output should appear something like:

|id|job_id|agency_id|title|salary_range_from|salary_range_to|
|:----|:----|:----|:----|:----|:----|
|0|454437|0|Executive  Front Office Executive Operations Analyst|46856|62480|
|1|386903|1|Public Health Nurse, Bureau of School Health|40.79|40.79|
|2|424454|2|Desktop Support Technician|60550|69632|
|3|373602|3|HR PAYROLL ANALYST|75000|115000|
|...|...|...|...|...|...|

---

template: data-set

## Check the data (continued)
Inspect the `agencies` tables:

```sqlite3
select * from agencies;
```

--

The output should appear something like:

id|title
:---|:---
0|OFFICE OF MANAGEMENT & BUDGET
1|DEPT OF HEALTH/MENTAL HYGIENE
2|DEPARTMENT OF CORRECTION
3|FINANCIAL INFO SVCS AGENCY
4|TAXI & LIMOUSINE COMMISSION
5|LAW DEPARTMENT
...|...

---

name: keys

# Primary Keys and Foreign Keys

--

## Primary keys
Every table has a *primary key* - a field (or fields) whose values act as a unique identifier for all records.

- In the `jobs` table, the `id` field is always unique for every record and was designated as the primary key when the table was created.

- In the `agencies` table, the `id` field is always unique for every record and was designated as the primary key when the table was created.

- Thus, each table has a *primary key* field.

---

template: keys

## Relationships among multiple tables
In this example, as is often the case, we have multiple tables: `jobs` and `agencies`.  And there is a relationship between the them.

- Each job belongs to a particular agency.

- The `agency_id` field of each job indicates the agency to which each job belongs.

- It does so not by naming the agency, but by giving the unique `id` number of the relavant agency record.

- Thus, in order to see the full data about a job, we would have to pull the record from the `jobs` table as well as the relevant record from the `agencies` table.

- Such a query, merging data from two or more tables, is called a *join*.

---

template: keys

## Foreign keys
In order to perform a *join* to merge data from multiple tables, we must somehow inform the database *how to match a record from one table with the related record in the other table*.

- In our example, the `jobs` table contains the `agency_id` field, which holds the unique `id` of the related record in the `agencies` table.

- The `id` field of the `jobs` table is that table's *primary key*.

- The `id` field of the `agencies` table is that table's *primary key*.

- The `agency_id` field of the `jobs` table is called a *foreign key* - a reference to the primary key of a record in another table.

---

name: inner-joins

# Inner Joins

--

## Merging records from two tables
There are several ways to merge - or *join* - records from one table to related records from another table.  An *inner join* is the most common and perhaps simplest technique.

- Join all records in the `jobs` table to their related records in the `agencies` table:
```sqlite3
select jobs.title, agencies.title from jobs inner join agencies on jobs.agency_id=agencies.id;
```

- We have joined the tables by *foreign key* and *primary key*... a classic technique.

- Notice that both tables have their own `id` and `title` fields, and so we need to specifically prefix the field names with their table names, e.g. `jobs.title` and `agencies.title`.

---

template: inner-joins

## Results
The results of the inner join should look like a merged table including the fields we requested from both tables.

jobs.title|agencies.title
:----|:----
Executive  Front Office Executive Operations Analyst|OFFICE OF MANAGEMENT & BUDGET
Public Health Nurse, Bureau of School Health|DEPT OF HEALTH/MENTAL HYGIENE
Desktop Support Technician|DEPARTMENT OF CORRECTION
HR PAYROLL ANALYST|FINANCIAL INFO SVCS AGENCY
Administrative Assistant to the Assistant Commissioner of Safety & Emissions|TAXI & LIMOUSINE COMMISSION
...|...

---

template: inner-joins

## Referential integrity
An *inner join* maintains *referential integrity*.  In practical terms, this means that if a particular *job* record refers to an *agency* that does not exist in the `agencies` table, then that job will not be included in our merged results.

- Try for yourself... let's first look at the job #1 and its related agency.
```sqlite
select jobs.title, agencies.title from jobs inner join agencies on jobs.agency_id=agencies.id where jobs.id=1;
```

- Update this job record's *foreign key* to refer to a non-existant agency.
```sqlite
update jobs set agency_id=999 where id=1;
```

- See what happens when you *inner join* this job to its non-existent agency.
```sqlite
select jobs.title, agencies.title from jobs inner join agencies on jobs.agency_id=agencies.id where jobs.id=1;
```

---

name: left-joins

# Left Joins

--

## Concept
*Left joins* are similar to *inner joins* - they merge two related records from two different tables.  However, whereas *inner joins* maintain referential integrity and do not show records with invalid relationships, *left joins* have no such integrity.

- Try a left join that replicates what we did with an inner join earlier on:
```sqlite3
select jobs.id, jobs.title, agencies.title from jobs left join agencies on jobs.agency_id=agencies.id;
```

- You will see all the jobs listed, with their corresponding agencies, just like in an inner join.

- If you look at the job with the `id=1`, which we updated to refer to a non-existant agency, you will see it listed - this is different from an inner join. 
```sqlite3
select jobs.id, jobs.title, agencies.title from jobs left join agencies on jobs.agency_id=agencies.id where jobs.id=1;
```

- Thus *left joins* are not concerned with referential integrity.

- The table mentioned first in the query, `jobs` shows up on the *left*, with related records from the second table, `agencies`, attached to the right... thus the term, *left join*.


---

template: left-joins

## Checking for nothingness
This feature of *left joins* - that they do not maintain referential integrity - allows us to do something we cannot do with inner joins: we can check for non-existent relationships.

- For example, this query shows all jobs for which there is no matching agency:
```sqlite3
select jobs.id, jobs.title, agencies.title from jobs left join agencies on jobs.agency_id=agencies.id WHERE agencies.id IS NULL;
```

---

name: conclusions

# Conclusions

--

Thank you.  Bye.

