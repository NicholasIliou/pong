"""
Aufgabe: Klassen und Objekte
----------------------------

Folgender Code modelliert Rechtecke und Punkte und implementiert eine 
Funktion `contains` welche prüft ob sich ein Punkt innerhalb eines Rechtecks 
befindet. Wandeln Sie den Code in einen *objekt-orientierten* Code um. 

1. Erstellen Sie eine Klasse `Point`:
    - die Klasse soll zwei Member-Variablen (Attribute) besitzen: `x`, `y`
    - beide Variablen sollen im Konstruktor initialisiert werden.
    - die Klasse soll außerdem eine Member-Methode mit dem Namen `__str__()` besitzen, welche einen wie folgt formatierten String zurückliefert:
      (31, 41)

Hinweis: Lassen Sie sich vom CS50-Chatbot ([Link](https://cs50.ai/chat)) erklären, 
         für was die `__str__`-Member-Methode ist.

2. Erstellen Sie eine Klasse `Rectangle`:
    - die Klasse soll die folgenden Member-Variablen (Attribute) besitzen: `x`, `y`, `width` und `height`
    - Alle Member-Variablen (Attribute) sollen im Konstruktor initialisiert werden.
    - Fügen Sie eine Member-Methode `contains` hinzu, welche prüft, ob ein übergebenes Objekt vom Typ Point sich innerhalb des
      Rechtecks befindet. Die Funktion soll `True`, oder `False` zurückliefern.
    - Fügen Sie außerdem eine Member-Funktion mit dem Namen `__str__()` hinzu, welche einen wie folgt formatierten String zurückliefert:
      x: 10, y: 12, width: 100, height: 30

3. Erzeugen Sie Objekte der Klassen und prüfen Sie mit Hilfe von contains, ob die Punkte innerhalb des Rechtecks liegen.

"""

class Point:
    def __init__(self,x:int,y:int):
        self.x=x
        self.y=y
    def __str__(self):
        return(f"{self.x}, {self.y}")

class Rectangle:
    def __init__(self,x:int,y:int,width:int,height:int):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
    def contains(self, point):
        if point.x < self.x or point.y < self.y:
            return False
        if point.x > self.x + self.width or point.y > self.y + self.height:
            return False
        return True
    def __str__(self):
        return(f"x: {self.x}, y: {self.y}, width: {self.width}, height: {self.height}")

point1 = Point(31, 41)
point2 = Point(-3, 50)
rect = Rectangle(x=10, y=12, width=100, height=30)
rect.contains(point1)

print(rect.contains(point1))
print(rect.contains(point2))
