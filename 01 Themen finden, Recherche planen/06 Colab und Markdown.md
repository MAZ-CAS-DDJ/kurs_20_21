# Erste Bekanntschaft mit Jupyter Notebook

In einem ersten Schritt werden wir mit Google Colab arbeiten. Das ist einfacher, weil wir uns um das ganze Setup nicht kümmern müssen, weil sich alles in der Cloud befindet.

Wenn ihr beginnt, grosse Datensätze mit Google Colab zu bearbeiten, dann wird es in der Cloud allerdings etwas mühsam. Deshalb werden wir im Verlaufe der nächsten Wochen auf eine lokale Variante umsteigen. Diese Cloud-Arbeitsfläche ist aber auch künftig gut zu kennen: Sie lässt sich in jedem Browser auf jedem Computer bedienen.

- Loggt euch also bei Google Drive mit eurer G-Mailadresse ein. (Das ist natürlich ein grosser Nachteil. Es braucht eine Gmail-Adresse. Aber Google hat das ganze Colab-Werkzeug auch aufgebaut.)
- Wählt in der Liste Google Colaboraty aus. Wenn es nicht da ist, müsst ihr euer Drive mit dem nötigen Addon ausstatten.
- Gut ist es, wenn ihr euch von Anfang an, eine sinnvolle Ordner Struktur überlegt. So findet ihr die Files nachher wieder schnell.
- Nun starten wir also ein solches Google Colab
- Das werdet ihr in den nächsten Tagen sehr viel tun. Denn das wird eure Arbeitsfläche sein.
- Am Freitag werden wir uns dann wieder davon lösen. Nicht ganz. Aber dann werden wir die lokale Lösung kennenlernen.

Diese Colab-Notebooks sind im Grunde identisch mit sogenannten Jupyter Notebooks haben zwei Modi: MarkDown und Code. Wir können den Modus pro Zelle einstellen.

# MarkDown

Den MarkDown-Modus wählen wir, um unseren Code zu beschreiben und zu strukturieren. Das ist sehr wichtig. Nur wirklich gut dokumenteirter Code ist auch nützlich - kann zu einem späteren Zeitpunkt wiederverwendet werden. Es lohnt sich deshalb früh anzueignen, Code möglichst genau zu dokumentieren.

Um auf MarkDown zu wechseln, gehen wir auf "Cell" und wählen "Markdown" an.

Um Text zu formatieren gibt es ein paar ganz grundlegende Befehle.
- Für Titel benutzt ihr #
- Für Untertitel ##, ### uns so weiter.
- Um Wörter einzufetten, rahmt ihr sie mit zwei Sternchen ein: **hallo**
- Aufzählungen könnt ihr mit Zahlen 1. oder mit einem simplen Bindestrich darstellen.
- Wer mehr wissen will, zum Beispiel Tabellen bauen usw., findet mehr [hier](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).
- Wenn ihr Code-Zeilen nur beschreiben wollt, braucht ihr allerdings nicht in den Markdown-Modus zu wechseln. Es gibt dafür die einfache Möglichkeit, vor jeder Code-Zeile ein # zu setzen. Im Code-Modus macht das keinen Titel, sondern es sagt dem Computer, dass er alles was auf derselben Zeile dahinterkommt, nicht beachten muss.

Üben wir das ein wenig:
- Geht zurück zu Jupyter Notebook. Wechselt in der ersten Zelle in den Markdown-Modus.
- Gebt dort als Titel ein: "Mein erster Code"
- Drückt ausführen. Dann erfasst ihr als Text, wie im Markdown-Modus: "Als Erstes werde ich den den Text 'hello world' ausdrucken." Führt die Zelle wieder aus.
- Dann lässt ihr eine Zelle aus. Und gebt in der übernächten ein. "Hier verlange ich einen Input" ein.

# Python 3

Wir arbeiten mit Python 3. Das ist die neueste Version. Ihr stösst im Netz oft auf Python 2. Der grösste Unterschied betrifft auf den ersten Blick das Print-Verhalten. Bei Python 3 müssen wir alles in Klammern verpacken, damit der Computer versteht, was wir wollen.

Also, geben wir ein ```print("Hello World")```

So, und schon habt ihr euer erstes Programm geschrieben. Ihr seht, dass sich das statement **print** automatisch grün färbt. Das ist ein Zeichen dafür, dass der Computer das als Befehl erkannt habt. Und die Zeile, die der Computer ausspucken soll, ist in Anführungs- und Schlusszeichen. Das ist wichtig. Sie können doppelt oder einfach sein.

Alles was zwischen Anführungs und Schlusszeichen ist erkennt der Computer als Text. Er heisst **String**. Ihr werdet ab morgen sehr viel mehr über Strings kennenlernen. Die anderen Datenformate ins **Integers**, ganze Zahlen. Und **Floats**, Zahlen mit Dezimalstellen. Floats und Integers werden ohne Anführungs- und Schlusszeichen geschrieben. Wenn wir das tun, erkennt sie der Computer als Text.

Ihr erkennt schon daran, dass Zahlen für den Computer sehr viel wichtiger sind als Text. Für Text gibt es nur ein Format. Für Zahlen zwei.

Ich möchte hier nicht mehr weiter auf die verschiedenen Datentypen eingehen. Davon werdet ihr morgen noch genug erfahren.

Stattdessen möchte ich neben Print noch einen weiteren Befehl einführen: **input**. Diesen Befehl können wir verwenden, um mit Menschen zu inteagieren. Geben wir ein ```Wie alt bist Du?```. Testet das.
