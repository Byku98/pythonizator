# Zadanie 03: Funkcje, Type Hints, Context Managers
#
# Modul 1 — Python dla ludzi z Javy
#
# === ETAP 1: Type Hints ===
# Python nie ma static typing, ale ma "etykiety na pudelkach".
#
# === ETAP 2: *args i **kwargs ===
# Brak overloading w Pythonie. Jest cos lepszego.
#
# === ETAP 3: Context Manager ===
# try-with-resources po Pythonowemu.


# ==========================================
# ETAP 1: Type Hints
# ==========================================
#
# W Javie:
#   String name = "Kowalski";
#   int age = 30;
#
# W Pythonie:
#   name: str = "Kowalski"
#   age: int = 30
#
# Type hints sa OPCJONALNE. Python ich nie sprawdza w runtime.
# Ale IDE i linter (mypy) je czytaja i ostrzegaja o bledach.
#
# Wazne typy z modulu typing:
#
#   List[int]       → lista intow (od Python 3.9: list[int])
#   Dict[str, int]  → slownik string->int (od 3.9: dict[str, int])
#   Optional[str]   → str lub None (to samo co Union[str, None])
#   Union[int, str]  → int lub str
#   Tuple[int, ...]  → krotka intow
#   Any             → cokolwiek (uzywaj ostroznie)


# --- Przyklad ---

from typing import Optional, List


def greet(name: str, age: int = 0) -> str:
    """Zwraca powitanie. age jest opcjonalne."""
    if age:
        return f"Czesc {name}, masz {age} lat"
    return f"Czesc {name}"


def find_user(users: List[str], name: str) -> Optional[str]:
    """Szuka uzytkownika w liscie. Zwraca None jak nie znajdzie."""
    for user in users:
        if user == name:
            return user
    return None


# --- Zadanie ETAP 1 ---
#
# Napisz funkcje calculate_bmi:
# - Argumenty: weight_kg: float, height_m: float
# - Zwraca: float (BMI = weight / height^2)
# - Type hint na wszystkim
#
# Napisz funkcje get_bmi_category:
# - Argument: bmi: float
# - Zwraca: str ("niedowaga", "norma", "nadwaga", "otylosc")
# - BMI < 18.5 → "niedowaga"
# - BMI 18.5-24.9 → "norma"
# - BMI 25-29.9 → "nadwaga"
# - BMI >= 30 → "otylosc"


# Twoj kod tutaj:


# --- Test ETAP 1 ---
# bmi = calculate_bmi(75, 1.80)
# print(f"BMI: {bmi:.1f}")                    # 23.1
# print(f"Kategoria: {get_bmi_category(bmi)}")  # "norma"
#
# bmi2 = calculate_bmi(100, 1.70)
# print(f"BMI: {bmi2:.1f}")                    # 34.6
# print(f"Kategoria: {get_bmi_category(bmi2)}")  # "otylosc"


# ==========================================
# ETAP 2: *args i **kwargs
# ==========================================
#
# W Javie masz overloading:
#   void greet(String name) { ... }
#   void greet(String name, int age) { ... }
#
# W Pythonie NIE ma overloading. Jest cos prostszego:
#
#   *args   → dowolna liczba argumentow pozycyjnych (tuple)
#   **kwargs → dowolna liczba argumentow nazwanych (dict)
#
# --- Analogia ---
#
# *args to jak plecak:
#   - "Wrzuc co chcesz, nie wiem ile bedzie"
#   - greet("Kowalski", "Nowak", "Wiśniewski")
#   - args = ("Kowalski", "Nowak", "Wiśniewski")
#
# **kwargs to jak walizka z etykietami:
#   - "Wrzuc co chcesz, ale kazda rzecz ma miec etykiete"
#   - greet(name="Kowalski", age=30)
#   - kwargs = {"name": "Kowalski", "age": 30}


# --- Przyklad ---

def sum_all(*args: int) -> int:
    """Sumuje dowolna liczbe intow."""
    return sum(args)


def print_info(**kwargs) -> None:
    """Wypisuje wszystkie argumenty nazwane."""
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


def create_person(name: str, *hobbies: str, **extra) -> dict:
    """Tworzy slownik z danymi osoby."""
    return {
        "name": name,
        "hobbies": list(hobbies),
        "extra": extra
    }


# --- Zadanie ETAP 2 ---
#
# Napisz funkcje build_url:
# - Argument: base_url: str (np. "https://example.com")
# - *args: sciezki (np. "api", "users", "123")
# - **kwargs: parametry query (np. page=1, limit=10)
# - Zwraca: pelny URL jako string
#
# Przyklad:
#   build_url("https://example.com", "api", "users", page=1, limit=10)
#   → "https://example.com/api/users?page=1&limit=10"
#
# Wskazowki:
# - "/".join(laczycie sciezki)
# - "&".join(f"{k}={v}" for k, v in kwargs.items())
# - Jesli kwargs nie jest puste, dodaj "?" przed parametrami


