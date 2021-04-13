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
	
	# If there are multiple files
	if len(files) > 1:

		print("I found these files: " + str(files))

		# Identify common prefix in filenames and ask if it's right
		prefix = os.path.commonprefix(files)
		if not yes_no("\nIdentified following file prefix: '" + prefix + "'   Continue? (y/n) "): exit()

		# Generate synthetic files names with series and compare to filenames. If synthetic names == real names, ok. Else: Ciao! & exit()
		synFiles = [(str(prefix) + str(i+1).zfill(math.floor(math.log(len(files)))) + ".csv") for i in range(len(files))]	
		if not collections.Counter(files) == collections.Counter(synFiles): print("\nPrefix wasn't right. Ciao!") & exit()

	# list for the individual DataFrames
	li = []

	# format and merge all .csv files to a single DataFrame
	for x in files:
	
		tempDataFrame = pd.read_csv("dirty_data/" + str(x))

		filterBuilder = FilterBuilder(tempDataFrame)
		filterBuilder.formatData()

		if x == files[2]:
			filterBuilder.dataFrame = filterBuilder.dataFrame.tz_localize(tz = "Etc/GMT-3")

		tempDataFrame = filterBuilder.fixTimeZone().getDataFrame()
		
		# clear filterBuilder variable
		del(filterBuilder)

		# add tempDataFrame to list of imported and formated DataFrames
		li.append(tempDataFrame)

	li[2] = li[2].tz_convert(tz = "America/Belem")
	print(li[2].head())

	if len(li) == 1:
		dataFrame = li[0]
	
	else:
		print("Do Stuff .. ")

		''' Merge DataFrames in li with regard to timestamp and signal '''
		# print("\n" + li[0].corrwith(li[0], axis=0))
		dataFrame = pd.concat([x for x in li ], axis=1)

	print(dataFrame.head())

	# print("\n\nCleaned Data Frame: \n\n\n" + str(cleanDataFrame))
	dataFrame.to_csv(r'clean_data/clean_data.csv')