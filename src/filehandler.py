from zipfile import ZipFile
import os

import src.print as printer

def get_all_file_paths(directory):
	# initializing empty file paths list
	file_paths = []
  
	# crawling through directory and subdirectories
	for root, directories, files in os.walk(directory):
		for filename in files:
			# join the two strings in order to form the full filepath.
			filepath = os.path.join(root, filename)
			file_paths.append(filepath)
  
	# returning all file paths
	return file_paths

def get_consolidated_path(paths:list, zipname:str):
	# check if we even need to do this by checking if there is only one path, and if it is a file
	if(len(paths) == 1):
		if os.path.isfile(paths[0]):
			return paths[0], False

	# initializing empty file paths list
	file_paths = []

	# Iterate over paths and get consolidated list to zip up
	for path in paths:		
		if os.path.isfile(path):
			file_paths.append(path)
		elif os.path.isdir(path):
			file_paths.extend(get_all_file_paths(path))

	# Zip all files
	zipname = zipname + '.zip'
	with ZipFile(zipname, 'w') as zip:
		counter=0
		for file in file_paths:
			printer.print_percent_done(counter, len(file_paths), title="Zipping files")
			zip.write(file)
			counter += 1

	return zipname, True

def extract_zip(filename:str):
	# opening the zip file in READ mode
	with ZipFile(filename, 'r') as zip:
		# extracting all the files
		zip.extractall()