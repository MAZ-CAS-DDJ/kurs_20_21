Lobbywatch Export: Neo4j CSV
============================

Datei: export/node_person.csv  
Datum: 07.12.2020 02:31:02  
Datensatztyp: node  
Exporttyp: Öffentlich / Public  

Herausgeber: Lobbywatch (https://lobbywatch.ch)  

Die Inhalte von Lobbywatch.ch sind lizenziert unter einer Creative Commons Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz. (https://creativecommons.org/licenses/by-sa/4.0/deed.de)

Data are licensed as CC BY-SA


## person (person)

Datensatztyp: node

Feld | Beschreibung
- | -
anzeige_name | Der Anzeigename ist eine Kombination anderer Namensfelder. Dieser Name enthält die relevanten Bestandteile zur Anzeige. In der Regel ist der deutsche Name enthalten.
anzeige_name_de | Deutscher Anzeigename. Er ist eine Kombination anderer Namensfelder. Dieser Name enthält die relevanten Bestandteile zur Anzeige.
anzeige_name_fr | Französischer Anzeigename. Er ist eine Kombination anderer Namensfelder. Dieser Name enthält die relevanten Bestandteile zur Anzeige.
name | Name des Datensatzes. In der Regel ist der deutsche Name enthalten.
name_de | Deutscher Name des Datensatzes.
name_fr | Französicher Name des Datensatzes.
id | Technischer Schlüssel der Zugangsberechtigung Technischer Schlüssel
nachname | Nachname des berechtigten Persion
vorname | Vorname der berechtigten Person
zweiter_vorname | Zweiter Vorname der zutrittsberechtigten Person
namensunterscheidung | Namenszusatz zur Unterscheiden von Personen mit exakt gleichem Namen. Ein Unterscheidungsmerkmal der Person z.B. der Beruf, sollte im Feld gespeichert werden. NUR BEI PERSONEN MIT EXAKT GLEICHEM VORNAMEN UND NAMEN VERWENDEN.
beschreibung_de | Beschreibung der Person. Der Text ist öffentlich einsehbar.
beschreibung_fr | Französische Beschreibung der Person. Der Text ist öffentlich einsehbar.
parlamentarier_kommissionen | Abkürzungen der Kommissionen des zugehörigen Parlamentariers (automatisch erzeugt [in_Kommission/person Trigger])
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
erfasst | Ist die Person erfasst? Falls der zugehörige Parlamentarier beispielsweise nicht mehr zur Wiederwahl antritt und deshalb die Person nicht erfasst wird, kann dieses Feld auf Nein gestellt werden. NULL bedeutet Status unklar.
freigabe_datum | Freigabedatum (Freigabe = Daten sind fertig)
freigabe_datum_unix | Publikationsdatum als UNIX-Timestap (Sekunden seit 1.1.1970), siehe 'freigabe_datum'

