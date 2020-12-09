Lobbywatch Export: CSV
======================

Datei: export/cartesian_minimal_parlamentarier_interessenbindung.csv  
Datum: 07.12.2020 02:31:02  
Datensatztyp: cartesian  
Exporttyp: Öffentlich / Public  

Herausgeber: Lobbywatch (https://lobbywatch.ch)  

Die Inhalte von Lobbywatch.ch sind lizenziert unter einer Creative Commons Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz. (https://creativecommons.org/licenses/by-sa/4.0/deed.de)

Data are licensed as CC BY-SA


## minimal_parlamentarier_interessenbindung (parlamentarier)

Datensatztyp: cartesian

Feld | Beschreibung
- | -
anzeige_name | Der Anzeigename ist eine Kombination anderer Namensfelder. Dieser Name enthält die relevanten Bestandteile zur Anzeige. In der Regel ist der deutsche Name enthalten.
id | Technischer Schlüssel des Parlamentariers Technischer Schlüssel
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
beschreibung | Bezeichung der Interessenbindung. Möglichst kurz. Wird nicht ausgewertet, jedoch angezeigt.
von | Beginn der Interessenbindung, leer (NULL) = unbekannt
bis | Ende der Interessenbindung, leer (NULL) = aktuell gültig, nicht leer = historischer Eintrag
art | Art der Interessenbindung
funktion_im_gremium | Funktion innerhalb des Gremiums, z.B. Präsident in einem Vorstand einer AG entspricht einem Verwaltungsratspräsidenten, Präsident einer Geschäftsleitung entspricht einem CEO.
deklarationstyp | Ist diese Interessenbindung deklarationspflichtig? Bezeichung der Interessenbindung. Möglichst kurz. Wird nicht ausgewertet, jedoch angezeigt.
status | Status der Interessenbindung
hauptberuflich | Eigene Firma/Haupttätigkeit: Ist diese Interessenbindung hauptberuflich? (Hauptberufliche Interessenbindungen müssen nicht offengelegt werden.)
behoerden_vertreter | Entstand diese Interessenbindung als Behördenvertreter von Amtes wegen? Beispielsweise weil ein Regierungsrat in einem Verwaltungsrat von Amtes wegen Einsitz nimmt.
wirksamkeit | 'tief', 'mittel', 'hoch': Wirksamkeit der Interessenbindung, siehe https://lobbywatch.ch/de/seite/wirksamkeit. Die Wirksamkeit ist eines der primären Resultate von Lobbywach.
organisation_id | Fremdschlüssel Organisation
verguetung | Jährliche Vergütung CHF für Tätigkeiten aus dieser Interessenbindung, z.B. Entschädigung für Beiratsfunktion.
verguetung_jahr | Jahr auf welche sich die Werte beziehen
verguetung_beschreibung | Beschreibung der Vergütung. Möglichst kurz. Wird nicht ausgewertet, jedoch angezeigt.
name_de | Name der Organisation. Sollte nur juristischem Namen entsprechen, ohne Zusätze, wie Adresse. Deutscher Name des Datensatzes.
ort | Ort der Organisation
rechtsform | Rechtsform der Organisation
typ | Typ der Organisation. Beziehungen können über Organisation_Beziehung eingegeben werden.
vernehmlassung | Häufigkeit der Teilname an nationalen Vernehmlassungen
interessengruppe1 | Zuteilung der Organisation zur Lobbygruppe (Hauptlobbygruppe der Organisation), deutsch
interessengruppe1_branche | Zugehörigkeit zur Branche aufgrund der Hauptlobbygruppe (interessengruppe1) der Organisation, deutsch
interessengruppe1_branche_kommission_abkuerzung | Deutsches Kürzel der zugeordneten Kommission aufgrund der Branche der Organisation

