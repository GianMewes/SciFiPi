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
			try: 
				start = dataFrame["TIMESTAMP"].where(dataFrame["TIMESTAMP"].str.contains("time",case=False, na=False)).first_valid_index()+1
				names = dataFrame.iloc[start-2, 1::]
				units = dataFrame.iloc[start-1, 1::]
				for x in range(start): dataFrame = dataFrame.drop([x])
			except:
				pass

		# Make first column datetime and set as index. Errors are set as NaT
		if not pd.api.types.is_datetime64_dtype(dataFrame.index):
			dataFrame["TIMESTAMP"] =  pd.to_datetime(dataFrame["TIMESTAMP"], infer_datetime_format=True, errors='coerce')
			# TODO: Fill NaT's!
			# IDEE: NaT auffüllen mit letzten Wert + .diff()
			# 		letztes NaT + .diff() == nächster richtiger Zeitstempel zu kontrolle
			# 		Hilfserie erzeugen mit [0] + n* diff und damit auffüllen.
			time = dataFrame["TIMESTAMP"]
			diff = time.diff().median()
			for x in range(1, time.size):
				time.iloc[x] = time.iloc[x-1] + diff
			# dataFrame["TIMESTAMP"] = dataFrame["TIMESTAMP"].fillna(method='pad')
			print(time)
			# dataFrame.index = dataFrame.index.fillna()
			dataFrame = dataFrame.set_index("TIMESTAMP")



		if 'names' in locals():
			dataFrame.columns = names

		return dataFrame
