# SQLite Table Operations

## Create a table

### Commands

- `CREATE TABLE`

### Examples

The following query creates a table named `viking_metal_bands` in the current database, and specifies all of the table's fields, including which one is the primary key.

```sql
create table viking_metal_bands (
  id INTEGER PRIMARY KEY,
  band TEXT,
  formed INTEGER,
  origin TEXT,
  created DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### Primary keys

One field in every table must be the designated "primary key".

- The value in the primary key field for a given record is that record's unique identifier
- No two records can have the same value in the primary key field
- If a given data set does not have a good candidate for primary key (i.e. no field is guaranteed to have a unique value), you can have the database automatically create a unique integer for each row inserted into your table.
  - In the example command above, the `id` field is created as an automatically-incrementing integer, and is also set as the primary key. When a new row is inserted into this table, this field will automatically be assigned a unique integer value in that field.

```sql
  id INTEGER PRIMARY KEY,
```

### Timestamps

It is often very useful to keep a record of the date and time when any given record was inserted into the table.

- a field of the type DATETIME can have the current date and time automatically entered into it when a new row is inserted

```
  created DATETIME DEFAULT CURRENT_TIMESTAMP
```

## Read information about a table

### Commands

- `.tables` - lists all the tables in a given database
- `.schema` - outputs the properties of all of its fields in the given table

### Examples

The following query will output a list of all of the tables in the current database

```
.tables
```

The following will output all of the fields of the current database

```
.schema viking_metal_bands
```

## Update a table

### Commands

- `ALTER TABLE` - modifies a table

### Examples

The following query will add a new column to the table

```sql
ALTER TABLE viking_metal_bands ADD is_awesome BOOLEAN NOT NULL DEFAULT FALSE;
```

The following query will modify a column in the table

```sql
ALTER TABLE viking_metal_bands RENAME COLUMN band TO band_name;
```

Modify it back again!

```sql
ALTER TABLE viking_metal_bands RENAME COLUMN band_name TO band;
```

The following query will rename the table

```sql
ALTER TABLE viking_metal_bands RENAME TO favorite_viking_metal_bands;
```

In most other SQL-based databases, `ALTER TABLE` can be used to drop a field from a table. However, SQL does not support this - one must make an entirely new table without one of the fields, and then copy the data from the old table to the new one.

For example, to remove the `is_awesome` field.

```sql
CREATE TABLE temp_table AS SELECT id, band, formed, origin, created FROM favorite_viking_metal_bands;

DROP TABLE favorite_viking_metal_bands;

ALTER TABLE temp_table RENAME TO favorite_viking_metal_bands

```

## Delete a table

### Commands

- `DROP TABLE` - completely removes it from the database
- `DELETE FROM` - deletes the data stored in the table, but otherwise preserves the table structure

### Examples

The following query will completely remove the table from the database

```sql
DROP TABLE favorite_viking_metal_bands;
```

The following query will wipe out the data from the table, but keep the structure of the table

```sql
DELETE FROM favorite_viking_metal_bands;
```

## Save data to the table

Once a table is created, it is time to [create, read, update, and delete (CRUD) records in it](./sqlite-row-operations.md)!
