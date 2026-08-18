raw_data = [
    "Ducati Panigale V4;350;18.5",
    "Yamaha YZF-R1;280;14.2",
    "Honda CBR1000RR;420;19.8",
    "Kawasaki ZX-10R;broken;data",      # błąd! tekst zamiast liczby
    "BMW S1000RR;310;-5",               # błąd! ujemne paliwo
    "Suzuki GSX-R1000",                  # błąd! za mało pól
    "Triumph Street Triple;200;9.5",
]

def calculate_consumption(distance_km: float, fuel_liters: float) -> float:
    """Oblicza spalanie w L/100km"""
    return (fuel_liters / distance_km) * 100

def parse_fuel_data(raw_data: list[str]) -> list[dict]:
    wynik = []
    
    for line in raw_data:
        pole = line.split(";")
        
        # Krok 1: sprawdź długość
        if len(pole) != 3:
            print(f"⚠️  Błąd: zbyt mało pól w linii: {line}")
            continue
        
        # Krok 2: konwersja z try/except
        try:
            dystans = float(pole[1])
            paliwo = float(pole[2])
        except ValueError:
            print(f"⚠️  Błąd: nieprawidłowy format liczbowy w linii: {line}")
            continue
        
        # Krok 3: walidacja wartości
        if dystans <= 0 or paliwo < 0:
            print(f"⚠️  Błąd: nieprawidłowe wartości w linii: {line}")
            continue
        
        # Krok 4: dodaj do wyników
        wynik.append({
            "marka": pole[0],
            "dystans_km": dystans,
            "paliwo": paliwo
        })
    
    return wynik

def find_most_efficient(motocykle: list[dict]) -> dict:
    """Znajduje najoszczędniejszy motocykl"""
    return min(motocykle, key=lambda x: calculate_consumption(x["dystans_km"], x["paliwo"]))

if __name__ == "__main__":
    # Parsowanie danych
    motocykle = parse_fuel_data(raw_data)
    print(f"Znaleziono {len(motocykle)} motocykli. Oto one: {motocykle}")
    print(f"Najoszczędniejszy motocykl: {find_most_efficient(motocykle)}")
    