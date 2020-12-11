Lobbywatch Export: Neo4j CSV
============================

Datei: export/node_parlamentarier.csv  
Datum: 07.12.2020 02:31:02  
Datensatztyp: node  
Exporttyp: Öffentlich / Public  

Herausgeber: Lobbywatch (https://lobbywatch.ch)  

Die Inhalte von Lobbywatch.ch sind lizenziert unter einer Creative Commons Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz. (https://creativecommons.org/licenses/by-sa/4.0/deed.de)

Data are licensed as CC BY-SA


## parlamentarier (parlamentarier)

Datensatztyp: node

Feld | Beschreibung
- | -
anzeige_name | Der Anzeigename ist eine Kombination anderer Namensfelder. Dieser Name enthält die relevanten Bestandteile zur Anzeige. In der Regel ist der deutsche Name enthalten.
anzeige_name_de | Deutscher Anzeigename. Er ist eine Kombination anderer Namensfelder. Dieser Name enthält die relevanten Bestandteile zur Anzeige.
anzeige_name_fr | Französischer Anzeigename. Er ist eine Kombination anderer Namensfelder. Dieser Name enthält die relevanten Bestandteile zur Anzeige.
name | Name des Datensatzes. In der Regel ist der deutsche Name enthalten.
name_de | Deutscher Name des Datensatzes.
name_fr | Französicher Name des Datensatzes.
id | Technischer Schlüssel des Parlamentariers Technischer Schlüssel
nachname | Nachname des Parlamentariers
vorname | Vornahme des Parlamentariers
vorname_kurz | Alltagsvorname oder gebräuchlicher Spitzname, z.B. Nik für Niklaus
zweiter_vorname | Zweiter Vorname des Parlamentariers
rat_id | Ratszugehörigkeit; Fremdschlüssel des Rates
kanton_id | Kantonszugehörigkeit; Fremdschlüssel des Kantons
kommissionen | Abkürzungen der Kommissionen des Parlamentariers (automatisch erzeugt [in_Kommission Trigger])
partei_id | Fremdschlüssel Partei. Leer bedeutet parteilos.
parteifunktion | Funktion des Parlamentariers in der Partei
fraktion_id | Fraktionszugehörigkeit im nationalen Parlament. Fremdschlüssel.
fraktionsfunktion | Funktion des Parlamentariers in der Fraktion
im_rat_seit | Jahr der Zugehörigkeit zum Parlament
im_rat_bis | Austrittsdatum aus dem Parlament. Leer (NULL) = aktuell im Rat, nicht leer = historischer Eintrag
ratswechsel | Datum in welchem der Parlamentarier den Rat wechselte, in der Regel vom National- in den Ständerat. Leer (NULL) = kein Ratswechsel hat stattgefunden
ratsunterbruch_von | Unterbruch in der Ratstätigkeit von, leer (NULL) = kein Unterbruch
ratsunterbruch_bis | Unterbruch in der Ratstätigkeit bis, leer (NULL) = kein Unterbruch
beruf | Beruf des Parlamentariers
beruf_fr | Beruf des Parlamentariers auf französisch
beruf_interessengruppe_id | Zuordnung (Fremdschlüssel) zu Interessengruppe für den Beruf des Parlamentariers
titel | Titel des Parlamentariers, wird von ws.parlament.ch importiert
aemter | Politische Ämter (importiert von ws.parlament.ch mandate)
weitere_aemter | Zusätzliche Ämter (importiert von ws.parlament.ch additionalMandate)
zivilstand | Zivilstand
anzahl_kinder | Anzahl der Kinder
militaerischer_grad_id | Militärischer Grad, leer (NULL) = kein Militärdienst
geschlecht | Geschlecht des Parlamentariers, M=Mann, F=Frau
geburtstag | Geburtstag des Parlamentariers
photo_dateiname | Photodateiname ohne Erweiterung
photo_dateierweiterung | Erweiterung der Photodatei
photo_dateiname_voll | Photodateiname mit Erweiterung
photo_mime_type | MIME Type des Photos
kleinbild | Bild 44x62 px oder leer.png
sitzplatz | Sitzplatznr im Parlament. Siehe Sitzordnung auf parlament.ch
homepage | Homepage des Parlamentariers
homepage_2 | Zweite Homepage, importiert von ws.parlament.ch
parlament_biografie_id | Biographie ID auf Parlament.ch; Dient zur Herstellung eines Links auf die Parlament.ch Seite des Parlamenteriers. Zudem kann die ID für die automatische Verarbeitung gebraucht werden.
parlament_number | Number Feld auf ws.parlament.ch, wird von ws.parlament.ch importiert, wird z.B. als ID für Photos verwendet.
parlament_beruf_json | Importierter Beruf des Parlamentariers: Beruf, Arbeitgeber, Jobtitel/Funktion, von, bis (von parlament.ch)
parlament_interessenbindungen | Importierte Interessenbindungen von ws.parlament.ch
parlament_interessenbindungen_json | Importierte Interessenbindungen von ws.parlament.ch als JSON. Rechtsformen: -, AG, Anst., EG, EidgKomm, Gen., GmbH, KollG, Komm., Körp., Stift., Ve., öffStift; Gremien: -, A, AufR., Bei., D, GL, GL, V, GV, Pat., Sr., V, VR, Vw., ZA, ZV; Funktionen: -, A, AufR., Bei., D, GL, GL, V, GV, Pat., Sr., V, VR, Vw., ZA, ZV
parlament_interessenbindungen_updated | Datum, wann die Interessenbindungen von ws.parlament.ch zu letzt aktualisiert wurden.
twitter_name | Twittername
linkedin_profil_url | URL zum LinkedIn-Profil
xing_profil_name | Profilname in XING (letzter Teil von Link), wird ergänzt mit https://www.xing.com/profile/ zu einem ganzen Link
facebook_name | Facebookname (letzter Teil von Link), wird mit https://www.facebook.com/ zu einem ganzen Link ergänzt
wikipedia | Link zum Wikipedia-Eintrag des Parlamentariers
sprache | Sprache des Parlamentariers, wird von ws.parlament.ch importiert
arbeitssprache | Arbeitssprache des Parlamentariers, erhältlich auf parlament.ch
adresse_firma | Wohnadresse des Parlamentariers, falls verfügbar, sonst Postadresse; Adressen erhältlich auf parlament.ch
adresse_plz | Wohnadresse des Parlamentariers, falls verfügbar, sonst Postadresse; Adressen erhältlich auf parlament.ch
adresse_ort | Wohnadresse des Parlamentariers, falls verfügbar, sonst Postadresse; Adressen erhältlich auf parlament.ch
erfasst | Ist der Parlamentarier erfasst? Falls der Parlamentarier beispielsweise nicht mehr zur Wiederwahl antritt und deshalb nicht erfasst wird, kann dieses Feld auf Nein gestellt werden. NULL bedeutet Status unklar.
freigabe_datum | Freigabedatum (Freigabe = Daten sind fertig)
beruf_de | Beruf des Parlamentariers
von | Jahr der Zugehörigkeit zum Parlament
bis | Austrittsdatum aus dem Parlament. Leer (NULL) = aktuell im Rat, nicht leer = historischer Eintrag
aktiv | 0/1: Ist der Datensatz zum Zeitpunkt des Exportes aktuell? , 1=aktiv, 0=abgelaufen/historisiert. Der Wert 'aktiv' wird vom 'von'- und 'bis'-Datum berechnet.
geburtstag_unix | Datum als UNIX-Timestap (Sekunden seit 1.1.1970), siehe geburtstag
im_rat_seit_unix | Datum als UNIX-Timestap (Sekunden seit 1.1.1970), siehe im_rat_seit
im_rat_bis_unix | Datum als UNIX-Timestap (Sekunden seit 1.1.1970), siehe im_rat_bis
freigabe_datum_unix | Publikationsdatum als UNIX-Timestap (Sekunden seit 1.1.1970), siehe 'freigabe_datum'
von_unix | Von-Datum als UNIX-Timestap (Sekunden seit 1.1.1970), siehe 'von'
bis_unix | Bis-Datum als UNIX-Timestap (Sekunden seit 1.1.1970), siehe 'bis'

