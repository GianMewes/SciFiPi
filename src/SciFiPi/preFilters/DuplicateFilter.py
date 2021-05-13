import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy.spatial import distance_matrix

from ..filters.Filter import Filter

class DuplicateFilter(Filter):
	def applyFilter(self, dataFrame:pd.DataFrame):
		# EASY METHOD for detecting exact duplicates
		# iterate through all columns in dataFrame and find equal columns (duplicates) + delete duplicate columns
		listOfColumnPairs_exact = []
		dataFrame_new = dataFrame
		# print(dataFrame_new.shape)
		for i in range(0, len(dataFrame.columns)-2):
			for j in range(i + 1, len(dataFrame.columns)-1):
				if dataFrame.iloc[:,i].equals(dataFrame.iloc[:,j]):
					listOfColumnPair_exact = [i, j]
					listOfColumnPairs_exact.append(listOfColumnPair_exact)
					# rename column i with new name ("i, j"), if column header are different
					if dataFrame_new.columns[listOfColumnPair_exact[0]] == dataFrame_new.columns[listOfColumnPair_exact[1]]:
						new_columnheader = dataFrame_new.columns[listOfColumnPair_exact[0]]
					else:
						new_columnheader = str(dataFrame_new.columns[listOfColumnPair_exact[0]]) + ", " + str(dataFrame_new.columns[listOfColumnPair_exact[1]])
					dataFrame_new.rename(columns = {str(dataFrame_new.columns[listOfColumnPair_exact[0]]):str(new_columnheader)}, inplace=True)
					# delete duplicate column
					dataFrame_new.drop(dataFrame_new.columns[listOfColumnPair_exact[1]], inplace=True, axis=1)
				else:
					pass
		# print(listOfColumnPairs_exact)
		# print(dataFrame_new.shape)

		return dataFrame

		'''# ADVANCED METHOD for detecting different kinds of duplicates
        # calculate similarity of columns, using the cosine similirarity and euclidean distance
		# article https://medium.com/@sasi24/cosine-similarity-vs-euclidean-distance-e5d9a9375fc8 compares both similarity measures
		# both measures have their justification to be used
		similarity_matrix_cosine = 1-cosine_similarity(dataFrame)
		similarity_matrix_euclidean = distance_matrix(dataFrame.values, dataFrame.values)

		# define similarity value for exact, linearTransformed and partial duplicates
		# check if coordinates of exact_duplicates are also 0 in the euclidean distance
		# if YES = exact duplicates
		# if NO = linear transformed duplicates
		similarity_matrix = similarity_matrix_cosine + similarity_matrix_euclidean
		exact_duplicates = np.where(simularity_matrix = 0)
		linearTransformed_duplicates = np.where(simularity_matrix_cosine = 0 and similarity_matrix_euclidean != 0)
		partial_duplicates = np.where(similarity_matrix_cosine > 0.99 & similarity_matrix_cosine < 1)

		# zip the 2 arrays to get the column pairs
		listOfColumnPairs_exact = list(zip(exact_duplicates[0], exact_duplicates[1]))
		listOfColumnPairs_linearTransformed= list(zip(linearTransformed_duplicates[0], linearTransformed_duplicates[1]))
		listOfColumnPairs_partial = list(zip(partial_duplicates[0], partial_duplicates[1]))

		# iterate over the list of coordinates
		for cord_exact in listOfColumnPairs_exact:
			print(cord_exact)

		for cord_linearTransformed in listOfColumnPairs_linearTransformed:
			print(cord_linearTransformed)

		for cord_partial in listOfColumnPairs_partial:
			print(cord_partial)
			
		return dataFrame_new, listOfColumnPairs_exact, listOfColumnPairs_linearTransformed, listOfColumnPairs_partial'''
