from filters.Filter import Filter
from datetime import datetime
import pandas as pd

class tsCorrectionFilter(Filter):
    #def applyFilter(self, dataFrame:pd.DataFrame):
    def applyFilter(self, dataFrame:pd.DataFrame):
        df_long = pd.read_csv("D:/09_Hacky Hours/KEEN/data/real/00-complete/dirty_data.csv")
        df = df_long.drop([0,1])

        for ts in df.index:
            try:
                print(datetime.strptime(str(df.iloc[ts,0]), "%H:%M:%S"))
            except:
                try:
                    print(datetime.strptime(str(df.iloc[ts,0]), "%-I:%M:%S %p"))
                except:
                    print("Wrong time format: " + str(df.iloc[ts,0]))

            #print(df.iloc[ts,0])
            

        return dataFrame