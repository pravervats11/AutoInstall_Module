#!/usr/bin/env python3.5

import pip
import importlib
file = open("module_file.txt").readlines()
#print(file)
failed_packages = []

# Trying to see if a particular module exists and if not then downloading and installing the module.
for dependency in file:
    try:
        importlib.import_module(dependency)
        print(dependency + " file already exist.\n")
    except:
        try:
            pip.main(['install',dependency])
            print("\n Succesfully installed " + dependency + " file.\n")
        except:
            failed_packages.append(dependency)
print("\n These are the list of failed packages: \n")

# Printing all the failed packages
for packages in failed_packages:
    print(packages + "\n")
			
