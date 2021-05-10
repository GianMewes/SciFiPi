import pandas as pd

from cleaners.FormatData import FormatDataFrame

from preFilters.DuplicateFilter import DuplicateFilter
from preFilters.ImputationFilter import ImputationFilter
from preFilters.EquiDistanceFilter import EquiDistanceFilter
from preFilters.FillTimestampsFilter import FillTimestampsFilter
from preFilters.FixTimezoneFilter import FixTimezoneFilter

class PreFilterBuilder:


    dataFrame: pd.DataFrame


    def __init__(self, data=None):
        if isinstance(data, pd.DataFrame):
            self.dataFrame = self.formatData(data)
        elif isinstance(data, list):
            dataFrames = []
            for x in data:
                if isinstance(x, str):
                    self.dataFrame = self.formatData(pd.read_csv("dirty_data/" + x))
                    self.filterFixTimezone()
                    dataFrames.append(self.dataFrame)
                elif isinstance(x, pd.DataFrame):
                    dataFrames.append(self.formatData(x))
                else:
                    print("[PreFilterBuilder]: No Valid Input!")
            self.dataFrame = pd.concat([x for x in dataFrames ], axis=1)
        elif data is None:
            self.dataFrame = pd.DataFrame
        else:
            print("FilterBuilder: No Valid Input!")


    def getDataFrame(self):
        return self.dataFrame


    def formatData(self, df):
        filter = FormatDataFrame()
        dataFrame = filter.applyFilter(df)
        return dataFrame
        

    def filterEquidistance(self):
        filter = EquiDistanceFilter()
        self.dataFrame = filter.applyFilter(self.dataFrame)
        return self
    
    def filterFillTimestamps(self):
        filter = FillTimestampsFilter()
        self.dataFrame = filter.applyFilter(self.dataFrame)
        return self

    def filterFixTimezone(self):
        filter = FixTimezoneFilter()
        self.dataFrame = filter.applyFilter(self.dataFrame)
        return self
    
    def filterDuplicates(self):
        filter = DuplicateFilter()
        self.dataFrame = filter.applyFilter(self.dataFrame)
        return self

    def filterImputation(self):
        filter = ImputationFilter()
        self.dataFrame = filter.applyFilter(self.dataFrame)
        return self
