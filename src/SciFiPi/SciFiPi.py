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
		self.getFilesInFolder()
		
		# Get all PreFilter and Filter methods:
		preFilterMethods = self.getOwnMethods(PreFilterBuilder)
		filterMethods = self.getOwnMethods(FilterBuilder)

		# Create the CLI argument parser
		argParser = argparse.ArgumentParser(prog='SciFiPi', description='Cleans your ML data set by applying a set of filters', formatter_class=argparse.RawTextHelpFormatter)

		# Add CLI arguments
		argParser.add_argument('--filters', metavar='filter', type=str, nargs="+",
		                            help='The list of filters that should be applied to the dataset. Currently, the following filters can be applied: \nPrefilters: ' + str(list(preFilterMethods.keys())) + "\nFilters: " + str(list(filterMethods.keys())))


		# User input arguments. Convert to lower case and prepend "filter" to each one
		userInputFilters = argParser.parse_args().filters
		userInputFilters = [userFilter.lower() for userFilter in userInputFilters]


		# Check for each userFilter: Is it a Prefilter or Filter?
		preFiltersToExecute = []
		filtersToExecute = []
		for userFilter in userInputFilters:
			if userFilter in preFilterMethods:
				preFiltersToExecute.append(preFilterMethods[userFilter])

			elif userFilter in filterMethods:
				filtersToExecute.append(filterMethods[userFilter])

			else:
				print("The filter '" + userFilter + "' is neither implemented as a prefilter nor as a filter and will therefore not be called.")

		# Call the prefilters
		preFilterBuilder = PreFilterBuilder(self.files)
		for preFilter in preFiltersToExecute:
			try:
				getattr(preFilterBuilder, preFilter)()
			except Exception as err:
				print("Error while calling the prefilter '" + preFilter + "'! Error: " + str(err))

		# Take the prefilter's dataFrame, pass it to the filterBuilder and call all filters
		filterBuilder = FilterBuilder(preFilterBuilder.getDataFrame())

		for filter in filtersToExecute:
			try:
				getattr(filterBuilder, filter)()
			except Exception as err:
				print("Error while calling the filter '" + filter + "'! Error: " + str(err))

		
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


	def getOwnMethods(self, className):
		"""
		Creates a dictionary of the objects methods. Keys are the lower case method names, values the correct names
		"""
		methods = [method for method in dir(className) if method.startswith('filter')]
		methodDict = {}
		for method in methods:
			lowCaseMethod = method.lower().removeprefix("filter")
			methodDict[lowCaseMethod] = method
		return methodDict



if __name__ == '__main__':

    SciFiPi()
