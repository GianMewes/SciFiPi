[![Python package](https://github.com/GianMewes/KEEN/actions/workflows/testPython.yaml/badge.svg)](https://github.com/GianMewes/KEEN/actions/workflows/testPython.yaml)

<p align="center">
    <img width="250px" src="https://github.com/GianMewes/KEEN/blob/documentation/images/images/SciFiPi-Logo_left.png">
    <img width="250px" src="https://github.com/GianMewes/KEEN/blob/documentation/images/images/SciFiPi-Logo_right.png"> 
</p>

<h1 align="center">Sci-Fi-Pi<h2>
<h2 align="center">The Scientific Filtering Pipeline to Clean your Machine Learning Datasets<h2>

<hr>


## Usage
SciFiPi can be used either as a standalone tool with a command line interface (CLI) or as a library which you can include into your own code. These two options are described below

### CLI
In order to use SciFiPi as a CLI tool, first clone this repository or download the code. After obtaining the code, open a shell inside the src folder and execute ```python SciFiPi.py --filters filter1 | filter2 | filterN ``` with filter1 - filterN being the prefilters and filters you want to apply. Note that they don't have to be in any particular order. You can even mix prefilters and filters, SciFiPi will take care of order. Filters are separated by pipe characters. If any arguments are passed to the lag or noise filter, they are passed in parentheses, e.g. lag([[1, 2],[4, 5]]) to remove lag in columns 1/2 and 3/4 or noise([2]) to filter noise from the second column.

### Library


### List of Cleaners
These filters are run by default:
- FormatData ("Cleaner" - run by default): This isn't actually a filter as the others. FormatData is called in the constructor of the PreFilterBuilder to format the read data into a standardized format for the following actual filters. Therefor multiple files are merged, all files are transformed to matrix format, non-data-rows as die signal names and units are dropped and later set als column names. Furthermore the timestamp is set as index and all cells are transferred to numeric.


### List of PreFilters

- filterDuplicates (CLI name: "duplicates"): The DuplicatesFilter checks every possible column pair for exact matches (easy method). Alternativley a more advanced method can be used, where the similarity of the column pairs is calculated using the cosine similarity and euclidean distance from the sklearn and scipy libraries. The combination check of both similarity measures results in exact, linear transformed and partial duplicates.
- filterEquidistance (CLI name: "equidistance"): The EquidistanceFilter finds the most frequent distance value in the index column by using the mode. Afterwards the index is recreated by using the resample() method from the pandas library and setting the offset to the most frequent distance value.
- filterImputation (CLI name: "imputation"): Adds missing values. On small dataframes (less than three columns) missing values are replaced via backfilling. on larger dataframes, missing values are added via a decision tree with backfilling as a fallback strategy.
- filterFillTimestamps (CLI name: "fillTimestamps"): The fillTimestamps-Filter is scanning the dataFrames index for NaTs. If NaTs are found, a synthetic timestamp is created by the start time and the difference between the timestamps. The index is then filled by this synthetic timestamp.
- filterFixTimezone (CLI name: "fixtimezone"): The FixTimezoneFilter is searching for timezone information in the dataframes index. If a timezone information is found it is transferred into datetime-format. If no timezone information is given, the local timezone is set. By adding timezone information into the index of dataframes, the signals of individual dataframes are mapped by the time recorded.

### List of Filters
You can use any number of the following filters in any order:
- filterDecimalShift (CLI name: "decimalshift"): Checks for sudden jumps in the data caused by decimal place errors. Identified errors are then multiplied/devided by 10.
- filterNoise (CLI name: "noise"): The NoiseFilter uses a k-Nearest-Neighbours regressor (from the sklearn library) to self-predict the column and remove noise.
- filterLag (CLI name: "lag"): The LagFilter uses Dynamic Time Warping (DTW - from the dtwalign library) to dynamically align two lagged columns and recreate them in their respective dataframe columns.


## Architecture
### Idea & Existing Filters
The idea of SciFiPi is to provide a flexible data cleaning & filtering pipeline that covers a variety of use cases. You can apply a variety of filters in any arbitrary order and if that's not enough, SciFiPi provides an extension mechanism that allows to extend the library with custom filter functions.

The main principle of our architecture is a design pattern which is widely used in Object Oriented Programming, a [fluent interface](https://en.wikipedia.org/wiki/Fluent_interface). This interface allows arbitrary chaining of filters without users having to worry about the order of method calls. All filtering functions described below are provided by so-called *FilterBuilders* which implement the fluent interface pattern.

The existing filters of SciFiPi can be separated into three categories:
<img width="100%" src="https://github.com/GianMewes/KEEN/blob/documentation/images/images/SciFiPi_Architecture.png">

- **Cleaners & Preparators:** We refer to the first category of filters as *Cleaners* or *Preparators* because they take care of the initial preparation (i.e. loading and cleaning) of the dataset. This category contains functions to read single files or multiple files from a folder. Furthermore, this functions of this first category take care of correct indexing (i.e. by timestamp) and make sure that a datasets contents are all typed "numeric". If a dataset entry cannot be cast to numeric, it will be marked as "NaN" here. In this step, no advanced filling techniques are applied.
- **PreFilters:** The second category, so-called *PreFilters* contain functions for simple filtering operations. Filters in this category take care of duplicated columns, make sure a dataset is equidistant and fill "NaN"s from the previous step.
- **Filters:** The third category contains some more advanced filtering functions such as filters for noise, lag as well as value shifts caused by unit shifts.

### Extend SciFiPi
We just started SciFiPi as a submission to the [KEEN Hackathon](https://www.achema.de/en/the-achema/innovation-challenge/keen-challenge) and implemented a basic set of filters. We know that this is just a first step and might not be sufficient for some of you out there. In this case, you can simply extend SciFiPi by writing your own *PreFilters* or *Filters*.
In order to do so, you have to follow these two steps:
1. Write your custom filter class. You should stick to the naming convention: The name of your class should be (FilterFunction) + Filter.
2. Register it inside the *PreFilterBuilder* (for custom PreFilters) or inside the *FilterBuilder* (for custom Filters). 

The following snippet shows step 1, writing your custom filter:
```python
from filters.Filter import Filter

# Create your own filter class and extend the base filter
class CustomFilter(Filter):

	# Override the "applyFilter" function
    def applyFilter(self, dataFrame:pd.DataFrame):
        
		# Do with the dataFrame whatever you want, but make sure to return the changed dataFrame it in the end

        return dataFrame
```

As you can see, it's pretty straightforward. Extend the base ```Filter``` class and override the applyFilter method. 
<br>
The second step, registering your filter is shown in the next code snippet:
```python
class FilterBuilder:

# Existing filters ... 

	def filterCustom(self):
			filter = CustomFilter()
			self.dataFrame = filter.applyFilter(self.dataFrame)
			return self
```

This is also rather straightforward. Define a function for your filter. In order for our CLI to work, it has to follow the naming scheme "filter" + (FilterFunction). Inside of the new functions, create an instance of your filter and invoke the ```applyFilter() ``` function before returning self. This last line us required to not break the fluent interface.


### Current Limitations
Due to limited time, some limitations still exist. 
1. The equidistance filter has a large runtime due to high computational complexity.
2. The DecimalShiftFilter is occasionally to sensitive to changes. Sometimes decimal shifts are detected where there are none. If sensitivity is artificially lowered, some true decimal shifts are not detected any more.
3. LagFilter requires specifications on which columns are possible linked by a time lag.
4. NoiseFilter needs instruction on which columns should be freed from noise. This is due to individual characteristics of columns - what constitutes noise in one sensor, might be valid data for other sensors.
