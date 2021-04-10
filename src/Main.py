import pandas as pd
import locale as loc
from FilterBuilder import FilterBuilder

if __name__ == '__main__':
	df = pd.DataFrame()
	print(str(df))

	filterBuilder = FilterBuilder(df)
	cleanDataFrame = filterBuilder.filterTsCorrection().getDataFrame()

	print(str(cleanDataFrame))