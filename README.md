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
In order to use SciFiPi as a CLI tool, open a shell inside the src folder and execute ```python .\src\SciFiPi --filters filter1 filter2 filterN ``` with filter1 - filterN being the prefilters and filters you want to apply. Note that they don't have to be in any particular order. You can even mix prefilters and filters, SciFiPi will take care of order.


### Library




## Architecture
### Idea
### Extend SciFiPi
### Current Limitations


## Erkenntnisse zu den Datenset
- Dateien mit gleichem Namen haben gleichen Inhalt
- Beispieldaten sind künstlich erzeugt und beinhalten immer nur "ein" Problem.

Folgende 

- Physical Units (K <> C°)
- Formats (liste statt matrix)
- Lagging (Leicht versetzte Werte)
- base, [TS,Value] mit lücken (null or empty)
- flag, [TS,Value,QualityFlag] (wert mit einem Error flag in der dritten spalte)
- replacement [TS, Value] (Value hat Ersatzwert (UINT max))
- Rauschen
- Zeitzonen test



## Teamaufteilung

Gian / Artan : Lag
Michelle / Andreas : NA
Tom / Aljosha : Noise, Classification, 





## Abstract Architecture

![AbstractArchitecture](Pipeline_Abstract.png)

