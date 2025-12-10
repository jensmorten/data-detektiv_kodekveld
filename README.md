# Velkommen til data-detektiv_kodekveld!
Vi bruker denne kvelden på å legge vekt på det ekte data-detektiver alltid gjør først: undersøke åstedet, forstå sporene og finne ut hva dataene faktisk prøver å fortelle oss. Først når vi har god kunnskap om datasettet går vi videre til konkurranse-delen. 

🔍 Datadetektivens oppgaver: <br> <br>
Analyser dette oppdikta datasettet med lønnsstatistikk:  https://raw.githubusercontent.com/jensmorten/data-detektiv_kodekveld/refs/heads/main/data/data2.csv
<br> <br>
Oppgavene kan løses i Excel, Python eller hvilket som helst verktøy du er komfortabel med. 
<br> <br>
1. Beskrivende statistikk:  
Beregn gjennomsnitt, median og standardavvik for "alder", "lonn", "utdanning", "ansiennitet", "sko_str","prestasjonsscore", og lag histogrammer. Finnes det noen mistenkelige verdier?

2. Jakten på korrelasjoner:  
Finn de tre sterkeste korrelasjonene mellom lønn og numeriske variabler. Hvilke kan være nyttige for prediksjon?  
pass på! https://www.tylervigen.com/spurious-correlations

3. Andre variabler:
Hva slags datatyper er er_leder og favorittfarge? Hvordan vil du inkludere disse i analysen? 

4. Simpsons paradoks:  
Finn sammenhengen mellom lønn og ansiennitet per avdeling. Er Simpsons paradoks gjeldende? 

🥇 Konkurrase-del <br>
5. Bygg en enkel regresjon:  
Bygg en lineær regresjonsmodell som predikerer lønn. Hvilke forklaringsvariabler velger du? Fjerner du noen datapunkt?

Bruk modellen til å lage prediksjoner på test-datasett (som ikke inneholder lønn): https://github.com/jensmorten/data-detektiv_kodekveld/blob/main/data/test_set.csv

Lever inn din .csv-fil med prediksjoner. 
Bruk gjerne notebooken compete.ipynb (https://github.com/jensmorten/data-detektiv_kodekveld/blob/main/notebooks/Compete.ipynb) for å se et eksempel du kan bygges videre på.

Se predictions.csv (https://github.com/jensmorten/data-detektiv_kodekveld/blob/main/compeval/predictions.csv) for å undersøke formatet som må leveres. To kolonner "id" og "lonn", komma-separarert. "." er desimalskilletegn

Følg med på https://datadetektivkodekveld.streamlit.app/ for vinnaren. 🏇

6. (ekstra)
Bygg en avansert modell som predikerer lønn. 

---- 
Event: https://event.bouvet.no/event/e020398f-d768-445e-8933-7e874211aa28
----
# Oppsett av python på windows (valgfritt):
Download WinPython and extract the files to a folder of your choice. https://winpython.github.io/
Open the extracted folder and run WinPython Command Prompt.exe.
Navigate to your GitHub folder with the exercise by typing cd C:\[....]\GitHub\data-detektiv_kodekveld\notebooks\.
Type "jupyter notebook" to start Jupyter Notebooks. Select notebook "Compete" in the browser window that opens.
