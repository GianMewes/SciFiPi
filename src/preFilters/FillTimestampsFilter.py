import pandas as pd

from filters.Filter import Filter


class FillTimestampsFilter(Filter):

     def applyFilter(self, df: pd.DataFrame):
        
        if df.index.isna().any():
            tempIndex = df.index.to_series()
            time = df.index.to_series().copy()
            diff = time.diff().median()
            for x in range(1, time.size):
                time.iloc[x] = time.iloc[x-1] + diff

            tempIndex.fillna(value=time, inplace=True)
        else:
            print("There are no NaT's to fill!")

        return df