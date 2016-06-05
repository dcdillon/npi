# npi

#### db.sql
This file contains MySQL commands for creating the database and table to contain the data.

#### insert_npi_data.py
This is a python script that can be called as follows:

```
python insert_npi_data.py --host=someserver --user=someuser --password=somepassword somenpifile.csv
```

It will load the data from the given file into the NPIData table on the given server (with the given user credentials).  This can be run on either the big NPI file (initial run) or on any of the incremental update files (to bring the database up to date).

#### query_npi_data.py
This is a python script that can be called as follows:

```
python query_npi_data.py --host=someserver --user=someuser --password=somepassword 123456789
```

It will query the `NPIData` table and print out the record data in a reasonable format.
