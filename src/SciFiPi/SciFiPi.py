import argparse
import pandas as pd
import sys
import os
import collections
import math

from FilterBuilder import FilterBuilder
from PreFilterBuilder import PreFilterBuilder
from cleaners.FormatData import FormatDataFrame
from helper.yes_no import yes_no


class SciFiPi():

	filters = []
	files = []
	df: pd.DataFrame

	def __init__(self):

		# Create the CLI argument parser
		argParser = argparse.ArgumentParser(description='Cleans your ML data set by applying a set of filters')

		# Add CLI arguments
		argParser.add_argument('--filters', metavar='filters', type=str, nargs="+",
		                            help='The list of filters that should be applied to the dataset')

		# User input arguments. Capitalize and prepend "filter" to each one
		userInputFilters = argParser.parse_args().filters
		userInputFilters = [userFilter.capitalize() for userFilter in userInputFilters]
		userInputFilters = ["filter"+userFilter for userFilter in userInputFilters]

		self.getFilesInFolder()

		# Get all PreFilter Methods:
		preFilterBuilder = PreFilterBuilder(self.files)
		preFilterMethods = self.getOwnMethods(preFilterBuilder)

		# Get all Filter Methods
		filterBuilder = FilterBuilder()
		filterMethods = self.getOwnMethods(filterBuilder)

		print(userInputFilters)
		
		# Check for each user: Is it a Prefilter or Filter?
		preFiltersToExecute = []
		filtersToExecute = []
		for userFilter in userInputFilters:
			if (userFilter) in preFilterMethods:
				preFiltersToExecute.append(userFilter)
			elif (userFilter) in filterMethods:
				filtersToExecute.append(userFilter)
			else:
				print("The filter '" + userFilter + "' is neither implemented as a prefilter nor as a filter and will therefore not be called.")

		# Call the prefilters
		for preFilter in preFiltersToExecute:
			try:
				getattr(preFilterBuilder, preFilter)
			except:
				print("Error while calling the prefilter'" + preFilter + "'!")

		# Take the prefilter's dataFrame, pass it to the filterBuilder and call all filters
		# TODO: Wäre hier ein setter nicht cooler? Dann könnte man die selbe Instanz des filterBuilders verwenden.
		filterBuilder.setDataFrame(preFilterBuilder.getDataFrame())
		# dataFrameAfterPreFiltering = preFilterBuilder.getDataFrame()
		# filterBuilder = FilterBuilder(dataFrameAfterPreFiltering)

		for filter in filtersToExecute:
			try:
				getattr(filterBuilder, filter)
			except:
				print("Error while calling the filter '" + filter + "'!")

		
		cleanDataFrame = filterBuilder.getDataFrame()
		cleanDataFrame.to_csv(r'clean_data/cleaned_data.csv')


	def getFilesInFolder(self):

		# get files in input directory and remove all not .csv files from list
		self.files = [x for x in os.listdir("dirty_data/") if '.csv' in x]

		# If there are multiple files
		if len(self.files) > 1:

			print("I found these self.files: " + str(self.files))

			# Identify common prefix in filenames and ask if it's right
			prefix = os.path.commonprefix(self.files)
			if not yes_no("\nIdentified following file prefix: '" +
							prefix + "'   Continue? (y/n) "):
				exit()

			# Generate synthetic files names with series and compare to filenames. If synthetic names == real names, ok. Else: Ciao! & exit()
			synFiles = [(str(prefix) + str(i+1).zfill(math.floor(math.log(len(self.files)))) + ".csv")
						for i in range(len(self.files))]
			if not collections.Counter(self.files) == collections.Counter(synFiles):
				print("\nPrefix wasn't right. Ciao!") & exit()

		return True

	def getOwnMethods(self, obj):
		return [method for method in dir(obj) if not method.startswith('__')]
		



if __name__ == '__main__':

    SciFiPi()
