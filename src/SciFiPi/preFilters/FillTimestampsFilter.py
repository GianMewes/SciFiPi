import pandas as pd

from ..filters.Filter import Filter


class FillTimestampsFilter(Filter):

     def applyFilter(self, dataFrame: pd.DataFrame):
        
        if dataFrame.index.isna().any():
            tempIndex = dataFrame.index.to_series()
            time = dataFrame.index.to_series().copy()
            diff = time.diff().median()
            for x in range(1, time.size):
                time.iloc[x] = time.iloc[x-1] + diff

            tempIndex.fillna(value=time, inplace=True)
        else:
            print("[fillTimestamps-Filter]: There are no NaT's to fill!")

        return dataFrame
