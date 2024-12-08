"""
Aufgabe: Klassen und Objekte
----------------------------

Diskutieren Sie mit einer Kommilitionin/einem Kommilitonen:
Das Rechteck aus Aufgabe 3 ist durch einen Startpunkt `x`, `y` und durch die 
Breite `width` und Höhe `height` eindeutig definiert. Ein Punkt wiederum 
durch `x` und `y`. Würden Sie zustimmen, dass deshalb ein Punkt eine Abstraktion 
eines Rechtecks ist?

Ändern Sie Aufgabe 3 ab das:

Ändern Sie Ihre Klasse `Rectangle`:

1. Nutzten Sie anstatt `x`, `y` einen `point` des Typs `Point`
2. Führen Sie Methoden `get_x1`, `get_y1`, `get_x2`, `get_y2` ein, welche Ihnen 
   `point.x`, `point.y` sowie `point.x + width` und `point.y + height` zurückliefern.
3. Machen Sie alle Attribute privat.

4. Erweitern Sie Ihre Klasse `Point` um die Methode `__add__(self, other: any) -> any` und `__sub__(self, other: any) -> any`.
   Die Member-Methoden müssen beide als Ergebnis ein neues Objekt vom Typ `Point` zurückliefern.
   Durch die Implementierung ist nun folgendes möglich:

    point1 = Point(1, 1)
    point2 = Point(2, 3)
    point3 = point1 + point2
    point4 = point2 - point1
    print(point1)
    print(point2)
    print(point3)
    print(point4)

Hinweis1: In self steckt das Objekt links vom +/- Operator, in other steckt das Objekt rechts vom Operator.

Hinweis2: Man nennt die Implementierung dieser Funktionen "Überladen des `+` bzw. `-`-Operators".
         Fragen Sie CS50, welche Funktionen sie noch überladen können.

Hinweis3: any ist an der Stelle notwendig, weil Point erst in der Funktion definiert ist, aber noch nicht
          bei der Auswertung der Funktionssignatur.

Vermeiden Sie bei Ihrer Implementierung doppelten Code!

"""

class Point:
    def __init__(self, x: int, y: int) -> None:
        self.__x = x
        self.__y = y
      
    def __str__(self) -> str:
        return f'({self.__x}, {self.__y})'

    def __add__(self,other:any)->any:
        return self.__x + self.__y + other.get_x() + other.get_y()

    def __sub__(self,other:any)->any:
        return (self.__x + self.__y) - (other.get_x() + other.get_y())
    
    def get_x(self)->int:
        return self.__x
    def get_y(self)->int:
        return self.__y

class Rectangle:
    def __init__(self,point:Point, width: int, height: int) -> None:
        self.x = point.get_x()
        self.y = point.get_y()
        self.width = width
        self.height = height
      
    def __str__(self) -> str:
        return f'x: {self.x}, y: {self.y}, width: {self.width}, height: {self.height}'
  
    def contains(self, point: Point) -> bool:
        if point.get_x() < self.x or point.get_y() < self.y:
            return False
        if point.get_x() > self.x + self.width or point.get_y() > self.y + self.height:
            return False
        return True

    def getx1(self,point: Point):
        return point.__x
    def gety1(self,point: Point):
        return point.__y
    def getx2(self,point: Point):
        return point.__x + self.width
    def gety2(self,point: Point):
        return point.__x + self.height

point1=Point(1,12)
rect1=Rectangle(point1,24,43)
print(rect1.contains(point1))

point1 = Point(1, 1)
point2 = Point(2, 3)
point3 = point1 + point2
point4 = point2 - point1
print(point1)
print(point2)
print(point3)
print(point4)