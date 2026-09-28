# Zadanie: Motorcycle class
#
# Napisz klase Motorcycle z:
# - __init__(self, brand, model, year, engine_cc)
# - @property dla age (obliczane: 2026 - year)
# - @property + setter dla engine_cc z walidacja (musi byc > 0)
# - Metoda specs() zwracajaca string: "Honda CBR600RR (2020), 600cc, 6 lat"
#
# Wskazowki:
# - engine_cc przechowuj w _engine_cc (z podkreślnikiem)
# - age nie ma settera — to readonly property
# - specs() zwraca string, nie printuje
#
# Test:
# m = Motorcycle("Honda", "CBR600RR", 2020, 600)
# print(m.age)        # 6
# print(m.specs())    # "Honda CBR600RR (2020), 600cc, 6 lat"
# m.engine_cc = 0     # ValueError: Engine CC must be positive


# Twoj kod tutaj:

class Motorcycle:
    
    def __init__(self, brand, model, year, engine_cc):
        self.brand = brand
        self.model = model
        self.year = year
        self._engine_cc = engine_cc
        
    @property
    def age(self) -> int:
        return 2026 - self.year
    
    @property
    def engine_cc(self) -> int:
        return self._engine_cc
    
    @engine_cc.setter
    def engine_cc(self, value: int):
        if value <= 0:
            raise ValueError ("Engine CC must be positive")
        else:
            self._engine_cc = value
            
    def specs(self):
        return f"{self.brand} {self.model} ({self.year}), {self._engine_cc}cc, {self.age} lat"