# Twoj kod tutaj:


# --- Test ETAP 2 ---
# print(sum_all(1, 2, 3, 4, 5))              # 15
# print_info(name="Kowalski", age=30, city="Warszawa")
#
# url1 = build_url("https://example.com", "api", "users", page=1, limit=10)
# print(url1)  # "https://example.com/api/users?page=1&limit=10"
#
# url2 = build_url("https://example.com", "api", "health")
# print(url2)  # "https://example.com/api/health"
#
# person = create_person("Kowalski", "motocykle", "programowanie", age=30, city="Warszawa")
# print(person)


# ==========================================
# ETAP 3: Context Manager
# ==========================================
#
# W Javie:
#   try (BufferedReader br = new BufferedReader(new FileReader("file.txt"))) {
#       String line;
#       while ((line = br.readLine()) != null) {
#           System.out.println(line);
#       }
#   }
#
# W Pythonie:
#   with open("file.txt") as f:
#       for line in f:
#           print(line)
#
# "with" = "otworz, uzyj, zamknij — nawet jesli bedzie blad"
#
# --- Analogia ---
#
# Context manager to jak wynajem pokoju:
#   1. Wchodzisz (.__enter__)
#   2. Robisz co chcesz
#   3. Wychodzisz (.__exit__) — sprzataja za Ciebie
#
# Bez context managera musisz sam sprzatac:
#   f = open("file.txt")
#   try:
#       ...
#   finally:
#       f.close()  # zamykasz recznie


# --- Przyklad: wlasny context manager ---

class Timer:
    """Mierzy czas wykonania bloku kodu."""
    
    def __enter__(self):
        import time
        self.start = time.time()
        return self  # "self" jest dostepny jako "t" w "with Timer() as t"
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.elapsed = time.time() - self.start
        print(f"Czas: {self.elapsed:.4f}s")
        return False  # nie obslugujemy wyjatkow


# --- Przyklad uzycia ---
# with Timer() as t:
#     total = sum(range(1_000_000))
# print(f"Wynik: {total}, czas: {t.elapsed:.4f}s")


# --- Zadanie ETAP 3 ---
#
# Napisz context manager DatabaseConnection:
# - __enter__: drukuje "Laczenie z baza...", zwraca self
# - __exit__: drukuje "Zamykanie polaczenia"
# - __init__ przyjmuje connection_string: str
# - ma metode query(sql: str) ktora drukuje f"Wykonuje: {sql}"
#
# Uzycie:
#   with DatabaseConnection("postgresql://localhost/mydb") as db:
#       db.query("SELECT * FROM users")
#       db.query("SELECT * FROM orders")
#
# Oczekiwany output:
#   "Laczenie z baza: postgresql://localhost/mydb..."
#   "Wykonuje: SELECT * FROM users"
#   "Wykonuje: SELECT * FROM orders"
#   "Zamykanie polaczenia"


# Twoj kod tutaj:


# --- Test ETAP 3 ---
# with DatabaseConnection("postgresql://localhost/mydb") as db:
#     db.query("SELECT * FROM users")
#     db.query("SELECT * FROM orders")


# ==========================================
# FINALNY TEST
# ==========================================

if __name__ == "__main__":
    print("=== ETAP 1: Type Hints ===")
    bmi = calculate_bmi(75, 1.80)
    print(f"BMI: {bmi:.1f}")
    print(f"Kategoria: {get_bmi_category(bmi)}")
    
    bmi2 = calculate_bmi(100, 1.70)
    print(f"BMI: {bmi2:.1f}")
    print(f"Kategoria: {get_bmi_category(bmi2)}")
    
    print("\n=== ETAP 2: *args **kwargs ===")
    print(f"sum_all(1,2,3,4,5) = {sum_all(1, 2, 3, 4, 5)}")
    
    url1 = build_url("https://example.com", "api", "users", page=1, limit=10)
    print(f"URL: {url1}")
    
    url2 = build_url("https://example.com", "api", "health")
    print(f"URL: {url2}")
    
    person = create_person("Kowalski", "motocykle", "programowanie", age=30)
    print(f"Person: {person}")
    
    print("\n=== ETAP 3: Context Manager ===")
    with DatabaseConnection("postgresql://localhost/mydb") as db:
        db.query("SELECT * FROM users")
        db.query("SELECT * FROM orders")