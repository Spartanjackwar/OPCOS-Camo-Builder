#Jack Moss, aka Spartanjackwar
#Version 6
#Arma 3 camo-build script.
import time
from time import sleep
import os
import datetime
from datetime import date, datetime, time, timedelta
from shutil import copyfile
import configparser
import traceback

#GLOBAL VARIABLES
scriptMode:bool = False
config = None
#---------------------------------------------------------------#
#Function for handling the config file.
#After: returns false if the config does not contain necessary data.  Otherwise returns true
def configLoad():
	global config
	config = configparser.ConfigParser()
	config.read('config.ini')
	
	#Variables for logic
	passedChecks = True
	
	#Section validation
	passedChecks = configValidate(config, "Inputs", None)
	passedChecks = configValidate(config, "Outputs", None)
	
	#Child validation
	passedChecks = configValidate(config, "Inputs", "ConfigC++Template")
	passedChecks = configValidate(config, "Inputs", "Template")
	passedChecks = configValidate(config, "Inputs", "ClassPrefix")
	passedChecks = configValidate(config, "Inputs", "TextureFilePath")
	
	passedChecks = configValidate(config, "Outputs", "RootName")
	passedChecks = configValidate(config, "Outputs", "ConfigFilePath")
	passedChecks = configValidate(config, "Outputs", "FilePath")
	
	return passedChecks #Finished checks!  Passed!
#---------------------------------------------------------------#
#Function to test config sections and variables using try: except: blocks.
#Item is optional, and should be None if not used.  This then just tests the section's existance.
#After: Returns true if check is passed.  False if failed.
def configValidate(file, section : str, item : str):
	if item is None: #Effectively just doin config.has_section()
		try:
			temp = file[section]
		except:
			print("Failure: config.ini data missing: " + section)
			return False
	else: #Effectively just doin config.has_option()
		try:
			temp = file[section][item]
		except:
			print("Failure: config.ini data missing: " + section + ": " + item)
			return False
	#If we got here, then the validate was successful
	return True
#---------------------------------------------------------------#
#logs message to console
def log(message:str):
	log_message = '[' + str(datetime.now()) + ']: '
	log_message = log_message + message
	#log_message = '\n' + log_message #for readability
	#Log to Console
	print(log_message)

#Outputs to a specified file some code via appending to the file's end.
def WriteToFile(logMode: bool, fName:str, code:str):
	try:
		f = fName
		file = open(f, "a")
		file.write(code)
		file.close()
	except FileNotFoundError:
		log("Failure: Wrote code to file: " + fName + " doesn't exist")
		raise FileNotFoundError
	if logMode is 1:
		log("Success: Wrote code to file: " + fName)
	else:
		return

#Reads a template and replaces the strings www, xxx, yyy, and zzz with the parameters
#templateName indicates the file we copy, while outputFileName is the file we write to
def BuildFromTemplate(className:str, alias:str, outputFileName:str, templateName:str, rootConfigID:str):
	file = []
	global config
	prefix = config["Inputs"]["ClassPrefix"]
	texPath = config["Inputs"]["TextureFilePath"]
	
	#Read the template
	with open(templateName) as f:
		file = f.readlines()
	
	#Write lines to a new file
	for line in file:
		line = line.replace("www", prefix)
		line = line.replace("xxx", className)
		line = line.replace("yyy", texPath)
		line = line.replace("zzz", alias)
		if "class" in line and prefix in line and ":" in line:
			newClass = line.split(":", 1)[0]
			WriteUnitList(newClass, rootConfigID)
			log("Created " + newClass)
		WriteToFile(0, outputFileName, line)

#Parses the input from mode 2 to ready for BuildFromTemplate()'s use.  Also writes config includes
def InterpretInput(className:str, alias:str, outputFileName:str, rootConfigID:str):
	templateName:str = None
	global config
	cwd = os.getcwd()
	configOutputPath = cwd + "\\" + config["Outputs"]["RootName"] + "\\addons\\" + config["Outputs"]["ConfigFilePath"] + "\\"
	outputFilePath = configOutputPath + config["Outputs"]["FilePath"] + "\\" + outputFileName
	
	#Build config.cpp if rootConfigID is "Config"
	if rootConfigID is "Config":
		initConfig()
		return
	
	#Build the template
	templateName = cwd + "\\" + "Templates" + "\\" + config["Inputs"]["Template"] + ".cpp"
	BuildFromTemplate(className, alias, outputFilePath, templateName, rootConfigID)
	
	WriteInclude(outputFileName, rootConfigID)

