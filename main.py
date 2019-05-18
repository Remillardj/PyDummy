#!/usr/local/bin/python3

import argparse
import random
import multiprocessing
from threading import Thread
import os
import time

from dummy import dummy
from dummy import toformat

def welcome():
	print("""\

		____ ___  _ ____  _     _      _     ___  _   _____ _____ _      _____ ____  ____  _____  ____  ____ 
		/  __\\  \///  _ \/ \ /\/ \__/|/ \__/|\  \//  /  __//  __// \  /|/  __//  __\/  _ \/__ __\/  _ \/  __\
		|  \/| \  / | | \|| | ||| |\/||| |\/|| \  /   | |  _|  \  | |\ |||  \  |  \/|| / \|  / \  | / \||  \/|
		|  __/ / /  | |_/|| \_/|| |  ||| |  || / /    | |_//|  /_ | | \|||  /_ |    /| |-||  | |  | \_/||    /
		\_/   /_/   \____/\____/\_/  \|\_/  \|/_/     \____\\____\\_/  \|\____\\_/\_\\_/ \|  \_/  \____/\_/\_\
																											
								
	""")
	print("--- Starting PyDummy Data Generator! ---")


# Lookup table for the appropriate function to run
def lookup_table(number):
	d = {
		0 : "license_plate",
		1 : "phone_number",
		2 : "full_name",
		3 : "first_name",
		4 : "last_name",
		5 : "email",
		6 : "get_manufactorer",
		7 : "vehicle_model_year",
		8 : "vin_generator"
	}
	try:
		return(d[number])
	except KeyError:
		return False

def generate_data(count, limbo = []):
	output = {}
	gender = ['male', 'female']
	for value in limbo:
		if (lookup_table(value) == "license_plate"):
			tmp = []
			for _ in range(count):
				tmp.append(dummy.license_plates())
			output['license_plates'] = tmp
		if (lookup_table(value) == "phone_number"):
			tmp = []
			for _ in range(count):
				tmp.append(dummy.phone_number())
			output['phone_number'] = tmp
		if (lookup_table(value) == "full_name"):
			tmp = []
			for _ in range(count):
				tmp.append(dummy.full_name(random.choice(gender)))
			output['full_name'] = tmp
		if (lookup_table(value) == "first_name"):
			tmp = []
			for _ in range(count):
				tmp.append(dummy.first_name(random.choice(gender)))
			output['first_name'] = tmp
		if (lookup_table(value) == "last_name"):
			tmp = []
			for _ in range(count):
				tmp.append(dummy.last_name())
			output['last_name'] = tmp
		if (lookup_table(value) == "email"):
			tmp = []
			for _ in range(count):
				tmp.append(dummy.generate_email())
			output['email'] = tmp
		if (lookup_table(value) == "get_manufactorer"):
			tmp = []
			for _ in range(count):
				tmp.append(dummy.get_manufactorers())
			output['get_manufactorer'] = tmp
		if (lookup_table(value) == "vehicle_model_year_api"):
			tmp = []
			for _ in range(count):
				tmp.append(dummy.vehicle_model_year_api())
			output['vehicle_model_year'] = tmp
		if (lookup_table(value) == "vin_generator"):
			tmp = []
			for _ in range(count):
				tmp.append(dummy.vin_generator())
			output['vin_generator'] = tmp
	return output

