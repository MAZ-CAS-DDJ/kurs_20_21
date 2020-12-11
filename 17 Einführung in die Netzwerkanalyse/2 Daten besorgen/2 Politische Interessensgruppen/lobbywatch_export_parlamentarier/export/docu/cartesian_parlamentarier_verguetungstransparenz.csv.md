Lobbywatch Export: CSV
======================

Datei: export/cartesian_parlamentarier_verguetungstransparenz.csv  
Datum: 07.12.2020 02:31:02  
Datensatztyp: cartesian  
Exporttyp: Öffentlich / Public  

Herausgeber: Lobbywatch (https://lobbywatch.ch)  

Die Inhalte von Lobbywatch.ch sind lizenziert unter einer Creative Commons Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz. (https://creativecommons.org/licenses/by-sa/4.0/deed.de)

Data are licensed as CC BY-SA


## parlamentarier_verguetungstransparenz (parlamentarier_transparenz)

Datensatztyp: cartesian

Feld | Beschreibung
- | -
id | Technischer Schlüssel Technischer Schlüssel
parlamentarier_id | Fremdschlüssel des Parlamentariers
stichdatum | Stichdatum der Auswertung der Vergütungstransparenz
in_liste | Ist dieser Eintrag in der Transparenzliste mit dem angegebenen Stichdatum enthalten? (Dieses Feld verhindert Transparenzlisteneinträge löschen zu müssen, wenn diese nicht in der Transparenzliste enthalten sind.)
verguetung_transparent | Ist der dieser Parlamentarier transparent bzgl seinen Vergütungen? ja, nein, teilweise (Leer/NULL bedeutet noch nicht eingetragen): NEIN=Minimaltransparenz (= gesetzliches Minimum, bezahlt/ehrenamtlich); TEILWEISE=teilweise transparent (=gesetzl Minimum plus einzelne Entschädigungen als Betrag offengelegt); JA=transparent (=gesetzl. Minimum plus alles Entschädigungen offengelegt; Exkl. Entschädigung aus Hauptberuf)
freigabe_datum | Freigabedatum (Freigabe = Daten sind fertig)
anzeige_name | Der Anzeigename ist eine Kombination anderer Namensfelder. Dieser Name enthält die relevanten Bestandteile zur Anzeige. In der Regel ist der deutsche Name enthalten.
rat | Kürzel des Rates
kanton | Kantonskürzel
partei_de | Parteiabkürzung
fraktion | Fraktionsabkürzung
kommissionen | Abkürzungen der Kommissionen des Parlamentariers (automatisch erzeugt [in_Kommission Trigger])
im_rat_seit | Jahr der Zugehörigkeit zum Parlament
im_rat_bis | Austrittsdatum aus dem Parlament. Leer (NULL) = aktuell im Rat, nicht leer = historischer Eintrag
geschlecht | Geschlecht des Parlamentariers, M=Mann, F=Frau
geburtstag | Geburtstag des Parlamentariers
parlament_biografie_id | Biographie ID auf Parlament.ch; Dient zur Herstellung eines Links auf die Parlament.ch Seite des Parlamenteriers. Zudem kann die ID für die automatische Verarbeitung gebraucht werden.
parlament_number | Number Feld auf ws.parlament.ch, wird von ws.parlament.ch importiert, wird z.B. als ID für Photos verwendet.
sprache | Sprache des Parlamentariers, wird von ws.parlament.ch importiert
arbeitssprache | Arbeitssprache des Parlamentariers, erhältlich auf parlament.ch

