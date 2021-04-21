import pandas as pd
import fastdtw
import dtw

from filters.Filter import Filter

class Lag(Filter):
    def applyFilter(self, dataFrame:pd.DataFrame):
		# notes:
		# lag is defined as a time series x, which represents the time series y shifted by the lag z (expressed in time)
		# lagged time series can also be related time series (one is input, the other is output) --> extremely difficult to differentiate without knowledge
		# calculate lagged correlation (contrary to "classical" correlation) has the advantage of detecting lagged variables
		# different approaches for time lag correlation https://towardsdatascience.com/four-ways-to-quantify-synchrony-between-time-series-data-b99136c4a9c9
		# ideas: Pearson, Dynamic Time Warping, Partial Autocorrelation
		# to find all lagged variables, ones need to iterate through all variables and all timeshifts and compare them...
		# another approach is to find the maximum cross-correlation coefficient https://stackoverflow.com/questions/41492882/find-time-shift-of-two-signals-using-cross-correlation/56432463
		# see also: https://stats.stackexchange.com/questions/482927/estimate-the-delay-between-two-signals
		# but before using the Lag Filter, one should remove noise

		# calculate cross-correlation between columns
		for i in len(dataFrame.columns)-2:
			j = i+1
			for j in len(dataFrame.columns)-1:


		# find lagged variables
		# where cross-correlation curve = autocorrelation curve? or where ac = ac?

		# use dynamic time warping to align lagged variables
		# tutorial: https://htmlpreview.github.io/?https://github.com/statefb/dtwalign/blob/master/example/example.html
		for columnPair in columnPairs:
			aligned_column = dtw(columnPair[0], columnPair[1])
