# Dummy
Dummy is a Python program used to generate dummy data, this is primary created for another project I have in the works.

# Notes
Program uses multithreading, so it is slow to start but does speed up. Working on getting some benchmarks soon.

# Version
0.1.0 Release

# Usage
`pip install -r requirements.txt`
`mysql -e "create database VehicleModelYear"`
`mysql -D VehicleModelYear < db/schema.sql`
`mysql -D VehicleModelYear < db/data.sql`
Start generating:
`./main -h`

# The INI File for VehicleModelYear module, insert the data from the db/ folder into a local MySQL server
Currently it is hardcoded for sections, but the format needs to be like so:
~~~
[mysql]
host=hostname
port=0000
user=mysql_user
password=mysql_password
db=database_name
~~~
