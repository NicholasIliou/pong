"""
Aufgabe: Klassen und Objekte
----------------------------

Erstellen Sie eine Klasse `Student`. Diese Klasse soll mind. die zwei 
Member-Variablen (Attribute) `name` und `age` sowie die Member-Methode `say_hello` umsetzen. 
Die Member-Variablen sollen im Konstruktor initialisiert werden. 
Hierfür sollen dem Konstruktor die Werte für `name` und `age` übergeben werden.

Die Member-Funktion `say_hello` soll den Namen und das Alter ausgeben. 

Erzeugen Sie mehrere Objekte Ihrer Klasse und testen Sie die Member-Methode `say_hello`.
"""

class Student:
    def __init__(self,name:str,age:int)->None:
        self.name=name
        self.age=age
    def say_hello(self):
        print(f"Hallo {self.name}, {self.age}")

student1 = Student("test",3)

if __name__ == "__main__":
    student1.say_hello()