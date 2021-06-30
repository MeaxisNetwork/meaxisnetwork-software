# Python Modules
import configparser
import keyring
import os

from meaxisnetwork import accounts

# Load Config & Credentials
config = configparser.ConfigParser()

logcook = keyring.get_password("MeaxisNetwork Launcher", "logcook")
sesscook = keyring.get_password("MeaxisNetwork Launcher", "sesscook")

print("Starting MeaxisNetwork Launcher ")

# Check for valid credentials
if logcook and sesscook and logcook != "NONE" and sesscook != "NONE":
	print('Yay, it works!')

	try:
		accounts.Account("hello", "world")
	except:
		print("Invalid session in MeaxisNetwork Launcher: Running login sequence")

		logcook = "NONE"
		sesscook = "NONE"
else:
	print("Unauthenticated MeaxisNetwork Launcher: Running login sequence")
	os.system('python login.py')
