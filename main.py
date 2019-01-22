#!/usr/local/bin/python3

import argparse

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
	print("--- Starting Dummy Data Generator! ---")

def main():
	print("Generate some license plates")

if (__name__ == "__main__"):
	parser = argparse.ArgumentParser(description="Arguments for Dummy Data Generator", allow_abbrev=True)
