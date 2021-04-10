import Filter
import pandas as pd

class tsCorrectionFilter(Filter):
    def applyFilter(self, dataFrame: pd.DataFrame):
        print("tyCorrectFilter")
        return dataFrame
