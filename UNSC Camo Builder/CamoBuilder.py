#Jack Moss, aka Spartanjackwar
#Version 5
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
	passedChecks = configValidate(config, "Template_File_Names", None)
	
	#Children validation
	passedChecks = configValidate(config, "Template_File_Names", "M52A")
	passedChecks = configValidate(config, "Template_File_Names", "M52D")
	passedChecks = configValidate(config, "Template_File_Names", "CBU_Soldiers")
	passedChecks = configValidate(config, "Template_File_Names", "CBU_Uniforms")
	passedChecks = configValidate(config, "Template_File_Names", "3den_subcat")
	
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
	
#Creates new uniform using a hardcoded template
def LEGACY_New_U(prefix:str, fName:str, className:str, alias:str, parentName:str):
	uniform = prefix + "_UNSC_Army_Uniform_" + className
	code = [None] * 8
	
	code[0] = "class " + uniform + ": " + parentName + "\n"
	code[1] = "{\n"
	code[2] = '\tdisplayName = "Cross-Branch BDU ' + alias + '";\n'
	code[3] = "\tclass ItemInfo: ItemInfo\n"
	code[4] = "\t{\n"
	code[5] = '\t\tuniformClass = "' + prefix + '_UNSC_Army_Soldier_' + className + '";\n'
	code[6] = "\t};\n"
	code[7] = "};\n"
	
	for line in code:
		WriteToFile(0, fName, line)
	log("Class created: " + uniform)

#Creates new soldier using a hardcoded template
def LEGACY_New_S(prefix:str, fName:str, className:str, parentName:str, texA:str, texB:str, model:str):
	soldier = prefix + "_UNSC_Army_Soldier_" + className
	code = [None] * 6
	
	code[0] = "class " + soldier + ": " + parentName + "\n"
	code[1] = "{\n"
	code[2] = '\tuniformClass = "' + prefix + '_UNSC_Army_Uniform_' + className + '";\n'
	
	#If slimleg variant, use selections.  If base variant, then don't use textures.
	if "_SlimLeg" in className:
		code[3] = '\thiddenSelections[] = {"camo", "camo2", "insignia", "clan", "A_BaseLeg"};\n'
	elif className + "_S" not in soldier and className + "_R" not in soldier:
		code[3] = '\thiddenSelectionsTextures[] = {"' + texA + '", "' + texB + '"};\n'
	elif className + "_R" in soldier: #If rolled, then apply B tex in both slots
		code[3] = '\thiddenSelectionsTextures[] = {"' + texB + '", "' + texB + '"};\n'
	else:
		code[3] = ""
	
	#Efficiency note: the elif can stop at the first elif and cut out the check for _R.
	#This leaves programmer work to input texB for both texA and texB parameters.
	
	if model is not None:
		code[4] = '\tmodel = "' + model + '";\n'
	else:
		code[4] = ""
		
	code[5] = "};\n"
	
	for line in code:
		WriteToFile(0, fName, line)
	log("Class created: " + soldier)

#Creates a new Vest set.  fName here is the template used
def LEGACY_New_V(prefix:str, fName:str, className:str, alias:str, outputName:str): #, texA:str, texB:str):
	filePath = prefix + r"_Uniforms_Army\data"
	output = outputName + className + ".hpp"
	BuildFromTemplate(prefix, fName, output, className, filePath, alias)
	log("Finished compiling " + className + " vests")
	
#Creates a new item set from a template.  Is used for vests and uniforms.
#Appends classname and .hpp to all output files.
def New_Item(prefix:str, fName:str, className:str, alias:str, outputName:str, consoleString:str):
	OutputVariableFilePath = prefix + r"_Uniforms_Army\data"
	output = outputName + className + ".hpp"
	BuildFromTemplate(prefix, fName, output, className, OutputVariableFilePath, alias)
	log("Finished compiling " + className + " " + consoleString)
	
#Reads a template and replaces the strings www, xxx, yyy, and zzz with the parameters
#fName indicates the file we copy, while outputFile is the file we write to
def BuildFromTemplate(prefix:str, fName:str, outputFile:str, className:str, filePath:str, alias:str):
	file = []
	
	#Read the template
	with open(fName) as f:
		file = f.readlines()
	
	#Write lines to a new file
	for line in file:
		line = line.replace("www", prefix)
		line = line.replace("xxx", className)
		line = line.replace("yyy", filePath)
		line = line.replace("zzz", alias)
		if "class" in line and prefix in line and ":" in line:
			log("Created " + line.split(":", 1)[0])
		WriteToFile(0, outputFile, line)

