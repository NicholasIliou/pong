"""
Aufgabe: Klassen und Objekte
----------------------------

Erstelle eine Python-Klasse namens Weihnachtswichtel. 

Die Klasse soll die folgenden Eigenschaften und Methoden haben:

1.Member-Variablen:
- Ein öffentliches Attribut name, das den Namen des Wichtels speichert.
- Ein privates Attribut geschenke_liste, das eine Liste von Geschenken enthält, die der Wichtel vorbereiten soll.
- Ein geschütztes Attribut arbeitsstunden, das die Anzahl der Stunden speichert, die der Wichtel gearbeitet hat.

2. Member-Funktionen:
- Eine öffentliche Methode geschenk_hinzufuegen(geschenk), die ein Geschenk zur geschenke_liste hinzufügt.
- Eine geschützte Methode _arbeitsstunden_hinzufuegen(stunden), die Arbeitsstunden zum Attribut arbeitsstunden hinzufügt.
- Eine private Methode __geschenke_anzeigen(), die die Geschenke in der Liste ausgibt.
- Eine öffentliche Methode wichtel_informieren(), die den Namen des Wichtels, die Anzahl der Arbeitsstunden und 
  die Geschenkeliste anzeigt. (Nutze dabei die private Methode __geschenke_anzeigen.)

Beispiel:

Der folgende Code

    wichtel = Weihnachtswichtel("Frodo")
    wichtel.geschenk_hinzufuegen("Teddy")
    wichtel.geschenk_hinzufuegen("Puzzle")
    wichtel._arbeitsstunden_hinzufuegen(5)
    wichtel.wichtel_informieren()

soll folgende Ausgabe erzeugen:

    Wichtelname: Frodo
    Arbeitsstunden: 5
    Geschenkeliste: ['Teddy', 'Puzzle']

"""

class Weihnachtswichtel:
    
    def __init__(self,name,geschenke_liste:list=[],arbeitsstunden:int=0):
        self.name=name
        self.__geschenke_liste=geschenke_liste
        self._arbeitsstunden=arbeitsstunden

    def geschenk_hinzufuegen(self,geschenk:str):
        self.__geschenke_liste.append(geschenk)

    def _arbeitsstunden_hinzufuegen(self,stunden):
        self._arbeitsstunden+=stunden

    def __geschenke_anzeigen(self):
        return self.__geschenke_liste
    
    def wichtel_informieren(self):
        print(f"""Wichtelname: {self.name}
Arbeitsstunden: {self._arbeitsstunden}
Geschenkeliste: {self.__geschenke_anzeigen()}
""")





wichtel = Weihnachtswichtel("Frodo")
wichtel.geschenk_hinzufuegen("Teddy")
wichtel.geschenk_hinzufuegen("Puzzle")
wichtel._arbeitsstunden_hinzufuegen(5)
wichtel.wichtel_informieren()