#Writes an include statement to the relevant config file.
def WriteInclude(outputFileName:str, rootConfigID:str):
	global config
	cwd = os.getcwd()
	configOutputPath = config["Outputs"]["RootName"] + "\\addons\\" + config["Outputs"]["ConfigFilePath"] + "\\"
	
	#Build the config.cpp entry
	if rootConfigID is "W":
		configOutputPath = configOutputPath + "cfgWeapons.hpp"
	elif rootConfigID is "M":
		configOutputPath = configOutputPath + "cfgMagazines.hpp"
	elif rootConfigID is "A":
		configOutputPath = configOutputPath + "cfgAmmo.hpp"
	elif rootConfigID is "V":
		configOutputPath = configOutputPath + "cfgVehicles.hpp"
	elif rootConfigID is "3denSubcat":
		filename = "CfG3densubcats.hpp"
	
	#output actual include
	line:str = "#include<" + config["Outputs"]["FilePath"] + "\\" + outputFileName + ".hpp>/t"
	if configOutputPath is not None:
		configOutputPath = cwd + "\\" + configOutputPath
		WriteToFile(False, configOutputPath, line)

#Writes to a list header file whose job is to ensure Zeus works with the items in question
def WriteUnitList(className:str, rootConfigID:str):
	global config
	cwd = os.getcwd()
	configOutputPath = cwd + "\\" + config["Outputs"]["RootName"] + "\\addons\\" + config["Outputs"]["ConfigFilePath"] + "\\"
	filename:str = None
	
	#Evaluate which list to use
	if rootConfigID is "W":
		filename = "WeaponList.hpp"
	elif rootConfigID is "M":
		filename = "MagazineList.hpp"
	elif rootConfigID is "A":
		filename = "AmmoList.hpp"
	elif rootConfigID is "V":
		filename = "UnitList.hpp"
	else:
		return
	
	configOutputPath = configOutputPath + filename
	
	
	line = '"' + className + '",/t'
	WriteToFile(False, configOutputPath, line)

#Starts a new config file from a template of an existiting one.
def initConfig():
	global config
	configOutputPath = config["Outputs"]["RootName"] + "\\addons\\" + config["Outputs"]["ConfigFilePath"] + "\\"
	cwd = os.getcwd()
	configTemplate = cwd + "\\Templates\\" + config["Inputs"]["ConfigC++Template"] + ".hpp"
	
	#Build file
	configOutputPath = cwd + "\\" + configFilePath + "\\" + "config.cpp"
	BuildFromTemplate(config["Outputs"]["ConfigFilePath"], config["Inputs"]["ClassPrefix"], configOutputPath, configTemplate, "Config")
	
#Makes the Directory structure
def CreateDirectory(path:str):
	if not (os.path.isdir(path)): #may fail if os.stat() is not allowed
		try:
			os.mkdir(path) #os.makedirs(x) does exist, but I want to check each directory.
		except OSError:
			log("Failure: Creation of the directory: %s OS error" % path)
			return False
		log("Success: Creation of the directory: %s" % path)
		return True
	else:
		log("Failure: Creation of the directory: %s already exists" % path)
		return False
	
#Removes an item in the file system
def RemoveFilesystemItem(path:str):
	#Logics and variables
	status:bool = True
	logstring = None
	e = None
	
	#Output string options
	dirString = "directory: "
	fileString = "file/item: "
	
	if not os.path.exists(path):
		status = False
	elif(os.path.isdir(path)):	#Path may be a directory
		logString = dirString
		try:
			os.rmdir(path)
		except OSError as e:
			status = False
	else: 						#Path is unquestionably a file
		logString = fileString
		try:
			os.remove(path)
		except OSError as e:
			status = False
	if(status): #Log the result back to the user
		log("Success: Removal of the " + logString + path)
		return status
	else:
		log("Failure: Removal of the " + logString + path)
		return status
	
#Removes the Directory structure
def ClearDirectory(path:str):
	status:bool = True
	subItems = None
	if(os.path.isdir(path)):
		subItems = os.listdir(path)
		for x in subItems:
			item = path + "\\" + x
			status = RemoveFilesystemItem(item)
	else:
		status = RemoveFilesystemItem(path)
	return status

#Initialize file structure.
def Interface_ResetDirectoryStructure():
	global scriptMode
	global config	
	prefix = config["Outputs"]["RootName"]
	
	if not scriptMode:
		print("Are you really sure you want to reset the directory strucutre?")
		confirm:str = input("This will DELETE the folder " + prefix + ", which I will ask for, and its subitems. (Y/N): ")
		if "y" in confirm.lower() and "n" not in confirm.lower():
			prefix = input("Please enter PREFIXNAME: ")
			print("\n")
		else:
			return False
	paths = []
	
	cwd = os.getcwd()
	if not "UNSC Camo Builder" in cwd:
		log("SECURITY ERROR! Attempt at deleting directory outside of the application's folder at " + cwd)
		return False
	
	#Root
	paths.append(cwd + "\\" + prefix)
	paths.append(paths[0] + "\\addons\\")
	#PBO Roots
	paths.append(paths[1] + prefix + "_Uniforms_Army")
	paths.append(paths[1] + prefix + "_Units")
	#@PREFIX\\PREFIX_Uniforms_Army\\
	paths.append(paths[2] + "\\CBU Soldiers")
	paths.append(paths[2] + "\\CBU Uniforms")
	#@PREFIX\\PREFIX_Units\\
	paths.append(paths[3] + "\\Army")
	paths.append(paths[3] + "\\INS")
	paths.append(paths[3] + "\\ODST")
	
	#Note, the delete attempt MUST be done backwards as the order matters to ensure clean directories
	#Since the order matters, the root must be first, followed by the PBO roots, in construction.
	y = len(paths)
	while y > 0:
		y = y - 1
		if os.path.exists(paths[y]):
			ClearDirectory(paths[y])
		else:
			log("Failure: Removal of path " + paths[y] + " does not exist!")
	for z in paths:
		CreateDirectory(z)
	return True

