import pandas as pd

from filters.Filter import Filter

class FixTimezone(Filter):

    def applyFilter(self, dataFrame:pd.DataFrame):
        # Check and set timezone information
        # print(dataFrame.head())
        if str(dataFrame.index.tzinfo) == "None":
            dataFrame = dataFrame.tz_localize(tz = "UTC")
        else:
            dataFrame = dataFrame.tz_convert(tz = "UTC")       
            # print(dataFrame.head()) 
        
        # TODO : Was ist wenn der DataFrame in einer anderen Zeitzone aufgenommen wurde, aber keine tzinfo enhaelt?
        # Wenn zwei gleiche Datensätze, dann nimm den mit Zeitzonen-Information

        return dataFrame

