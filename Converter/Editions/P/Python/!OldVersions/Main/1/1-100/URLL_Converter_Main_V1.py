#!/usr/bin/env python3.7.1
# Start of script
# This is the Python edition of the URLL converter software LIBrary. There will be versions written in other languages as well
# Planned editions at the moment: Java, C#, C++, Ruby, Elm, D, V, Eiffel, Fortran, Haskell, Lua
""" Section index
1. Import section
2. Variable section
3. Functions section
4. Program section
"""
''' Import section '''
import os()
import pygui()
''' Variables section '''
SupportedTypesLS = [".url", ".URL", ".lnk", ".LNK"]
''' Functions section '''
def url_To_URLL_convert():
	# URL to URLL converter function
	# Function coming soon
	print("Converting URL to URLL")
	print(os.filename(target) + " is being converted")
	print("This feature is not ready yet, and is coming soon")
	break
def lnk_To_URLL_convert():
	# LNK to URLL converter function
	# Function coming soon
	print("Converting LNK to URLL")
	print(os.filename(target) + " is being converted")
	print("This feature is not ready yet, and is coming soon")	
	break
def urll_To_URL_convert():
	# URLL to URL converter function
	# Function coming soon
	print("Converting URLL to URL")
	print(os.filename(target) + " is being converted")
	print("This feature is not ready yet, and is coming soon")
	break
def urll_To_LNK_convert():
	# URLL to LNK converter function
	# Function coming soon
	print("Converting URLL to LINK")
	print(os.filename(target) + " is being converted")
	print("This feature is not ready yet, and is coming soon")
	break
def main():
	print("URLL converter")
	""" Obsolete
	print("\nHow would you like to convert?")
	print("url to URLL | ID: 1")
	print("URLL to URL | ID: 2")
	print("lnk to URLL | ID: 3")
	print("URLL to lnk | ID: 4")
	console1 = input("Enter an ID to begin the conversi)
	"""
	os.file = input("Upload one or more files")
	if (os.file.suffix == ".url"):
		return url_To_URLL_convert():
		break
	elif (os.file.suffix == ".lnk"):
		return lnk_To_URLL_convert()
		break
	else (os.file.suffix == ".urll")
		print("What format would you like to convert this file to?\n")
		print("URL | ID: 1")
		print("LNK | ID: 2")
		console1 = input("Enter an ID to continue: ")
		if (console1 == "1"):
			return urll_To_URL_convert()
			break
		elif (console1 == "2"):
			return urll_To_LNK_convert()
			break
		else:
			print("Invalid ID. Please try again")
			return 0
			break
''' Program section '''
return main()
return 0
break
'''
File info
File type: Python source file (*.py)
File version: 1 (2022, Monday, April 25th at 4:10 pm PST)
Line count (including blank lines and compiler line): 115
'''
""" Notes
This is an offline program. The term `upload` here just means to import
This program is not yet functional
"""
''' Todo
Account for all URLL syntax and features
Check to make sure only URL, LNK, and URLL files are being uploaded, and others are included
Catch upload errors (such as a binary file being uploaded, a spoofed file, etc)
Maintain security and performance
Make the program functional
Enable error handling
'''
"""
Changelog
V1: 2022, Monday, April 25th at 4:10 pm PST
Changes:
Started the file
Included a shebang for Python 3.7.1
Added the 4 sections (Import section, Variable section, Functions section, Program section)
Added import statements for 2 libraries
Added the lnk, url, to urll, and urll to lnk, url functions
Added a todo section
Added the notes section
Adde dthe main function
Added the file info section
No other changes in version 1
"""
# End of script
