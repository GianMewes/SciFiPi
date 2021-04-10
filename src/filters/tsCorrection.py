from filters.Filter import Filter
from datetime import datetime
import pandas as pd
import locale as loc

class tsCorrectionFilter(Filter):

    formatList = {
        '%H:%M:%S':'de_DE',
        '%I:%M:%S %p':'en_US'
    }

    def applyFilter(self, dataFrame: pd.DataFrame):
        df_long = pd.read_csv("./data/real/00-complete/dirty_data.csv")
        df = df_long.drop([0, 1])

        for index in range(0, len(df)):
            retVal = False
            for key in self.formatList:
                retVal = self.tryConvert(df, index, key, self.formatList[key])
                if retVal:
                    # print("i:" + str(index) + " OK: " + str(df.iat[index, 0]))
                    break
            if not retVal:
                print("i:" + str(index) + " WTF: " + str(df.iat[index, 0]))
                continue

        print(df.index)
        return dataFrame

    def tryConvert(self, df, index, format, locale):
        try:
            loc.setlocale(loc.LC_ALL, locale)
            df.iat[index, 0] = datetime.strptime(str(df.iat[index, 0]), format).strftime("%H:%M:%S")
            return True
        except:
            return False
