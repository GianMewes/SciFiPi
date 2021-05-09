import pandas as pd
import unittest
import context

from src.FilterBuilder import FilterBuilder

class FixTimezoneTest(unittest.TestCase):

    def __init__(self):

        self.df = pd.read_csv(r"/testfiles/FixTimezone_test/dirty_data.csv")

    def testCalculation(self):

        filterBuilder = FilterBuilder(self.df)
        self.assertEqual(filterBuilder.fixTimezone(), filterBuilder.fixTimezone())
        

if __name__ == '__main__':

    unittest.main()

    