#Creates a new Unit set for Army units.  fName here is the template used
def New_Units(prefix:str, TemplateFName:str, outputName:str, className:str, alias:str, subfolder:str, logMode:bool):
	if (TemplateFName and subfolder):
		cwd = os.getcwd()
		TemplateFName = cwd + "\\Templates\\" + TemplateFName + ".hpp"
		outputName = cwd + "\\@" + prefix + "\\addons\\" + prefix + "_Units\\" + subfolder + "\\" + outputName + ".hpp"
		filePath = prefix + "_Units\\" #Shouldn't really be used in this template, but just in case.
		
		BuildFromTemplate(prefix, TemplateFName, outputName, className, filePath, alias)
		
		if logMode is 1:
			log("Finished compiling " + className + " units in " + filePath)
	else:
		log("You bloody errored and gave me an invalid, thus likely NULL, filename or subfolder.")

#Creates a whole OPTRE soldier + uniform combo	
def LEGACY_New_BDU(prefix:str, className:str, alias:str):
	#Setup aliases
	path = os.getcwd() + "\\@" + prefix + "\\addons\\"
	Normal = "[" + alias + "]"
	slim = "(Slim Legs) [" + alias + "]"
	short = "(Short) [" + alias + "]"
	rolled = "(Rolled) [" + alias + "]"
	rolledSlim = "(Rolled / Slim Legs) [" + alias + "]"
	shortSlim = "(Short / Slim Legs) [" + alias + "]"
	fNameS = path + prefix + "_Uniforms_Army\\CBU Soldiers\\Soldiers_" + className + ".hpp"
	fNameU = path + prefix + "_Uniforms_Army\\CBU Uniforms\\Uniforms_" + className + ".hpp"
	fNameUnits = "Units" + className + ".hpp"
	
	#Setup inheritance
	standard = prefix + "_UNSC_Army_Uniform_" + className
	base = "OPTRE_UNSC_Army_Uniform_WDL"
	
	#Call the uniform creation
	LEGACY_New_U(prefix, fNameU, className, Normal, base) #Standard
	LEGACY_New_U(prefix, fNameU, className + "_SlimLeg", slim, standard) #Slim
	LEGACY_New_U(prefix, fNameU, className + "_S", short, standard) #Short
	LEGACY_New_U(prefix, fNameU, className + "_R", rolled, standard) #Rolled
	LEGACY_New_U(prefix, fNameU, className + "_R_SlimLeg", rolledSlim, standard + "_R")
	LEGACY_New_U(prefix, fNameU, className + "_S_SlimLeg", shortSlim, standard + "_S")
	log("Finished configuring " + alias + " camouflage uniforms") #log uniform call
	
	#Setup Models
	#uNorm = "\OPTRE_UNSC_Units\Army\uniform.p3d"
	uShort = r"\OPTRE_UNSC_Units\Army\uniform_short.p3d"  #The r prefixing the string allows \
	uRoll = r"\OPTRE_UNSC_Units\Army\uniform_rolled.p3d"
	
	#Setup inheritance
	standard = prefix + "_UNSC_Army_Soldier_" + className
	#base = prefix + "_UNSC_Army_Soldier_WDL"
	base = "OPTRE_UNSC_Army_Soldier_WDL"
	
	#Setup files
	texA = prefix + r"_Uniforms_Army\data\Uniform_" + className + "_a_CO.paa"
	texB = prefix + r"_Uniforms_Army\data\Uniform_" + className + "_b_CO.paa"
	
	LEGACY_New_S(prefix, fNameS, className, base, texA, texB, None) #Standard
	LEGACY_New_S(prefix, fNameS, className + "_SlimLeg", standard, texA, texB, None) #Slim
	LEGACY_New_S(prefix, fNameS, className + "_S", standard, texA, texB, uShort) #Short
	LEGACY_New_S(prefix, fNameS, className + "_R", standard, texB, texB, uRoll) #Rolled
	LEGACY_New_S(prefix, fNameS, className + "_S_SlimLeg", standard + "_S", texB, texB, None) #Rolled
	LEGACY_New_S(prefix, fNameS, className + "_R_SlimLeg", standard + "_R", texB, texB, None) #Rolled
	log("Finished configuring " + alias + " camouflage soldiers") #log soldiers call

#Creates a whole soldier + uniform combo
def New_BDU(prefix:str, className:str, alias:str):
	global config
	#File Paths
	path = os.getcwd() + "\\@" + prefix + "\\addons\\"
	fNameS = path + prefix + "_Uniforms_Army\\CBU Soldiers\\Soldiers_"
	fNameU = path + prefix + "_Uniforms_Army\\CBU Uniforms\\Uniforms_"
	TemplateU = "Templates\\" + config["Template_File_Names"]["CBU_Uniforms"] + ".hpp"
	TemplateS = "Templates\\" + config["Template_File_Names"]["CBU_Soldiers"] + ".hpp"
	
	New_Item(prefix, TemplateU, className, alias, fNameU, "uniforms")
	print("\n")
	New_Item(prefix, TemplateS, className, alias, fNameS, "soldiers")
	
	return
	
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
def Interface_ResetDirectoryStructure(prefix:str):
	global scriptMode
	if not scriptMode:
		print("Are you really sure you want to reset the directory strucutre?")
		confirm:str = input("This will DELETE the folder @PREFIX, which I will ask for, and its subitems. (Y/N): ")
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
	paths.append(cwd + "\\@" + prefix)
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
		