'''
 Refactored function of generate_date() to allow a more threading friendly function
 Parameters:
 	count -> int: number of times to generate the data
 	value -> int: the data type to generate, uses the lookup table
'''
def generate_data_threading(count, value):
	gender = ['male', 'female']
	tmp = []
	if (lookup_table(value) == "license_plate"):
		for _ in range(count):
			tmp.append(dummy.license_plates())
		output['license_plates'] = tmp
	if (lookup_table(value) == "phone_number"):
		for _ in range(count):
			tmp.append(dummy.phone_number())
		output['phone_number'] = tmp
	if (lookup_table(value) == "full_name"):
		for _ in range(count):
			tmp.append(dummy.full_name(random.choice(gender)))
		output['full_name'] = tmp
	if (lookup_table(value) == "first_name"):
		for _ in range(count):
			tmp.append(dummy.first_name(random.choice(gender)))
		output['first_name'] = tmp
	if (lookup_table(value) == "last_name"):
		for _ in range(count):
			tmp.append(dummy.last_name())
		output['last_name'] = tmp
	if (lookup_table(value) == "email"):
		for _ in range(count):
			tmp.append(dummy.generate_email())
		output['email'] = tmp
	if (lookup_table(value) == "get_manufactorer"):
		for _ in range(count):
			tmp.append(dummy.get_manufactorers())
		output['get_manufactorer'] = tmp
	if (lookup_table(value) == "vehicle_model_year_api"):
		for _ in range(count):
			tmp.append(dummy.vehicle_model_year_api())
		output['vehicle_model_year'] = tmp
	if (lookup_table(value) == "vin_generator"):
		for _ in range(count):
			tmp.append(dummy.vin_generator())
		output['vin_generator'] = tmp

if (__name__ == "__main__"):
	parser = argparse.ArgumentParser(description="Arguments for PyDummy Data Generator", allow_abbrev=True)
	parser.add_argument("--version", action="version", version="PyDummy 0.0.4")
	parser.add_argument("-c", "--count", help="Number of times to generate dummy data", default=1, type=int)
	parser.add_argument("-i", "--insert", help="Create insert statements", default=True, action="store_true")
	parser.add_argument("-d", "--delete", help="Create delete statements", default=False)
	parser.add_argument("--column", help="Designated column to delete", type=str)
	parser.add_argument("--pk", help="Designated Primary Key to use to delete via WHERE clause")
	parser.add_argument("-t", "--table", help="Name of table to insert or delete from", default="pydummy")
	#parser.add_argument("-f", "--file-type", help="File type to generate", default="sql", action="store_true")
	parser.add_argument("--license-plate", help="Generate a license plate", default=False, action="store_true", dest="license")
	parser.add_argument("--phone-number", help="Generate a phone number", default=False, action="store_true", dest="phone")
	parser.add_argument("--full-name", help="Generate a full name", default=False, action="store_true", dest="full")
	parser.add_argument("--first-name", help="Generate a first name", default=False, action="store_true", dest="first")
	parser.add_argument("--last-name", help="Generate a last name", default=False, action="store_true", dest="last")
	parser.add_argument("--email", help="Generate an email", default=False, action="store_true", dest="email")
	#parser.add_argument("--get-manufactorer", help="Generate a manufactorer", default=False, action="store_true", dest="manufactor")
	#parser.add_argument("--vehicle-model-year", help="Generate a vehicle, model, and year", default=False, action="store_true", dest="vmy")
	parser.add_argument("--vin-generator", help="Generate a random fake VIN", default=False, action="store_true", dest="vin")
	args = parser.parse_args()

	# Handle arguments
	count = args.count
	limbo = []
	if (args.license):
		limbo.append(0)
	if (args.phone):
		limbo.append(1)
	if (args.full):
		limbo.append(2)
	if (args.first):
		limbo.append(3)
	if (args.last):
		limbo.append(4)
	if (args.email):
		limbo.append(5)
	# TODO: currently there is a bug with both these options, will fix later
	#if (args.manufactor):
		#limbo.append(6)
	#if (args.vmy):
		#limbo.append(7)
	if (args.vin):
		limbo.append(8)

	if (args.insert):
		output = {}
		threads = []
		for value in limbo:
			threads.append(Thread(target=generate_data_threading, args=(count, value)))

		for thread in threads:
			thread.start()

		for thread in threads:
			thread.join()

		toformat.sql_insert_query(args.table, list(output.keys()), list(output.values()))
	elif (args.delete and args.column and args.pk):
		for _ in range(count):
			toformat.sql_delete_query(args.table, args.column, args.pk)
	else:
		print("Please enter arguments")
		exit(1)

