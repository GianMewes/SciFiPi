import datetime
import pandas as pd

from tzlocal import get_localzone

from ..filters.Filter import Filter

class FixTimezoneFilter(Filter):

    def applyFilter(self, dataFrame:pd.DataFrame):
        # Check and set timezone information
        # print(dataFrame.head())
        if str(dataFrame.index.tzinfo) == "None":
            print("[FixTimezone-Filter]: No timezone information found. Setting local timezone: " + get_localzone().zone)
            dataFrame = dataFrame.tz_localize(tz = get_localzone())
        else:
            dataFrame = dataFrame.tz_convert(tz = get_localzone())       
        
        return dataFrame

