## CI-Actions
[![Python package](https://github.com/GianMewes/KEEN/actions/workflows/testPython.yaml/badge.svg)](https://github.com/GianMewes/KEEN/actions/workflows/testPython.yaml)


<p align="center">
    <img width="200px" src="images/SciFiPi-Logo_left.png">
	<span align="center" style="font-size:64px; font-weight:bold; margin:2em;">Sci-Fi-Pi</span>
	<img width="200px" src="images/SciFiPi-Logo_right.png">
</p>

<h2 align="center">The Scientific Filter Pipeline to Clean your Machine Learning Datasets<h2>


<hr>


Dateien mit gleichem Namen haben gleichen Inhalt


## Erkenntnisse zu den Datenset

Beispieldaten sind künstlich erzeugt und beinhalten immer nur "ein" Problem.

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

