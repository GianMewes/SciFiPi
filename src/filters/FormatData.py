import pandas as pd

from helper.yes_no import yes_no
from filters.Filter import Filter

class FormatDataFrame(Filter):


	df: pd.DataFrame
	names: pd.DataFrame
	units: pd.DataFrame


	def fixRowFormat(self):

		if len((self.df.columns)) == 3:
			# convert to matrix
			# TODO: Klüger machen!
			if yes_no("This might be in row format. Shall I convert it to matrix format for you?"): 
				self.df.pivot(index=self.df.columns[0], columns=self.df.columns[1], values=self.df.columns[2])

		return None


	def dropNonDataRows(self):

		if not pd.api.types.is_datetime64_dtype(self.df.index):
			self.df.rename(columns={self.df.columns[0]: "TIMESTAMP"}, inplace = True, errors="raise")
			try: 
				start = self.df["TIMESTAMP"].where(self.df["TIMESTAMP"].str.contains("time",case=False, na=False)).first_valid_index()+1
				self.names = self.df.iloc[start-2, 1::]
				self.units = self.df.iloc[start-1, 1::]
				for x in range(start): self.df = self.df.drop([x])
			except:
				pass

		return None


	def setTimestampAsIndex(self):

		# Make first column datetime and set as index. Errors are set as NaT
		if not pd.api.types.is_datetime64_dtype(self.df.index):
			self.df["TIMESTAMP"] =  pd.to_datetime(self.df["TIMESTAMP"], infer_datetime_format=True, errors='coerce')
			# TODO: Fill NaT's!
			# IDEE: NaT auffüllen mit letzten Wert + .diff()
			# 		letztes NaT + .diff() == nächster richtiger Zeitstempel zu kontrolle
			# 		Hilfserie erzeugen mit [0] + n* diff und damit auffüllen.
			time = self.df["TIMESTAMP"]
			diff = time.diff().median()
			for x in range(1, time.size):
				time.iloc[x] = time.iloc[x-1] + diff
			# self.df["TIMESTAMP"] = self.df["TIMESTAMP"].fillna(method='pad')
			print(time)
			# self.df.index = self.df.index.fillna()
			self.df = self.df.set_index("TIMESTAMP")

		return None


	def setColumnNames(self):

		# if 'names' in locals():
		self.df.columns = self.names

		return None

	def applyFilter(self, dataFrame:pd.DataFrame):

		self.df = dataFrame
		
		self.fixRowFormat()

		self.dropNonDataRows()

		self.setTimestampAsIndex()

		self.setColumnNames()		

		return self.df
