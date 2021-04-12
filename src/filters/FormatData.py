import pandas as pd

from filters.Filter import Filter

class FormatDataFrame(Filter):

	def applyFilter(self, dataFrame:pd.DataFrame):
		if len((dataFrame.columns)) == 3:
			print(dataFrame.head())
			if self.yes_no("This might be in row format. Shall I convert it to matrix format for you?"): 
				dataFrame.pivot(index=dataFrame.columns[0], columns=dataFrame.columns[1], values=dataFrame.columns[2])

		# Rename first column to TIMESTAMP and convert first column to pandas datetime with format detection
		dataFrame.rename(columns={dataFrame.columns[0]: "TIMESTAMP"}, inplace = True, errors="raise")
		dataFrame["TIMESTAMP"] =  pd.to_datetime(dataFrame["TIMESTAMP"], infer_datetime_format=True)

		# Make TIMESTAMP to DataFram.index
		dataFrame = dataFrame.set_index("TIMESTAMP")

		return dataFrame

	def yes_no(self, answer):
			yes = set(['y'])
			no = set(['n'])
			
			while True:
				choice = input(answer).lower()
				if choice in yes:
					return True
				elif choice in no:
					return False
				else:
					print("Please respond with 'y' or 'n' ")
