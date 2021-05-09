import pandas as pd
import sys
import os
import collections
import math

from FilterBuilder import FilterBuilder
from filters.FormatData import FormatDataFrame

class Starter():

    filters = []
    files = []
    dataFrames = []
    df: pd.DataFrame

    def __init__(self):

        self.filters = sys.argv[1:]
        self.getFilesInFolder()

        for x in self.files:
            self.formatData(pd.read_csv("dirty_data/" + str(x)))

        filterBuilder = FilterBuilder(pd.concat([x for x in self.dataFrames ], axis=1))

        for x in self.filters:
            if x == "formatData": filterBuilder.formatData()
            elif x == "World": print("Hello World!")
            else: print("Error!")

    def getFilesInFolder(self):

        # get files in input directory and remove all not .csv files from list
        self.files = [x for x in os.listdir("dirty_data/") if '.csv' in x]

        # If there are multiple files
        if len(self.files) > 1:

            print("I found these self.files: " + str(self.files))

            # Identify common prefix in filenames and ask if it's right
            prefix = os.path.commonprefix(self.files)
            if not yes_no("\nIdentified following file prefix: '" +
                          prefix + "'   Continue? (y/n) "):
                exit()

            # Generate synthetic files names with series and compare to filenames. If synthetic names == real names, ok. Else: Ciao! & exit()
            synFiles = [(str(prefix) + str(i+1).zfill(math.floor(math.log(len(self.files)))) + ".csv")
                        for i in range(len(self.files))]
            if not collections.Counter(self.files) == collections.Counter(synFiles):
                print("\nPrefix wasn't right. Ciao!") & exit()

        return True


    def formatData(self, df):
        filter = FormatDataFrame()
        self.dataFrames.append(filter.applyFilter(df))
        return True


if __name__ == '__main__':

    Starter()


def yes_no(answer):
    yes = set(['y'])
    no = set(['n'])

    while True:
        choice = input(answer).lower()
        if choice in yes:
            return True
        elif choice in no:
            return False
        else:
            print("Please respond with 'y' or 'n' ")
