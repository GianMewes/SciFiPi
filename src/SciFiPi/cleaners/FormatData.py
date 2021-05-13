import pandas as pd

from ..filters.Filter import Filter


class FormatDataFrame(Filter):

    df: pd.DataFrame
    names = pd.DataFrame()
    units: pd.DataFrame

    def fixRowFormat(self):
        
        if len((self.df.columns)) == 2:
            tempDF = self.df
            try:
                tempDF.pivot(columns=tempDF.columns[0], values=tempDF.columns[1])
                tempDF.rename(
                columns={tempDF.columns[0]: "TIMESTAMP"}, inplace=True, errors="raise")
                self.df = tempDF
                return True
            except:
                print("[formatData-Filter]: Transformation to matrix format failed!")
                return False
        else:
            print("[formatData-Filter]: Did not convert to matrix format!")
            return False

    def dropNonDataRows(self):
        
        tempDF = self.df
        if not pd.api.types.is_datetime64_dtype(tempDF.index):
            tempDF.rename(
                columns={tempDF.columns[0]: "TIMESTAMP"}, inplace=True, errors="raise")
            try:
                start = tempDF["TIMESTAMP"].where(tempDF["TIMESTAMP"].str.contains(
                    "time", case=False, na=False)).first_valid_index()+1
                self.names = tempDF.iloc[start-2, 1::]
                self.units = tempDF.iloc[start-1, 1::]
                for x in range(start):
                    tempDF = tempDF.drop([x])
                self.df = tempDF
                return True
            except:
                return False
        else:
            print("[formatData-Filter]: Timestamp is already in datetime format!")
            return False

    def setTimestampAsIndex(self):

        # Make first column datetime and set as index. Errors are set as NaT
        tempDF = self.df
        try: 
            if not pd.api.types.is_datetime64_dtype(tempDF.index):
                tempDF["TIMESTAMP"] = pd.to_datetime(tempDF["TIMESTAMP"], infer_datetime_format=True, errors='coerce')
                tempDF = tempDF.set_index("TIMESTAMP")
                self.df = tempDF
                return True
            else:
                print("[formatData-Filter]: Timestamp is already in datetime format!")
                return False
        except:
            return False

    def setColumnNames(self):
        try:
            if not self.names.size == 0:
                self.df.rename(self.names, axis='columns', inplace=True)
                return True
            else:
                print("[formatData-Filter]: No names to set as column names found!")
                return False
        except:
            return False


    def cleanTypes(self):

        try: 
            tempDF = self.df
            tempDF.apply(pd.to_numeric, errors='coerce')
            self.df = tempDF
            return True
        except:
            return False

    def applyFilter(self, dataFrame: pd.DataFrame):
        
        self.df = dataFrame
        
        if self.fixRowFormat():
            print("[formatData-Filter]: Fixed Row Format")
        else:
            if self.dropNonDataRows():
                print("[formatData-Filter]: Dropped Non Data Rows")
            else:
                print("[formatData-Filter]: Dropping name columns failed!")

            if self.setColumnNames():
                print("[formatData-Filter]: Set Columnames")
            else:
                print("[formatData-Filter]: Setting column names failed!")

        if self.setTimestampAsIndex():
            print("[formatData-Filter]: Set Timestamp as Index")
        else:
            print("[formatData-Filter]: Setting timestamp as index failed!")

        if self.cleanTypes():
            print("[cleanTypes-Filter]: Casted the dataFrame to numeric")
        else:
            print("[formatData-Filter]: Casting the dataFrame to numeric failed!")

        return self.df
