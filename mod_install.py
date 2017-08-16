#!/usr/bin/env python3.5

import pip
import importlib
file = open("module_file.txt").readlines()
#print(file)
for dependency in file:
    try:
        importlib.import_module(dependency)
        print(dependency + " file already exist.\n")
    except:
        try:
            pip.main(['install',dependency])
            print("Succesfully installed " + dependency + " file.\n")
        except:
            print("Error installing " + dependency + " file.\n")
			
