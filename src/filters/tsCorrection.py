from filters.Filter import Filter
from datetime import datetime
import pandas as pd
import locale as loc

class tsCorrectionStats:
    length = -1
    successfull = 0
    failed = 0
    failedRanges = []

    failedBegin = -1
    lastIndex = 0

    def __init__(self, length):
        self.length = length

    def success(self, index):
        self.lastIndex = index
        self.successfull = self.successfull + 1
        if self.failedBegin != -1:
            self.failedRanges.append((self.failedBegin, self.lastIndex, self.lastIndex - self.failedBegin))
            self.failedBegin = -1

    def fail(self, index):
        self.lastIndex = index
        self.failed = self.failed + 1
        if self.failedBegin == -1:
            self.failedBegin = index

    def printStats(self):
        print("Timestamp Conversation Statistics")
        print("Lengh: " + str(self.length))
        print("Success: " + str(self.successfull))
        print("Fail: " + str(self.failed))
        print("FailedRanges: ")
        print(self.failedRanges)

class tsCorrectionFilter(Filter):

    formatList = {
        '%H:%M:%S':'de_DE',
        '%I:%M:%S %p':'en_US'
    }

    stats = None

    def applyFilter(self, dataFrame: pd.DataFrame):
        df_long = pd.read_csv("./data/real/00-complete/dirty_data.csv")
        df = df_long.drop([0, 1])

        self.stats = tsCorrectionStats(len(df))

        for index in range(0, len(df)):
            retVal = False
            for key in self.formatList:
                retVal = self.tryConvert(df, index, key, self.formatList[key])
                if retVal:
                    self.stats.success(index)
                    break
            if not retVal:
                self.stats.fail(index)
                print("i:" + str(index) + " WTF: " + str(df.iat[index, 0]))
                continue

        print(df.index)
        self.stats.printStats()
        return dataFrame

    def tryConvert(self, df, index, format, locale):
        try:
            loc.setlocale(loc.LC_ALL, locale)
            df.iat[index, 0] = datetime.strptime(str(df.iat[index, 0]), format).strftime("%H:%M:%S")
            return True
        except:
            return False
