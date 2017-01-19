import os

# Creates new folder for each website in list
def create_dir(directory):
	# If directory/folder doesn't already exist then...
	# create directory/folder
	if not os.path.exists(directory):
		os.makedirs(directory)

# Creates/writes file to path specified for data given
def write_file(path, data):
	f = open(path, "w") # Open path and write file there
	f.write(str(data))
	f.close()

