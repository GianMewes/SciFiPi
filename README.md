## CI-Actions
[![Python package](https://github.com/GianMewes/KEEN/actions/workflows/testPython.yaml/badge.svg)](https://github.com/GianMewes/KEEN/actions/workflows/testPython.yaml)

<p align="center">
    <img width="250px" src="https://github.com/GianMewes/KEEN/blob/documentation/images/images/SciFiPi-Logo_left.png">
    <img width="250px" src="https://github.com/GianMewes/KEEN/blob/documentation/images/images/SciFiPi-Logo_right.png"> 
</p>

<h1 align="center">Sci-Fi-Pi<h2>
<h2 align="center">The Scientific Filtering Pipeline to Clean your Machine Learning Datasets<h2>

<hr>





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

