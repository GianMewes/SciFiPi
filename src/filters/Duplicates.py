import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from filters.Filter import Filter

class Duplicates(Filter):
    def applyFilter(self, dataFrame:pd.DataFrame):
        # calculate similarity of columns, using the cosine similirarity
		similarity_matrix = cosine_similarity(tempDataFrame)
		high_similarities = np.where(similarity_matrix > 0.95)
		# if similarity values of matrix > specific value then column x = column y --> can be merged, IFF there are outliers or missing values
		# column with the lower contribution to the explainability of the data set is dropped

		# zip the 2 arrays to get the exact coordinates
		listOfCoordinates = list(zip(high_similarities[0], high_similarities[1]))

		# iterate over the list of coordinates
		for cord in listOfCoordinates:
			print(cord)

        # other ideas:
		# calculate similarity on distribution, trend

        # TODO : Output muss ein neuer Dataframe sein...

        return dataFrame


		
