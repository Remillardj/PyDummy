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

# Benchmarks
```
[root@server0001 PyDummy]# time ./main.py -c 10000 -t test --license-plate --phone-number --full-name --email --address --vehicle-model-year --vin-generator --text --text-length 10000

		____ ___  _ ____  _     _      _     ___  _   _____ _____ _      _____ ____  ____  _____  ____  ____
		/  __\  \///  _ \/ \ /\/ \__/|/ \__/|\  \//  /  __//  __// \  /|/  __//  __\/  _ \/__ __\/  _ \/  __		|  \/| \  / | | \|| | ||| |\/||| |\/|| \  /   | |  _|  \  | |\ |||  \  |  \/|| / \|  / \  | / \||  \/|
		|  __/ / /  | |_/|| \_/|| |  ||| |  || / /    | |_//|  /_ | | \|||  /_ |    /| |-||  | |  | \_/||    /
		\_/   /_/   \____/\____/\_/  \|\_/  \|/_/     \____\____\_/  \|\____\_/\_\_/ \|  \_/  \____/\_/\_


--- Starting PyDummy Data Generator! ---

real	10m34.615s
user	10m21.115s
sys	1m20.371s
```
10k rows for 10minutes. Still really slow.

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
