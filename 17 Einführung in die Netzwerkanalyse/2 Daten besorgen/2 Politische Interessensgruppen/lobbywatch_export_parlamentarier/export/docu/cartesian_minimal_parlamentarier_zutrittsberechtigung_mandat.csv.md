Lobbywatch Export: CSV
======================

Datei: export/cartesian_minimal_parlamentarier_zutrittsberechtigung_mandat.csv  
Datum: 07.12.2020 02:31:02  
Datensatztyp: cartesian  
Exporttyp: Öffentlich / Public  

Herausgeber: Lobbywatch (https://lobbywatch.ch)  

Die Inhalte von Lobbywatch.ch sind lizenziert unter einer Creative Commons Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz. (https://creativecommons.org/licenses/by-sa/4.0/deed.de)

Data are licensed as CC BY-SA


## minimal_parlamentarier_zutrittsberechtigung_mandat (parlamentarier)

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
id | Technischer Schlüssel der Zutrittsberechtigung Technischer Schlüssel
funktion | Funktion der zutrittsberechtigen Person.
funktion_fr | Funktion der zutrittsberechtigen Person auf französisch.
von | Beginn der Zutrittsberechtigung, leer (NULL) = unbekannt
bis | Ende der Zutrittsberechtigung, leer (NULL) = aktuell gültig, nicht leer = historischer Eintrag
id | Technischer Schlüssel der Zugangsberechtigung Technischer Schlüssel
nachname | Nachname des berechtigten Persion
vorname | Vorname der berechtigten Person
zweiter_vorname | Zweiter Vorname der zutrittsberechtigten Person
namensunterscheidung | Namenszusatz zur Unterscheiden von Personen mit exakt gleichem Namen. Ein Unterscheidungsmerkmal der Person z.B. der Beruf, sollte im Feld gespeichert werden. NUR BEI PERSONEN MIT EXAKT GLEICHEM VORNAMEN UND NAMEN VERWENDEN.
beschreibung_de | Beschreibung der Person. Der Text ist öffentlich einsehbar.
beschreibung_fr | Französische Beschreibung der Person. Der Text ist öffentlich einsehbar.
beruf | Beruf der Person
beruf_fr | Französische Bezeichung des Beruf der Person
beruf_interessengruppe_id | Fremdschlüssel zur Interessengruppe für den Beruf
partei_id | Fremdschlüssel Partei. Parteimitgliedschaft der zutrittsberechtigten Person.
geschlecht | Geschlecht des Parlamentariers, M=Mann, F=Frau
arbeitssprache | Arbeitssprache des Zutrittsberechtigten
homepage | Homepage der zutrittsberechtigen Person
twitter_name | Twittername
linkedin_profil_url | URL zum LinkedIn-Profil
xing_profil_name | Profilname in XING (letzter Teil von Link), wird ergänzt mit https://www.xing.com/profile/ zu einem ganzen Link
facebook_name | Facebookname (letzter Teil von Link), wird mit https://www.facebook.com/ zu einem ganzen Link ergänzt
beschreibung | Umschreibung des Mandates. Beschreibung wird nicht ausgewertet, jedoch in den Resultaten angezeigt.
von | Beginn des Mandates, leer (NULL) = unbekannt
bis | Ende des Mandates, leer (NULL) = aktuell gültig, nicht leer = historischer Eintrag
art | Art der Funktion des Mandatsträgers innerhalb der Organisation
funktion_im_gremium | Funktion innerhalb des Gremiums, z.B. Präsident in einem Vorstand einer AG entspricht einem Verwatlungsratspräsidenten, Präsident einer Geschäftsleitung entspricht einem CEO.
hauptberuflich | Eigene Firma/Haupttätigkeit: Ist dieses Mandat hauptberuflich? (Hauptberufliche Mandate müssen nicht offengelegt werden.)
wirksamkeit | 'tief', 'mittel', 'hoch': Wirksamkeit des Mandates analog zur Wirksamkeit von Interessenbindungen, siehe https://lobbywatch.ch/de/seite/wirksamkeit, jedoch ohne Einbezug der Kommissionen.
organisation_id | Fremdschlüssel Organisation
name_de | Name der Organisation. Sollte nur juristischem Namen entsprechen, ohne Zusätze, wie Adresse. Deutscher Name des Datensatzes.
ort | Ort der Organisation
rechtsform | Rechtsform der Organisation
typ | Typ der Organisation. Beziehungen können über Organisation_Beziehung eingegeben werden.
vernehmlassung | Häufigkeit der Teilname an nationalen Vernehmlassungen
interessengruppe1 | Zuteilung der Organisation zur Lobbygruppe (Hauptlobbygruppe der Organisation), deutsch
interessengruppe1_branche | Zugehörigkeit zur Branche aufgrund der Hauptlobbygruppe (interessengruppe1) der Organisation, deutsch
interessengruppe1_branche_kommission_abkuerzung | Deutsches Kürzel der zugeordneten Kommission aufgrund der Branche der Organisation

