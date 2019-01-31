#!/usr/local/bin/python3

import string
import random
import names
import sqlite3
import pymysql
import configparser

from dummy.VinGenerator import vin

# Fake license plate  generator
def license_plates(size=6, chars=string.ascii_uppercase + string.digits):
	return (''.join(random.choice(chars) for _ in range(size)))

# random phone generator
def phone_number(size=10):
	phoneList = random.sample(range(0,10), size)
	phoneList.insert(0, "(")
	phoneList.insert(4, ")")
	phoneList.insert(5, "-")
	phoneList.insert(9, "-")
	return (''.join(map(str, phoneList)))

# Name generator
def full_name(mf):
	return names.get_full_name(gender=mf)

def first_name(mf):
	return names.get_first_name(gender=mf)

def last_name():
	return names.get_last_name()

def generate_email(userRand=False, chars=string.ascii_lowercase + string.digits):
	extensions = ['com','net','org','gov']
	domains = ['gmail','yahoo','comcast','verizon','charter','hotmail','outlook','frontier','protonmail']
	randExt = extensions[random.randint(0,len(extensions)-1)]
	randDom = domains[random.randint(0,len(domains)-1)]
	if (userRand == False):
		userLength = random.randint(1,40)
		user = ''.join(random.choice(chars) for _ in range(userLength))
	else:
		mf = ['male', 'female']
		pickGender = random.randint(0, 2)
		user = names.get_first_name(gender=mf[pickGender]) + "." + names.get_last_name()
	return (user + "@" + randDom + "." + randExt)


# A little deprecated with vehicle_model_year() function
def get_manufactorers(fileName="manufactorers.txt"):
	brands = []
	try:
		fileHandle = open(fileName, "r")
		for manufactorer in fileHandle:
			brands.append(manufactorer)
	except Exception as e:
		print("Error!", e)
		return False
	brandsLen = len(brands)
	if (brandsLen != 0):
		randIndex = random.randint(0, brandsLen)
		return brands[randIndex].rstrip("\n")
	else:
		return False

# Use a configuration file to retrieve vehicle model years randomly
# Yes I know it's not actually an API, but I plan to eventually implement one for the MySQL database
def vehicle_model_year_api(iniFile="../private/db.ini"):
	config = configparser.ConfigParser()
	config.read(iniFile)
	host=config['mysql']['host']
	port=config['mysql']['port']
	user=config['mysql']['user']
	passwd=config['mysql']['password']
	db=config['mysql']['db']
	vehicle_model_year(host, port, user, passwd, db)

def vehicle_model_year(host, password, db, port=3306, user="root"):
	connection = pymysql.connect(host=host, port=port, user=user, passwd=password, db=db, cursorclass=pymysql.cursors.DictCursor)
	try:
		cursor = connection.cursor()
		cursor.execute("SELECT MAX(id) FROM VehicleModelYear")
		row = cursor.fetchone()
		maxId = row['MAX(id)']
		randIndex = random.randint(0, maxId)

		getVMYQuery = "SELECT * FROM VehicleModelYear WHERE id={}".format(randIndex)
		cursor.execute(getVMYQuery)
		return (cursor.fetchone())

	except Exception as e:
		print(e)
		return 0

# Generate a random vin
def vin_generator():
	return vin.getRandomVin()