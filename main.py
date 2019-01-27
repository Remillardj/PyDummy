#!/usr/local/bin/python3

import argparse
import random
from dummy import dummy

def welcome():
	print("""\
		  _____                                    _____        _           _____                           _             
		 |  __ \                                  |  __ \      | |         / ____|                         | |            
		 | |  | |_   _ _ __ ___  _ __ ___  _   _  | |  | | __ _| |_ __ _  | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
		 | |  | | | | | '_ ` _ \| '_ ` _ \| | | | | |  | |/ _` | __/ _` | | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
		 | |__| | |_| | | | | | | | | | | | |_| | | |__| | (_| | || (_| | | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
		 |_____/ \__,_|_| |_| |_|_| |_| |_|\__, | |_____/ \__,_|\__\__,_|  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
		                                    __/ |                                                                         
		                                   |___/                                                                          
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
		7 : "vehicle_model_year"
	}
	try:
		return(d[number])
	except KeyError:
		return False

def main(count, limbo = []):
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
	return output

if (__name__ == "__main__"):
	parser = argparse.ArgumentParser(description="Arguments for PyDummy Data Generator", allow_abbrev=True)
	parser.add_argument("--version", action="version", version="PyDummy 0.0.2")
	parser.add_argument("-c", "--count", help="Number of times to generate dummy data", default=1, type=int)
	#parser.add_argument("-f", "--file-type", help="File type to generate", default="sql", action="store_true")
	parser.add_argument("--license-plate", help="Generate a license plate", default=False, action="store_true", dest="license")
	parser.add_argument("--phone-number", help="Generate a phone number", default=False, action="store_true", dest="phone")
	parser.add_argument("--full-name", help="Generate a full name", default=False, action="store_true", dest="full")
	parser.add_argument("--first-name", help="Generate a first name", default=False, action="store_true", dest="first")
	parser.add_argument("--last-name", help="Generate a last name", default=False, action="store_true", dest="last")
	parser.add_argument("--email", help="Generate an email", default=False, action="store_true", dest="email")
	parser.add_argument("--get-manufactorer", help="Generate a manufactorer", default=False, action="store_true", dest="manufactor")
	parser.add_argument("--vehicle-model-year", help="Generate a vehicle, model, and year", default=False, action="store_true", dest="vmy")
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
	if (args.manufactor):
		limbo.append(6)
	if (args.vmy):
		limbo.append(7)

	# Generate dat data
	main(count, limbo)
