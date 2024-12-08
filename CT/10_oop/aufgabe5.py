"""
Aufgabe: Klassen und Objekte
----------------------------

Elektroauto-Klasse mit Energieverbrauch
Erstelle eine Python-Klasse Elektroauto, die ein Fahrzeug mit einem Elektromotor modelliert. 
Dabei soll der Energieverbrauch und der Batteriestand verwaltet werden.

Anforderungen:

1.Attribute:
    - marke (str): Marke des Elektroautos.
	- modell (str): Modell des Elektroautos.
	- verbrauch (float): Energieverbrauch in kWh pro 100 km.
	- batteriestand (float): Aktueller Batteriestand in kWh.

2.Methoden:
	- fahren(km: float) -> None: Reduziert den Batteriestand entsprechend der gefahrenen Kilometer und dem Verbrauch. 
                                 Gibt eine Warnung aus, falls die Batterie leer ist.
	- laden(kwh: float) -> None: Erhöht den Batteriestand um die angegebene Energiemenge.
	- zeige_details() -> None: Gibt Fahrzeugdetails, Energieverbrauch und Batteriestand aus.
    
3.Teste die Klasse:
	- Erstelle ein Elektroauto mit:
	- Marke: “BMW”, Modell: “iX1”, Verbrauch: 18.0 kWh/100 km, Batteriestand: 64 kWh.
	- Fahre 150 km.
	- Lade 30 kWh.
	- Fahre weitere 200 km und zeige die Fahrzeugdetails an.

Beispiel:

    Folgender Code 

        auto = Elektroauto("BMW", "iX1", 18.0, 64)
        auto.fahren(150)
        auto.laden(30)
        auto.fahren(200)
        auto.zeige_details()

    soll folgende Ausgabe erzeugen: 

        150 km gefahren. Batteriestand: 37.00 kWh
        30 kWh geladen. Neuer Batteriestand: 67.00 kWh
        200 km gefahren. Batteriestand: 31.00 kWh
        Elektroauto: BMW iX1
        Energieverbrauch: 18.0 kWh/100 km
        Batteriestand: 31.00 kWh

"""

class Elektroauto:
    
    def __init__(self, marke: str, modell: str, verbrauch: float, batteriestand: float):
        self.marke = marke
        self.modell = modell
        self.verbrauch = verbrauch
        self.batteriestand = batteriestand
    
    def fahren(self,km:float)->None:
        self.batteriestand-=((self.verbrauch/100)*km)
        print(f"{km} km gefahren. Batteriestand: {self.batteriestand:.2f} kWh")

    def laden(self,kwh:float)->None:
        self.batteriestand+=kwh
        print(f"{kwh} kWh geladen. Neuer Batteriestand: {self.batteriestand:.2f} kWh")

    def zeige_details(self)->None:
        print(f"""Elektroauto: {self.marke} {self.modell}
Energieverbrauch: {self.verbrauch} kWh/100 km
Batteriestand: {self.batteriestand:.2f} kWh
            """)

auto = Elektroauto("BMW", "iX1", 18.0, 64)
auto.fahren(150)
auto.laden(30)
auto.fahren(200)
auto.zeige_details()