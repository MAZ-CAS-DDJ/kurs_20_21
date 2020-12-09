Lobbywatch Export: Neo4j CSV
============================

Datei: export/node_kommission.csv  
Datum: 07.12.2020 02:31:02  
Datensatztyp: node  
Exporttyp: Öffentlich / Public  

Herausgeber: Lobbywatch (https://lobbywatch.ch)  

Die Inhalte von Lobbywatch.ch sind lizenziert unter einer Creative Commons Namensnennung - Weitergabe unter gleichen Bedingungen 4.0 International Lizenz. (https://creativecommons.org/licenses/by-sa/4.0/deed.de)

Data are licensed as CC BY-SA


## kommission (kommission)

Datensatztyp: node

Feld | Beschreibung
- | -
anzeige_name | Der Anzeigename ist eine Kombination anderer Namensfelder. Dieser Name enthält die relevanten Bestandteile zur Anzeige. In der Regel ist der deutsche Name enthalten.
anzeige_name_de | Deutscher Anzeigename. Er ist eine Kombination anderer Namensfelder. Dieser Name enthält die relevanten Bestandteile zur Anzeige.
anzeige_name_fr | Französischer Anzeigename. Er ist eine Kombination anderer Namensfelder. Dieser Name enthält die relevanten Bestandteile zur Anzeige.
anzeige_name_mixed | Anzeigename deutsch und französisch
id | Technischer Schlüssel der Kommission Technischer Schlüssel
abkuerzung | Kürzel der Kommission
abkuerzung_fr | Französisches Kürzel der Kommission
name | Ausgeschriebener Name der Kommission Name des Datensatzes. In der Regel ist der deutsche Name enthalten.
name_fr | Ausgeschriebener französischer Name der Kommission Französicher Name des Datensatzes.
rat_id | Ratszugehörigkeit; Fremdschlüssel des Rates
typ | Typ einer Kommission (Spezialkommission ist eine Delegation im weiteren Sinne).
art | Art der Kommission gemäss Einteilung auf Parlament.ch. Achtung für Delegationen im engeren Sinne (= Subkommissionen) sollte die Art der Mutterkommission gewählt werden, z.B. GPDel ist eine Subkommission der GPK und gehört somit zu den Aufsichtskommissionen.
beschreibung | Beschreibung der Kommission
beschreibung_fr | Französische Beschreibung der Kommission
sachbereiche | Liste der Sachbereiche der Kommission, abgetrennt durch ";".
sachbereiche_fr | Liste der Sachbereiche der Kommission auf französisch, abgetrennt durch ";".
anzahl_mitglieder | Anzahl Kommissionsmitglieder
anzahl_nationalraete | Anzahl Kommissionsmitglieder des Nationalrates
anzahl_staenderaete | Anzahl Kommissionsmitglieder des Ständerates
mutter_kommission_id | Zugehörige Kommission von Delegationen im engeren Sinne (=Subkommissionen).  Also die "Oberkommission".
zweitrat_kommission_id | Entsprechende Kommission im anderen Rat, Stände- o. Nationalratskommission
von | Beginn der Kommission, leer (NULL) = unbekannt
bis | Ende der Kommission, leer (NULL) = aktuell gültig, nicht leer = historischer Eintrag
parlament_url | Link zur Seite auf Parlament.ch
parlament_id | Kommissions-ID von ws.parlament.ch
parlament_committee_number | committeeNumber auf ws.parlament.ch
parlament_subcommittee_number | subcommitteeNumber auf ws.parlament.ch
parlament_type_code | typeCode von ws.parlament.ch
freigabe_datum | Freigabedatum (Freigabe = Daten sind fertig)
name_de | Ausgeschriebener Name der Kommission Deutscher Name des Datensatzes.
abkuerzung_de | Kürzel der Kommission
beschreibung_de | Beschreibung der Kommission
sachbereiche_de | Liste der Sachbereiche der Kommission, abgetrennt durch ";".
freigabe_datum_unix | Publikationsdatum als UNIX-Timestap (Sekunden seit 1.1.1970), siehe 'freigabe_datum'