#User Interface	for mode 2
def Interface_template(CN:str, DN:str, OF:str, ID:str):
	global scriptMode
	global config
	
	if not scriptMode:
		CN = input("Please enter CLASSNAME: ")
		DN = input("Please enter DISPLAYNAME: ")
		OF = input("Please enter OUTPUTFILENAME (no file extensions): ")
		ID = input("Please enter config type (W, M, A, V, None, Config): ")
		print("\n")
	InterpretInput(CN, DN, OF, ID)
	print("\n")
	return

#Parses script mode.  Does not resolve mode-specific binds, just assumes mode 2 and passes to menu.
def Interface_Script(FN=None):
	script = []
	command = []
	global scriptMode
	initialScriptMode = scriptMode
	if not scriptMode:
		FN = input("Please enter the script FILENAME (don't include .txt): ")
		FN = "Scripts\\" + FN + ".txt"
	try:
		with open(FN) as f:
			script = f.readlines()
		print("Reading " + FN)
	except:
		print("Failure: File read: " + FN)
		return -1
	
	#Change global mode
	scriptMode = 1
	
	#for x in script:
	for x in range(0, len(script)):
		if (len(script[x]) > 1): #Ignore blank lines
			if "//" not in script[x]: #Ignore comments
				command = script[x].split(';') #Syntax: mode;CN;DN;OF;ID with optional CN;DN;OF;ID
				if(len(command) >= 1):
					m:int = command[0]
					try: #if len(command) is 2
						CN:str = command[1]
					except IndexError: #else
						CN:str = None
					try: #if len(command) is 4
						DN:str = command[2]
						OF:str = command[3]
					except IndexError: #else
						DN:str = None
						OF:str = None
					try: #if len(command) is 5
						ID:str = command[4]
					except IndexError: #else
						ID:str = None	
					Interface_Menu(m, CN, DN, OF, ID)
	
	#Change global mode back
	scriptMode = initialScriptMode

#Changes a line in the config.
#Since the rest of the interface uses a different structure, SectionName will act as PN.
#CN will act as ChildName, and DN will act as NewValue
def Interface_ChangeConfig(SectionName:str=None, ChildName:str=None, NewValue:str=None):
	global scriptMode
	global config
	if not scriptMode:
		SectionName = input("Please enter the config.ini section name: ")
		ChildName = input("Please enter the config.ini child name: ")
		NewValue = input("Please enter the config.ini child's new value: ")
	successString = "Success: Config.ini item change: [" + SectionName + "][" + ChildName + "] = " + NewValue
	failureString = "Failure: Config.ini item change: [" + SectionName + "][" + ChildName + "] = " + NewValue
	try:
		#config.set(SectionName, ChildName, NewValue)
		config[SectionName][ChildName] = NewValue
	except configparser.NoSectionError:
		log(failureString)
		return
	log(successString)
	return

#Handles menu interface.
def Interface_Menu(mode:str, CN:str=None, DN:str=None, OF:str=None, ID:str=None):
	if mode is None:
		return -1
	elif mode is "1": #Script
		Interface_Script(CN)
	elif mode is "2": #Templates
		Interface_Template(CN, DN, OF, ID)
	elif mode is "3": #INI change mode
		Interface_ChangeConfig(CN, DN, OF)
	elif mode is "4": #Reset file structure
		Interface_ResetDirectoryStructure()

	
def main():
	#Init
	global scriptMode
	print("Welcome to the UNSC camouflage warehouse!")
	mode:str = None
	if not configLoad():
		log("ERROR: config.ini load failed.  Aborting program!")
		return 0
	
	#Primary execution loop
	while mode is not "0":
		#Menu prints.
		print("\n")
		print("Mode 0: Quit")
		print("Mode 1: Script execution mode")
		print("Mode 2: Build from template mode")
		print("Mode 3: Config.ini Change")
		print("Mode 4: Reset directory structure")
		print("\n")
		
		#Query user for input
		mode = input("Please select mode: ")
		print("\n")
		
		#Attempt to catch two of the common exceptions.
		try:
			Interface_Menu(mode)
		except FileNotFoundError:
			print("\n")
			traceback.print_exc()
			log("Exception caught: FileNotFoundError")
			scriptMode = 0
		except IndexError:
			print("\n")
			traceback.print_exc()
			log("Exception caught: IndexError")
			scriptMode = 0
		except OSError:
			print("\n")
			traceback.print_exc()
			log("Exception caught: OSError")
			scriptMode = 0
	
	#End
	print ("Oh, I know what the ladies like!")
	return 0
main()