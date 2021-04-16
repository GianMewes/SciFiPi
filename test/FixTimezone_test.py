import pandas as pd
import unittest

from FilterBuilder import FilterBuilder

class FixTimezoneTest(unittest.TestCase):

    def testCalculation(self):
        self.assertEqual(fib(0), 0)

if __name__ == '__main__':

    unittest.main()


expected_res=pd.Series([7,9,11,13,15])
pd.testing.assert_series_equal((df1['a']+df2['a']),expected_res,check_names=False)