#Builds a new uniform-soldier pair
def Interface_U(PN=None, CN=None, DN=None, TT=None):
	global scriptMode
	if not scriptMode:
		PN = input("Please enter PREFIXNAME: ")
		CN = input("Please enter CLASSNAME: ")
		DN = input("Please enter DISPLAYNAME: ")
		print("\n")
	New_BDU(PN, CN, DN)
	print("\n")
	return

#Builds a new unit set.
def Interface_Units(PN=None, CN=None, DN=None, TT=None, SF=None):
	global scriptMode
	if not scriptMode:
		PN = input("Please enter PREFIXNAME: ")
		CN = input("Please enter CLASSNAME: ")
		DN = input("Please enter DISPLAYNAME: ")
		TT = input("Please enter UNITS TEMPLATENAME (Don't include the .hpp/.cpp/.h): ")
		SF = input("Please enter SUBFOLDERNAME of " + PN + "_Units: ")
		print("\n")
	unitFileOutputName = TT.replace("xxx", CN)
	TC = config["Template_File_Names"]["3den_subcat"]
	categoryOutputName = TC.replace("xxx", CN)
	
	New_Units(PN, TC, categoryOutputName, CN, DN, SF, False)
	New_Units(PN, TT, unitFileOutputName, CN, DN, SF, True)
	return

#Builds a new vest.
def Interface_V(PN=None, CN=None, DN=None, mode:int=0):
	global scriptMode
	global config
	M52A_Tempalte_Name = "Templates\\" + config["Template_File_Names"]["M52A"] + ".hpp"
	M52D_Tempalte_Name = "Templates\\" + config["Template_File_Names"]["M52D"] + ".hpp"
	cwd = os.getcwd()
	
	if not scriptMode:
		PN = input("Please enter PREFIXNAME: ")
		CN = input("Please enter CLASSNAME: ")
		DN = input("Please enter DISPLAYNAME: ")
		print("\n")
	if mode is 0: #M52A
		#LEGACY_New_V(PN, M52A_Tempalte_Name, CN, DN, "VestsARMY_")
		outputName = cwd + "\\@" + PN + "\\addons\\" + PN + "_Uniforms_Army\\" + "VestsODST_"
		New_Item(PN, M52A_Tempalte_Name, CN, DN, outputName, "vests")
	elif mode is 1: #M52D
		#LEGACY_New_V(PN, M52D_Tempalte_Name, CN, DN, "VestsODST_")
		outputName = cwd + "\\@" + PN + "\\addons\\" + PN + "_Uniforms_Army\\" + "VestsODST_"
		New_Item(PN, M52D_Tempalte_Name, CN, DN, outputName, "vests")
	else:
		log("ERROR!  Incorrect mode in Interface_V()!  Please complain to the programmer for a patch")
	print("\n")
	return

def Interface_Script(FN=None):
	script = []
	command = []
	
	global scriptMode
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
				command = script[x].split(';') #Syntax: mode;PN;CN;DN;TT;SF with optional CN;DN;TT;SF
				if(len(command) > 1):
					m:int = command[0]
					PN:str = command[1]
					try: #if len(command) is 4
						CN:str = command[2]
						DN:str = command[3]
					except IndexError: #else
						CN = None
						DN = None
					try: #if len(command) is 5:
						TT:str = command[4]
						SF:str = command[5]
					except IndexError: #else:
						TT:str = None
						SF:str = None
					Interface_Menu(m, PN, CN, DN, TT, SF)
	
	#Change global mode back
	scriptMode = 0

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
def Interface_Menu(mode:str, PN:str=None, CN:str=None, DN:str=None, TT:str=None, SF:str=None):
	if mode is None:
		return -1
	elif mode is "1": #CBU
		Interface_U(PN, CN, DN, TT)
	elif mode is "2": #M52A
		Interface_V(PN, CN, DN, 0)
	elif mode is "3": #M52D
		Interface_V(PN, CN, DN, 1)
	elif mode is "4": #Units
		Interface_Units(PN, CN, DN, TT, SF)
	#elif mode is "5": #Not implemented yet.  Not sure what it'll be either
	elif mode is "6": #Change config settings mode
		Interface_ChangeConfig(PN, CN, DN)
	elif mode is "7": #Script Mode
		Interface_Script()
	elif mode is "8": #ResetDirectoryMode
		Interface_ResetDirectoryStructure(PN)
	#quit = input("Quit? (Y/N): ")

	
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
		print("Mode 1: Cross Branch Uniform")
		print("Mode 2: M52A Vests")
		print("Mode 3: M52D Vests")
		print("Mode 4: Units Creation")
		#print("Mode 5: I don't know what this is yet")
		print("Mode 6: Config.ini Change")
		print("Mode 7: Script execution mode")
		print("Mode 8: Reset directory structure")
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