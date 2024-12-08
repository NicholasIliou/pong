# Bücherei

Sie finden in `main.py` die Verwaltungssoftware einer Bücherei.

Die Software funktioniert sehr gut, nur leider ist ziemlich viel Code in der `main.py` gelandet, was es schwierig macht:

* Fehler zu finden und zu korrigieren,
* das Programm zu erweitern,
* das Programm weiterzugeben und
* das Programm zu lesen.

## Refaktorisieren von Code

Refaktorisieren von Code bedeutet, den bestehenden Code zu verbessern, ohne das externe Verhalten des Programms zu verändern. 
Das Ziel des Refaktorisierens ist es, den Code lesbarer, wartungsfreundlicher und effizienter zu machen. 
Es handelt sich also um eine Umstrukturierung des Codes, bei der der Code an sich optimiert wird, ohne dass neue Funktionen hinzugefügt oder bestehende Funktionen verändert werden.
In den ersten Teilen der Aufgabe werden Sie den bestehenden Code refaktorisieren.
Im weiteren Teil werden Sie noch zusätzliche Funktionen schreiben, um die Funktionalität des Bibliotheksverwaltungsprogramms zu erweitern.
 
## Aufgabe 1

Refaktorisieren Sie den bestehenden Code, indem Sie ein Modul `library_manager` anlegen und alle Funktionen auslagern, mit der die Daten der Bibliothek (`books`) verändert oder ausgegeben werden.

Idealerweise verbleibt in der `main.py` somit nur noch der Code, der das User Interface (Konsolenanwendung) bereitstellt.

## Aufgabe 2

Sie haben im Rahmen der Refaktorisierung vermutlich ebenfalls die Variable `books` in die Datei `library_manager` ausgelagert. 
Nennen Sie einen Vor- und einen Nachteil von `books` in `library_manager`?

## Aufgabe 3

Ändern Sie den Code nun so ab, dass die Variable `books` in der `main()`-Funktion erzeugt wird. 
Wie müssen Sie hierfür die Funktionen des Moduls `library_manager` anpassen?

## Aufgabe 4

Schreiben Sie in der Datei `library_manager.py` Test-Code, welcher die einzelnen Funktionen aufruft und so die Funktionen testet.
Stellen Sie so sicher, dass die Library nach der Umstrukturierung noch funktioniert. 
Der Test-Code soll nur ausgeführt werden, wenn die Datei selbst ausgeführt wird.
Wird das Modul importiert, darf der Code nicht ausgeführt werden.

## Aufgabe 5

Schreiben Sie nun noch ein Modul `library_status` welches Funktionen implementiert, um den Büchereibestand und den aktuellen Ausleihstatus aus einer Datei einzulesen (Funktion `load_library_status()`) und auch wieder abzuspeichern (Funktion `store_library_status()`).

Der Inhalt der Datei (z.B. `data.csv`) soll wie folgt aussehen:

```text
Name,Author,ISBN,Status
Automate the Boring Stuff with Python,Al Sweigart,9781593275990,borrowed
Python Crash Course,Eric Matthes,9781593279288,borrowed
Fluent Python,Luciano Ramalho,9781491946008,available
Learning Python,Mark Lutz,9781449355739,borrowed
Python for Data Analysis,Wes McKinney,9781491957660,available
Effective Python,Brett Slatkin,9780134034287,available
```

Nutzen Sie diese Funktionen in der `main.py`, um den letzten Zustand aus der Datei zu laden und auch um Änderungen im Bestand und Ausleihzustand persistent zu speichern (d.h. bei einem Neustart des Programms sollte der letzte Stand wieder aus der Datei hergestellt werden).

**Tipp:** Übergeben Sie der Funktion `store_library_status` das Dictionary `books` und `borrowed_books` als Parameter. In der Funktion erzeugen Sie dann ein neues Dictionary, welches zusätzlich zu den Information von `books` noch den Status als String beinhaltet. Dieses Dictionary schreiben Sie dann in eine Datei, entweder mit einer selbst programmierten Funktion (super Übung) oder Sie verwenden das Python-Modul `csv` (ebenfalls eine sehr gute Übung, also machen Sie am besten beides ;-)).

**Tipp 2:** Um an die Variable `borrowed_books` zu kommen, welche vermutlich Teil des Pakets `library_manager` ist, können Sie in `library_manager` eine sogenannte getter-Funktion schreiben, d.h. eine Funktion namens `get_list_of_borrowed_books()`, welche die Liste `borrowed_books` zurückliefert. Analog können Sie auch eine setter-Funktion schreiben, welche es erlaubt, die Liste im Modul `library_manager` zu setzen.
