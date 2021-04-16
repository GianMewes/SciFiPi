import pandas as pd
import numpy as np

from helper.yes_no import yes_no
from filters.Filter import Filter

class FormatDataFrame(Filter):

	def applyFilter(self, dataFrame:pd.DataFrame):
		
		if len((dataFrame.columns)) == 3:
			# convert to matrix
			# TODO: Klüger machen!
			if yes_no("This might be in row format. Shall I convert it to matrix format for you?"): 
				dataFrame.pivot(index=dataFrame.columns[0], columns=dataFrame.columns[1], values=dataFrame.columns[2])

		if not pd.api.types.is_datetime64_dtype(dataFrame.index):
			dataFrame.rename(columns={dataFrame.columns[0]: "TIMESTAMP"}, inplace = True, errors="raise")
			start = dataFrame["TIMESTAMP"].where(dataFrame["TIMESTAMP"].str.contains("time",case=False, na=False)).first_valid_index()+1
			print(dataFrame.head())
			dataFrame.columns = dataFrame.iloc[start-1]
			# Rename first column to TIMESTAMP and convert first column to pandas datetime with format detection
			print(dataFrame.head())
			dataFrame.reset_index(drop=True, inplace=True)
			print(dataFrame.head())
			dataFrame = dataFrame.drop(labels=range(0, start), axis=0)
			print(dataFrame.head())

		

		# Make first column datetime and set as index
		if not pd.api.types.is_datetime64_dtype(dataFrame.index):
			dataFrame["TIMESTAMP"] =  pd.to_datetime(dataFrame["TIMESTAMP"], infer_datetime_format=True)
			dataFrame = dataFrame.set_index("TIMESTAMP")
		# TODO Find first timestamps

		# print(dataFrame.iloc[:, 0].apply(lambda x: 'date' if type(x)==pd.Timestamp else 'not date').head)
		# dataFrame["filterForTime"] = pd.to_datetime(dataFrame[dataFrame.columns[0]],errors='coerce').dropna()	

		# TO DO: find in firts colum "time" 

		# pd.api.types.is_datetime64_dtype(dataFrame[dataFrame.columns[0]])		
		# dataFrame.apply(lambda x: x.iloc[0].types.is)
		# print(dataFrame.select_dtypes(include="datetime"))

		

		return dataFrame
