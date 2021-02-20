# SQLite Row Operations

This document outlines the classic Create, Read, Update, and Delete (CRUD) methods available in the SQL language for manipulating records in a relational database.

## Create a new row in a table

### Commands

- `INSERT`

### Examples

The following query creates a new row in the table

```sql
INSERT INTO favorite_viking_metal_bands (
    band,
    formed,
    origin
)
VALUES (
    'Amon Amarth',
    1992,
    'Sweden'
);
```

The following query uses the `LOWER()` function to convert the strings to lowercase before saving in the table.

- Such string processing can be useful to make sure all data is stored in a standardized format.

```sql
INSERT INTO favorite_viking_metal_bands (
    band,
    formed,
    origin
)
VALUES (
    LOWER('Ancient Rites'),
    '1998',
    LOWER('Belgium')
);
```

## Importing data from a file into rows

### Notes

The following examples assume you have a CSV-formatted text file named `viking_metal_bands.csv` in your current working directory. Download the [sample CSV text file used in these examples](./example_data/viking_metal_bands.csv)

### Commands

- `.import`

### Examples

The following query, will import the data from a standard CSV file, ignoring the first line in the file

- It is important to first change the mode to `csv` before importing a CSV file.
- Also note that in SQLite **it is not possible to import data directly to a table with an auto-incrementing primary key**. So we first import into a temporary table with only those fields that match the data in the CSV, copy the data into the table with the primary key, and then drop the temporary table.

```sql
# switch to CSV mode
.mode csv

# create a temporary table with fields that exactly match the CSV
CREATE TABLE temp_table (
    band TEXT,
    formed INTEGER,
    origin TEXT
);

# import the CSV file into the temporary table
.import ./viking_metal_bands.csv temp_table

# copy the data into the permanent table
INSERT INTO favorite_viking_metal_bands (band, formed, origin) SELECT * FROM temp_table;

# drop the temporary table
DROP TABLE temp_table;
```

## Read rows from a table

### Commands

- `SELECT`

### Examples

The following query retrieves all rows of data from the table

```sql
SELECT * FROM favorite_viking_metal_bands WHERE 1;
```

The following query retrieves only a single field from all rows of data from the table

```sql
SELECT band FROM favorite_viking_metal_bands WHERE 1;
```

The following query retrieves only those rows of data from the table where the 'formed' field has a value greater than 1990:

```sql
SELECT * FROM favorite_viking_metal_bands WHERE formed>1990;
```

The following query retrieves only a single field from those rows of data from the table where the 'formed' field has a value greater than 1990:

```sql
SELECT band FROM favorite_viking_metal_bands WHERE formed>1990;
```

The following query retrieves three fields from those rows of data in the table where the 'origin' is either 'Norway' or 'Finland'

```sql
SELECT band, origin, formed FROM favorite_viking_metal_bands WHERE origin='Norway' OR origin='Finland';
```

The following query retrieves three fields from those rows of data in the table where the origin is neither 'Norway' nor 'Finland'

```sql
SELECT band, origin, formed from favorite_viking_metal_bands WHERE origin!='Norway' AND origin!='Finland';
```

The following query retrieves all rows of data from the table, and orders them alphabetically by the band field

```sql
SELECT * FROM favorite_viking_metal_bands WHERE 1 ORDER BY band ASC;
```

The following query will order all rows alphabetically, and then return only the first 10

```sql
SELECT band FROM favorite_viking_metal_bands WHERE 1 ORDER BY band ASC LIMIT 10;
```

The following query will order all rows alphabetically, and then return only the first 10... note the minor change in syntax from the previous example

```sql
SELECT band FROM favorite_viking_metal_bands WHERE 1 ORDER BY band ASC LIMIT 0,10;
```

The following query will order all rows alphabetically, and then return only the second 10 results

```sql
SELECT band from favorite_viking_metal_bands WHERE 1 ORDER BY band ASC LIMIT 10,10;
```

The following query will order all rows alphabetically, and then return only the third 10 results

```sql
SELECT band from favorite_viking_metal_bands WHERE 1 ORDER BY band ASC LIMIT 20,10;
```

The following query retrieves those rows of data from the table where the origin has the value "Netherlands", and orders them by the formed field in reverse numeric order

```sql
SELECT * FROM favorite_viking_metal_bands WHERE origin="Netherlands" ORDER BY formed DESC;
```

The following will read all the bands with names including the word "Thor"

```sql
SELECT * FROM favorite_viking_metal_bands WHERE band LIKE "%Thor%";
```

## Read aggregate data from a table

Aggregate functions allow you to generate insights into sets of rows.
They are used in tandem with the GROUP BY clause.

### Aggregate functions

- `MIN()`
- `MAX()`
- `AVG()`
- `SUM()`
- `COUNT()`

### Examples

The following query retrieves the earliest year a viking metal band was formed, broken down by country of origin

```sql
SELECT origin, MIN(formed) FROM favorite_viking_metal_bands GROUP BY origin;
```

The following query retrieves the latest year a viking metal band was formed, broken down by country of origin

```sql
SELECT origin, MAX(formed) FROM favorite_viking_metal_bands GROUP BY origin;
```

The following query retrieves the average year a viking metal band was formed, broken down by country of origin

```sql
SELECT origin, AVG(formed) FROM favorite_viking_metal_bands GROUP BY origin;
```

The following query retrieves the sum of all years that viking metal band were formed, broken down by country of origin

```sql
SELECT origin, SUM(formed) FROM favorite_viking_metal_bands GROUP BY origin;
```

The following query retrieves the number of bands formed, broken down by country of origin

```sql
SELECT origin, COUNT(formed) FROM favorite_viking_metal_bands GROUP BY origin;
```

## Update a row in a table

### Commands

- `UPDATE`

### Examples

The following example updates the row with the id value of 9, and changes the origin field to be "sweden"

```sql
UPDATE favorite_viking_metal_bands SET origin='sweden' WHERE id=9;
```

The following example updates any rows with the band field, "Amon Amarth", and the formed field greater than 1998

```sql
UPDATE favorite_viking_metal_bands SET origin='sweden' WHERE band="Amon Amarth" AND formed>1998;
```

## Delete a row in a table

### Commands

- `DELETE`

### Examples

The following query deletes all rows from a table

```sql
DELETE FROM favorite_viking_metal_bands WHERE 1;
```

The following query deletes only that row with id 9

```sql
DELETE FROM favorite_viking_metal_bands WHERE id=9;
```

The following query deletes any rows with band name "Ancient Rites" and origin, "belgium"

```sql
DELETE FROM favorite_viking_metal_bands WHERE band="Ancient Rites" AND origin="Belgium";
```

The following query deletes any rows where the formed field is greater than 1998

```sql
DELETE FROM favorite_viking_metal_bands WHERE formed>1998;
```
