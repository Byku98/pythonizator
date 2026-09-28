# Zadanie 02: Motorcycle — staticmethod, classmethod, dataclass
#
# Ten zadanie rozszerza klase Motorcycle z zadania 01.
# Dodajesz nowe funkcje krok po kroku.
#
# === ETAP 1: @staticmethod ===
# Dodaj metode ktora nie potrzebuje self — czysta logika.
#
# === ETAP 2: @classmethod ===
# Dodaj "alternatywny konstruktor" — tworzy obiekt ze stringa.
#
# === ETAP 3: Licznik instancji ===
# Zliczaj ile motocykli zostalo stworzonych.
#
# === ETAP 4: @dataclass ===
# Przepisz klase na dataclass. Porownaj ile linii kodu zniknelo.


# ==========================================
# ETAP 1: @staticmethod
# ==========================================
#
# Dodaj metode is_valid_year(year: int) -> bool
# - Zwraca True jesli rok jest miedzy 1900 a 2026
# - NIE potrzebuje self — to czysta logika
# - Wywolujesz ja NA klasie: Motorcycle.is_valid_year(2020)
#
# Dlaczego staticmethod a nie classmethod?
# Bo nie potrzebujesz dostepu do klasy (cls).
# To po prostu funkcja ktora logicznie nalezy do tej klasy,
# ale nie potrzebuje zadnego kontekstu.


# ==========================================
# ETAP 2: @classmethod — alternatywny konstruktor
# ==========================================
#
# Dodaj metode from_string(cls, motorcycle_str: str)
# - Parsuje string w formacie: "Honda CBR600RR 2020 600"
# - Zwraca nowy obiekt Motorcycle
# - cls = Motorcycle (nie self!)
#
# Format stringa: "Marka Model Rok Pojemnosc"
# - Marka: jedno slowo (Honda, Yamaha)
# - Model: jedno slowo (CBR600RR, R1)
# - Rok: liczba
# - Pojemnosc: liczba
#
# Uzyj split() do parsowania:
#   "Honda CBR600RR 2020 600".split() → ["Honda", "CBR600RR", "2020", "600"]
#
# Dlaczego classmethod?
# Bo tworzysz NOWY obiekt. Nie masz jeszcze self.
# cls pozwala Ci wywolac Motorcycle(...) bezposrednio.


# ==========================================
# ETAP 3: Licznik instancji
# ==========================================
#
# Dodaj zmienna klasy _count = 0
# - Kazdy __init__ zwieksza _count o 1
# - Dodaj @classmethod get_count(cls) -> int
# - Zwraca aktualna liczbe stworzonych motocykli
#
# Zmienna klasy (_count) jest wspolna dla WSZYSTKICH instancji.
# To jak licznik w fabryce — niezalezny od konkretnego motocykla.


# ==========================================
# ETAP 4: @dataclass (bonus)
# ==========================================
#
# Na koncu pliku jest wersja z @dataclass.
# Porownaj ile linii kodu zniknelo.
# Nie musisz jej zmieniac — po prostu przeczytaj i zrozum.


# ==========================================
# TWOJ KOD — zacznij od Motorcycle z zadania 01
# ==========================================


class Motorcycle:
    
    _count = 0  # zmienna klasy — licznik
    
    def __init__(self, brand: str, model: str, year: int, engine_cc: int):
        self.brand = brand
        self.model = model
        self.year = year
        self._engine_cc = engine_cc
        Motorcycle._count += 1  # kazdy nowy motocykl
        
    @property
    def age(self) -> int:
        return 2026 - self.year
    
    @property
    def engine_cc(self) -> int:
        return self._engine_cc
    
    @engine_cc.setter
    def engine_cc(self, value: int):
        if value <= 0:
            raise ValueError("Engine CC must be positive")
        self._engine_cc = value
            
    def specs(self) -> str:
        return f"{self.brand} {self.model} ({self.year}), {self._engine_cc}cc, {self.age} lat"
        
    # --- ETAP 1: Twoj kod tutaj ---
    # Dodaj @staticmethod is_valid_year
    
    @staticmethod
    def is_valid_year(year: int) -> bool:
        return 1900 <= year <= 2026
    
    # --- ETAP 2: Twoj kod tutaj ---
    # Dodaj @classmethod from_string
    
    @classmethod
    def from_string(cls, motorcycle_str: str):
        parsed = motorcycle_str.split()
        brand = parsed[0]
        model = parsed[1]
        year = int(parsed[2])
        engine_cc = int(parsed[3])
        return cls(brand, model, year, engine_cc)
    
    # --- ETAP 3: Twoj kod tutaj ---
    # Dodaj @classmethod get_count
    @classmethod
    def get_count(cls):
        return cls._count

# ==========================================
# TESTY — odkomentuj po dodaniu kazdego etapu
# ==========================================


#--- ETAP 1 TEST ---
# print("=== ETAP 1: @staticmethod ===")
# print(Motorcycle.is_valid_year(2020))      # True
# print(Motorcycle.is_valid_year(1800))      # False
# print(Motorcycle.is_valid_year(2030))      # False


# --- ETAP 2 TEST ---
# print("\n=== ETAP 2: @classmethod ===")
# m2 = Motorcycle.from_string("Yamaha R1 2023 1000")
# print(m2.specs())                          # "Yamaha R1 (2023), 1000cc, 3 lat"
# print(m2.brand)                            # "Yamaha"
# print(m2.engine_cc)                        # 1000


# --- ETAP 3 TEST ---
# print("\n=== ETAP 3: Licznik ===")
# print(Motorcycle.get_count())              # 2 (m1 + m2)
# m3 = Motorcycle("Suzuki", "GSX-R", 2019, 750)
# print(Motorcycle.get_count())              # 3


# --- FINALNY TEST ---
print("\n=== FINALNY TEST ===")
m1 = Motorcycle("Honda", "CBR600RR", 2020, 600)
m2 = Motorcycle.from_string("Yamaha R1 2023 1000")

print(f"m1: {m1.specs()}")
print(f"m2: {m2.specs()}")
print(f"m1.age = {m1.age}")
print(f"m2.age = {m2.age}")
print(f"Liczba motocykli: {Motorcycle.get_count()}")
print(f"2020 valid? {Motorcycle.is_valid_year(2020)}")
print(f"1800 valid? {Motorcycle.is_valid_year(1800)}")

try:
    m1.engine_cc = 0
except ValueError as e:
    print(f"engine_cc = 0 → {e}")


# ==========================================
# BONUS: @dataclass — porownanie
# ==========================================
#
# Zwykla klasa (co masz wyzej): ~30 linii
# dataclass (ponizej): ~15 linii
#
from dataclasses import dataclass

@dataclass
class MotorcycleDC:
    brand: str
    model: str
    year: int
    engine_cc: int
    
    @property
    def age(self) -> int:
        return 2026 - self.year
    
    @engine_cc.setter
    def engine_cc(self, value: int):
        if value <= 0:
            raise ValueError("Engine CC must be positive")
        self._engine_cc = value
    
    def specs(self) -> str:
        return f"{self.brand} {self.model} ({self.year}), {self.engine_cc}cc, {self.age} lat"
    
#
# Co @dataclass robi za Ciebie:
# - __init__ (automatycznie)
# - __repr__ (printowanie)
# - __eq__ (porownywanie)
#
# Co MUSISZ sam:
# - property (age)
# - walidacja (engine_cc setter)
# - metody (specs)