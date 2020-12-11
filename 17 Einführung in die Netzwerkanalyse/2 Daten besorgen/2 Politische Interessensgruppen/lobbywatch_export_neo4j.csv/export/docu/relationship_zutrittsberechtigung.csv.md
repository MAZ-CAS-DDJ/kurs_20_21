Lobbywatch Export: Neo4j CSV
============================

Datei: export/relationship_zutrittsberechtigung.csv  
Datum: 07.12.2020 02:31:02  
Datensatztyp: relationship  
Exporttyp: Öffentlich / Public  

Herausgeber: Lobbywatch (https://lobbywatch.ch)  

Die Inhalte von Lobbywatch.ch sind lizenziert unter einer Creative Commons Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz. (https://creativecommons.org/licenses/by-sa/4.0/deed.de)

Data are licensed as CC BY-SA


## zutrittsberechtigung (zutrittsberechtigung)

Datensatztyp: relationship

Feld | Beschreibung
- | -
id | Technischer Schlüssel der Zutrittsberechtigung Technischer Schlüssel
parlamentarier_id | Fremdschlüssel Parlamentarier
person_id | Fremdschlüssel zur zutrittsberechtigten Person
parlamentarier_kommissionen | Abkürzungen der Kommissionen des zugehörigen Parlamentariers (automatisch erzeugt [in_Kommission/zutrittsberechtigung Trigger])
funktion | Funktion der zutrittsberechtigen Person.
funktion_fr | Funktion der zutrittsberechtigen Person auf französisch.
von | Beginn der Zutrittsberechtigung, leer (NULL) = unbekannt
bis | Ende der Zutrittsberechtigung, leer (NULL) = aktuell gültig, nicht leer = historischer Eintrag
updated_by_import | Datum, wann die Zutrittsberechtigung durch einen Import zu letzt aktualisiert wurde.
freigabe_datum | Freigabedatum (Freigabe = Daten sind fertig)

