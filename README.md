# Dummy
Dummy is a Python program used to generate dummy data, this is primary created for another project I have in the works.

# Notes
As of right now, this program is single threaded, therefore, generating 10k rows can be quite tedious, and well, quite inefficient. However, multiprocessing is coming.

# Version
0.0.3

# The INI File
Currently it is hardcoded for sections, but the format needs to be like so:
~~~
[mysql]
host=hostname
port=0000
user=mysql_user
password=mysql_password
db=database_name
~~~
