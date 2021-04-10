import pandas as pd
import os
import math
import collections
import pandas._testing as tm
import numpy as np

from FilterBuilder import FilterBuilder

def yes_no(answer):
    yes = set(['y'])
    no = set(['n'])
     
    while True:
        choice = input(answer).lower()
        if choice in yes:
           return True
        elif choice in no:
           return False
        else:
           print("Please respond with 'y' or 'n' ")

if __name__ == '__main__':

	# get files in input directory and remove all not .csv files from list
	files = [x for x in os.listdir("dirty_data/") if '.csv' in x]

	# If multiple files, check if namingscheme is given and if series assumption ist right.
	if len(files) > 1:
	
		print("I found these files: " + str(files))
		prefix = os.path.commonprefix(files)
		if not yes_no("\nIdentified following file prefix: '" + prefix + "'   Continue? (y/n) "): exit()
		synFiles = [(str(prefix) + str(i+1).zfill(math.floor(math.log(len(files)))) + ".csv") for i in range(len(files))]	
		if not collections.Counter(files) == collections.Counter(synFiles): print("\nPrefix wasn't right. Ciao!") & exit()
		combined_csv = pd.concat([pd.read_csv("dirty_data/" + x).pivot(index="time", columns="signal", values="value") for x in files ], axis=1)
		

	print(combined_csv)


		
		
	''' If naming scheme is given, check timezones.
	If naming scheme is given, merge files '''

	# path = "dirty_data/" + files[0]

	# filterBuilder = FilterBuilder(path)
	# cleanDataFrame = filterBuilder.filterMatrix().getDataFrame()
	# print("\n\nCleaned Data Frame: \n\n\n" + str(cleanDataFrame))
	# cleanDataFrame.to_csv(r'clean_data/clean_data.csv')