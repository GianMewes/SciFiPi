import pandas as pd
import sys
import os
import math
import collections
import pandas._testing as tm
import numpy as np

from FilterBuilder import FilterBuilder
from sklearn.metrics.pairwise import cosine_similarity

from helper.yes_no import yes_no

from FilterBuilder import FilterBuilder


def getFilesInFolder():

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

	return files


if __name__ == '__main__':

	files = getFilesInFolder()

	# list for the individual DataFrames
	li = []

	# format and merge all .csv files to a single DataFrame
	for x in files:

		filterBuilder = FilterBuilder("dirty_data/" + str(x))

		# apply choosen filters
		for x in sys.argv[1:]:
			if x == "formatData": filterBuilder.formatData()
			else: print("Filter '" + x + "' not Found!")

		# TODO: wie erkenne ich den Zeitversatz automatisch?
		if len(files) > 1:
			if x == files[2]:
				filterBuilder.dataFrame = filterBuilder.dataFrame.tz_localize(tz = "Etc/GMT-3")

		tempDataFrame = filterBuilder.getDataFrame()
		
		# add tempDataFrame to list of imported and formated DataFrames and clear variables
		li.append(tempDataFrame)
		del(filterBuilder)
		del(tempDataFrame)

	# li[2] = li[2].tz_convert(tz = "America/Belem")

	if len(li) == 1:
		dataFrame = li[0]
	
	else:
		print("Do Stuff .. ")
		# print(li[0].head())
		''' Merge DataFrames in li with regard to timestamp and signal '''
		# print("\n" + li[0].corrwith(li[0], axis=0))
		dataFrame = pd.concat([x for x in li ], axis=1)

	# print("\n\nCleaned Data Frame: \n\n\n" + str(dataFrame.head()))
	dataFrame.to_csv(r'clean_data/cleaned_data.csv')