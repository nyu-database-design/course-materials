---
layout: presentation
title: SQLite Intro
permalink: /slides/sqlite-intro/
---

class: center, middle

# SQLite

Database Design

---

# Agenda

1. [Overview](#overview)
2. [Setup](#setup)
3. [CRUD](#crud)
4. [Import data](#import-data)
5. [Simple reads](#simple-reads)
6. [Functions](#functions)
7. [Grouping](#grouping)
8. [Combinations](#combinations)
9. [Conclusions](#conclusions)

---

name: overview

# Overview

--

## Features

A small, lightweight, portable _relational database_:

- zero configuration
- serverless
- simple file format
- cross-platform compatible
- manifest typing
- small footprint
- public domain source code
- industry-proven

---

name: setup

# Setup

--

## Installation

How to install and run SQLite:

- OS X comes with SQLite installed, although not necessarily the latest version.

- To install or upgrade, download the latest _Source code_ [here](https://sqlite.org/download.html) - pick the _"amalgamation" with "configure" script_. Unzip the file and follow the instructions in the file named `README.txt`.

---

template: setup
name: start

## Start

Run from the command shell.

Replace `database_name` with a database name of your choosing:

```bash
sqlite3 database_name.db
```

- If all goes swell, you are now in the SQLite command prompt.

- And if a database with this name didn't previously exist, it has now been created.

---

template: setup
name: quit

## Quit

To quit SQLite, use the `.quit` helper function:

```sqlite3
.quit
```

Now go and [re-start](#start) again!

---

name: crud

# CRUD

---

template: crud

## Overview

Data operations fall into one of four types:

- **C**reate - creating new data
- **R**ead - viewing existing data
- **U**pdate - updating existing data
- **D**elete - deleting existing data

These operations are affectionately known as data [CRUD](https://www.wordnik.com/words/crud).

---

template: crud

## Definition

"crud" definition from [wordnik.com](https://www.wordnik.com/words/crud):

> n. A coating or an incrustation of filth or refuse.
>
> n. Something loathsome, despicable, or worthless.

Welcome to the world of data!

---

template: crud

## Create (tables)

Before any data can be added to the database, a _table_ must be created using the `create table` command, including

- the name of the table

- a list of fields

- the data type assigned to each field, e.g. `INTEGER`, `REAL` (floating point), `NUMERIC`, `TEXT`, or `BLOB` (no data type assigned),

- an indication of which field is the _primary key_.

We will write these and other `CRUD` commands in the `SQL` language, which is common among relational databases.

---

template: crud

## Create (tables... continued)

An example of a table to hold student information:

```sqlite3
create table students (
  id INTEGER PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  email TEXT,
  city TEXT,
  state TEXT,
  country TEXT,
  created DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

- The `primary key` setting specifies which field holds the unique identifier of each row - in this case the `id` field.

- The current date and time will be automatically plugged into the `created` field with every new record.

---

template: crud

## Create rows manually

One can create new records in a table using the `insert` command

```sqlite3
insert into students (first_name, last_name, email, city, state, country) values ("Foo", "Barstein", "fb1258@nyu.edu", "Dallas", "Texas", "United States");
```

- Notice that the `id` value is not specified - it will be automatically supplied by the database if we don't specify.

- Notice also that the `created` value is not specified - it will be automatically supplied with the current date and time.

---

template: crud

## Create rows by importing a data file

One can import records from a file into a table. First set up the environment:

```sqlite3
.mode csv
.headers on
```

- SQLite natively imports _CSV_ files... just make sure to turn on `csv` mode first to avoid potential problems.

- the `.headers on` command tells SQLite to display the column headers once you read the data

- _JSON_ files are not natively supported and will have to be _transformed_ into a supported format prior to import.

- Download a [CSV file for this example](../files/sqlite/students.csv).

---

template: crud

## Create rows by importing a data file (continued)

Our `students` table has a `created` field that does not exist in the CSV data.
_SQLite will not import from a CSV file into a table whose fields do not exactly match the fields in the CSV data._

So let's import the CSV into a temporary table that matches the CSV exactly:

```sqlite3
create table temp_table (
  first_name TEXT,
  last_name TEXT,
  email TEXT,
  city TEXT,
  state TEXT,
  country TEXT
);
```

Then import the CSV into this `temp_table`, informing SQLite to `skip` the first row with headers in the file:

```sql
.import some_directory/students.csv temp_table --skip 1
```

---

template: crud

## Create rows by importing a data file (continued again)

Now, let's copy the data from `temp_table` into our permanent `students` table:

```sql
INSERT INTO students
(first_name, last_name, email, city, state, country)
SELECT * FROM temp_table;
```

The CSV data has now been copied, with the automatic addition of the `created` field in the `students` table.

Now we can drop the temporary table.

```sql
DROP TABLE temp_table;
```

---

template: crud

## Read

Read operations are performed with the `select` command

```sqlite3
select first_name from students where city="Grand Rapids";
```

- The command, `.mode csv` will make the output look like a CSV file. `.mode list` will return to the default. `.mode markdown` will make the output appear as a valid Markdown table.

- The command, `.separator ";"` will set the separator between fields to a semi-colon `;` - change it to whatever character you prefer.

- These two commands (`.mode` and `.separator`) can be useful for transforming the data into a format that is easily imported into another tools or programs.

---

template: crud

## Update

Update operations are performed with the `update` command

```sqlite3
update students set first_name="Baz" where id=15;
```

--

Updates to the overall schema of the table can be done with the `alter table` command

```sqlite3
alter table students add column photo blob;
```

---

template: crud

## Delete

Delete can be one of a few types:

- Delete a particular record using the `delete` command

```sqlite3
delete from students where first_name="Baz" and last_name="Trownson";
```

--

- Drop an entire table using the `drop table` command

```sqlite3
drop table students;
```

---

name: import-data

# Import data

---

template: import-data

## Find raw data

We will work with data on [school districts from the 2010 US census](https://www.census.gov/geographies/reference-files/time-series/geo/gazetteer-files.2010.html) This includes each district's...

- name
- state
- lowest grade taught
- highest grade taught
- population
- number of households
- land area
- water area
- geocoordinates (latitude & longitude)
- ... and a unique identifier for each row to serve as the _primary key_

We need a table in SQLite that will accommodate this.

--

- Note: 2010 was the last year that _population_ and _housing unit_ counts where included in these "Gazetteer" data sets.

---

template: import-data
name: create-table

## Create table

Create a table to accommodate the US Census school district data:

```sqlite3
CREATE TABLE sd (
  sd_state text,
  sd_geoid text PRIMARY KEY,
  sd_name text,
  sd_lowestGrade text,
  sd_highestGrade text,
  sd_pop_2010 integer,
  sd_hu_2010 integer,
  sd_aland real,
  sd_awater real,
  sd_aland_sqmi real,
  sd_awater_sqmi real,
  sd_intptlat real,
  sd_intptlong real
);
```

The _primary key_, the unique identifier of each record, is set to be the `sd_geoid` field, which represents unique locations in [the US Census' GEOID standard](https://www.census.gov/programs-surveys/geography/guidance/geo-identifiers.html), and is not to be confused with [the word geoid](https://en.wikipedia.org/wiki/Geoid).

---

template: import-data

## View list of tables

To view a list of any tables that exist in this database, use the `.tables` function.

```sqlite3
.tables
```

--

- Try it to make sure the table was created.

---

template: import-data

## View table schema

Viewing the `schema` of the `sd` table shows the command used to create it:

```sqlite3
.schema sd
```

--

- Try it to make sure the table was created _correctly_.

---

template: import-data
name: import-data-really

## Import data

Import from a [comma-separated values (CSV) file](../files/sqlite/school_districts.csv) of US census data on school districts into an SQLite table named `sd`... replace the path to the .csv file with one that works with your file system:

```sqlite3
.mode csv
.import /Users/foobar/some_directory/school_districts.csv sd
```

--

Note that SQL cannot import if the fields in the table do not exactly match the fields in the CSV data.

To import in such cases, we must do a workaround:

1. Create a temporary table whose fields exactly match those of the CSV.
1. Import from the CSV file into this temporary table.
1. Copy the data from the temporary table into the permanent table.
1. Drop the temporary table.

---

template: import-data

## Drop table

Delete the `sd` table:

```sqlite3
drop table sd
```

--

Now go [create it](#create-table) and [import data into it](#import-data) again!

---

template: import-data

## Use a script

Saving the commands to create and import data into [an SQL script](../files/sqlite/school_districts_setup.sql) can save time and effort - you can re-create and re-import data at any time by simply executing the script.

Change the file path to whatever path works on your system:

```sqlite3
.read /Users/foobar/some_directory/school_districts_setup.sql
```

--

- An SQL script is simply a file with a series of SQL commands that will run when read into the database.

---

template: import-data

## Share a database

If you want to copy a database or share it with someone (or yourself), simply pass around a copy of [the database file](../files/sqlite/sd.db) with the data in it.

And then [quit](#quit) and [re-start](#start) SQLite using that database file. No need to create tables from scratch or import anything.

Quit

```sqlite3
.quit
```

Restart

```bash
sqlite3 sd.db
```

Being a portable, small footprint, simple file format, cross-platform database system has its advantages.

---

template: import-data

## Dot functions

You have no-doubt noticed our use of some _dot functions_, such as:

- `.quit` - quit SQLite
- `.tables` - view a list of tables in the database
- `.schema [table name]` - show the schema of a table
- `.mode [mode]` - change the way data is formatted on screen, e.g `csv`, `list`, `markdown`, and more
- `.headers [on or off]` - whether to show the column headers above the data when displayed
- `.import [CSV filepath] [table name]` - import a data file into a table
- `.read [SQL script filepath]` - run an SQL script file

Replace the terms in square brackets with the real values (and delete the square brackets).

---

name: simple-reads

# Simple reads

---

template: simple-reads

## All school districts

Show all fields of all records.... there are a lot.

```sqlite3
select * from sd;
```

- The `*` here means _all fields_.

---

template: simple-reads

## School districts in New York State

The `where` clause filters results to only those within New York.... there are a lot.

```sqlite3
select * from sd where sd_state = "NY";
```

---

template: simple-reads

## Show only school district names

Each records contains many fields. Limit to just the _name_ of each school district, stored in a field named, `sd_name`:

```sqlite3
select sd_name from sd where sd_state = "NY";
```

Multiple fields can be selected by supplying a comma-separated list, such as `sd_name, sd_state`.

---

template: simple-reads

## Sort the results

Sort the records by school district name in reverse alphabetic order:

```sqlite3
select sd_name from sd where sd_state = "NY" order by sd_name desc;
```

- `asc` or `desc` can be used to indicate ascending or descending order.

---

template: simple-reads

## Limit the results

Show only the first 5 in the reverse-alphabetic list of New York school districts:

```sqlite3
select sd_name from sd where sd_state = "NY" order by sd_name desc limit 5;
```

- the `limit` clause controls the number of results that are displayed.

---

template: simple-reads

## Offset the results

Show the second _page_ of results...

```sqlite3
select sd_name from sd where sd_state = "NY" order by sd_name desc limit 5 offset 5;
```

... and the third _page_:

```sqlite3
select sd_name from sd where sd_state = "NY" order by sd_name desc limit 5 offset 10;
```

- the `limit` clause controls how many results are displayed

- the `offset` clause indicates which row in the results to start from

---

template: simple-reads

## Smallest school districts

The 10 smallest school districts in the country:

```sqlite3
select sd_name, sd_state, sd_pop_2010 from sd order by sd_pop_2010 asc limit 10;
```

- the `order` clause indicates by which field to order results

- the `asc` option indicates to order in ascending order

- the `limit` clause controls the number of results displayed

---

name: functions

# Functions

---

template: functions

## Concept

There are a variety of [built-in aggregate functions](https://sqlite.org/lang_aggfunc.html) available to be used in queries. These are used to calculate aggregate statistics from the records returned by any query.

- These are similar to the statistical functions built into spreadsheet software:, `SUM()`, `AVERAGE()`, `MIN()`, `MAX()`, `COUNT()`, etc.

---

template: functions

## Counting records

Calculate how many school districts exist in the US and Puerto Rico using the `count()` function.

```sqlite3
select count(sd_geoid) from sd;
```

- The `COUNT()` function returns the number of values in the _field_ indicated as an argument.

- The primary key field, `sd_geoid`, is guaranteed to be a unique for each record, while other fields may not be.

---

template: functions

## Counting records in a filtered result set

Count the number of school districts in New York State by filtering results with a `where` clause.

```sqlite3
select count(sd_geoid) from sd where sd_state = "NY";
```

- We have thus applied a filter - the `COUNT()` function will only count those rows that match the criteria indicated in the `WHERE` clause.

---

template: functions

## Calculating average

Calculate the average population of school districts across the US, using the `avg()` function.

```sqlite3
select avg(sd_pop_2010) from sd;
```

- The `AVG()` function will return a floating point number.

- In actuality, there are no half people or 1/4 people. So we could round the result using the `round()` function, as in `round( avg(sd_pop_2010) )`.

---

template: functions

## Calculating sum

Calculate the total population in the country, using the `sum()` function.

```sqlite3
select sum(sd_pop_2010) from sd;
```

And, of course, we could calculate the total population of just Minnesota by filtering this query with a `WHERE` clause:

```sqlite3
select sum(sd_pop_2010) from sd where sd_state = "MN";
```

---

name: grouping

# Grouping

---

template: grouping

## Concept

Grouping records together by some attributes they share in common allows us to calculate aggregate statistics.

---

template: grouping

## Counting school districts per state

Counting the number of school districts per state requires us to group together all school districts in each state:

```sqlite3
select count(sd_geoid) from sd group by sd_state;
```

- Thus we don't count the number of unique geoids in the entire table. This performs a separate count for each group.

---

template: grouping

## Counting school districts per state... better

The previous query showed us the numbers, but not which state they represented.

View the state name _and_ the number of school districts in each state:

```sqlite3
select sd_state, count(sd_geoid) from sd group by sd_state;
```

---

template: grouping

## Counting school districts per state in descending order

The state name and the number of school districts in each state, in descending order:

```sqlite3
select sd_state, count(sd_geoid) from sd group by sd_state order by count(sd_geoid) desc;
```

Note that the clause, `order by count(sd_geoid)` treats the count as if it were like any other field to sort by. We can make this less redundant to write by using an _alias_ for the result of the count:

```sqlite3
select sd_state, count(sd_geoid) as num_districts from sd group by sd_state order by num_districts desc;
```

---

template: grouping

## Calculating the 3 most populous states

Sort states by aggregate population in descending order, then limit to the first 3 records.

```sqlite3
select sd_state, sum(sd_pop_2010) as pop from sd group by sd_state order by pop desc limit 3;
```

---

template: grouping

## Calculating the 3 least populous states

Sort states by aggregate population in ascending order, then limit to the first 3 records.

```sqlite3
select sd_state, sum(sd_pop_2010) as pop from sd group by sd_state order by pop asc limit 3;
```

---

name: combinations

# Combinations

---

template: combinations

## Concept

Let's take what we've learned a step further.

---

template: combinations

## All of New England

New England is made of several states. Let's find the top ten largest school districts in this combined region using an `in` operator:

```sqlite3
select sd_name, sd_state, sd_pop_2010 from sd where sd_state in ("ME", "VT", "NH", "MA", "RI") ORDER BY sd_pop_2010 desc limit 10;
```

---

template: combinations

## Highest population density school districts

Which school districts have the highest population density?

```sqlite3
select sd_name, sd_state, round(sd_pop_2010 / sd_aland_sqmi) as density from sd order by density desc limit 10;
```

---

template: combinations

## Lowest population density school districts

Which school districts have the lowest population density?

```sqlite3
select sd_name, sd_state, round(sd_pop_2010 / sd_aland_sqmi) as density from sd order by density asc limit 10;
```

This query will return a bunch of school districts with the name including the text, "School District Not Defined"... let's exclude these:

```sqlite3
select sd_name, sd_state, round(sd_pop_2010 / sd_aland_sqmi) as density from sd where sd_name not like "%not defined%" order by density asc limit 10;
```

---

template: combinations

## Highest population density states

Which states have the highest population density?

```sqlite3
select sd_state, round( sum(sd_pop_2010) / sum(sd_aland_sqmi) ) as density from sd group by sd_state order by density desc limit 10;
```

---

template: combinations

## Lowest population density states

Which states have the lowest population density?

```sqlite3
select sd_state, round( sum(sd_pop_2010) / sum(sd_aland_sqmi) ) as density from sd group by sd_state order by density asc limit 10;
```

---

# Conclusions

--

Thank you. Bye.
