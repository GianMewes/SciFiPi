import pandas as pd
import numpy as np

from helper.yes_no import yes_no
from filters.Filter import Filter

class FormatDataFrame(Filter):

	def applyFilter(self, dataFrame:pd.DataFrame):
		if len((dataFrame.columns)) == 3:
			print(dataFrame.head())
			if self.yes_no("This might be in row format. Shall I convert it to matrix format for you?"): 
				dataFrame.pivot(index=dataFrame.columns[0], columns=dataFrame.columns[1], values=dataFrame.columns[2])

		# Rename first column to TIMESTAMP and convert first column to pandas datetime with format detection
		dataFrame.rename(columns={dataFrame.columns[0]: "TIMESTAMP"}, inplace = True, errors="raise")
		
		# TODO Find first timestamps

		# print(dataFrame.iloc[:, 0].apply(lambda x: 'date' if type(x)==pd.Timestamp else 'not date').head)

		dataFrame["filterForTime"] = pd.to_datetime(dataFrame[dataFrame.columns[0]],errors='coerce').dropna()
		
		#pd.api.types.is_datetime64_dtype(dataFrame[dataFrame.columns[0]])
		
		#dataFrame.apply(lambda x: x.iloc[0].types.is)

		# print(dataFrame.select_dtypes(include="datetime"))

		print(dataFrame.head())

		# Make TIMESTAMP to DataFram.index
		dataFrame["TIMESTAMP"] =  pd.to_datetime(dataFrame["TIMESTAMP"], infer_datetime_format=True)
		# dataFrame = dataFrame.set_index("TIMESTAMP")

		return dataFrame
