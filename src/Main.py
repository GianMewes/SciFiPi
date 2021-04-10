import pandas as pd

from FilterBuilder import FilterBuilder

if __name__ == '__main__':
	df = pd.DataFrame()
	print(str(df))
	
	filterBuilder = FilterBuilder(df)
	cleanDataFrame = filterBuilder.filterMissingValues().getDataFrame()

	print(str(cleanDataFrame))