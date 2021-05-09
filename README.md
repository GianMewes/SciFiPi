## CI-Actions
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
In order to use SciFiPi as a CLI tool, first clone this repository or download the code. After obtaining the code, open a shell inside the src folder and execute ```python SciFiPi.py --filters filter1 filter2 filterN ``` with filter1 - filterN being the prefilters and filters you want to apply. Note that they don't have to be in any particular order. You can even mix prefilters and filters, SciFiPi will take care of order.

### Library


## List of Filters
You can use any number of the following filters in any order:
- filterDuplicates (CLI name: "duplicates")
- filterEquidistant (CLI name: "equidistant")
- filterImputation (CLI name: "imputation")
- filterDecimalShift (CLI name: "decimalshift")
- filterNoise (CLI name: "noise")
- filterLag (CLI name: "lag")


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
