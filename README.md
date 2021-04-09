# KEEN


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

