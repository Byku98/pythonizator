# Pythonizator — Postępy w nauce

## Cel: Python Developer (mid) — rozmowa za ~1 rok
**Profil:** 10+ lat w IT (integracja, firewalle, K8s, DB, Linux, Windows, AD)
**Background:** Java (Spring, Hibernate, modyfikatory), podstawy React
**Cel:** Zmienic prace z integratora na Python Developera
**Podejscie:** Uczymy sie czytac, rozumiec i oceniac kod. Nie klepamy tutoriali.
**Czas:** 2-3h tygodniowo
**Projekt:** Wireshark dla GenZ (TS + Python) — pisany z AI

---

## Modul 1: Python dla ludzi z Javy

**Cel:** Przelozyc Java-owe koncepty na Pythona. Krotko, na temat.

- [x] Skladnia: co jest inaczej niz w Javie
- [x] Kolekcje: listy, dicty, sety (inne niz w Javie)
- [x] OOP: self, brak private/public, property ✅ (zadanie 01 + 02)
- [x] @staticmethod, @classmethod, dataclass ✅ (zadanie 02)
- [ ] Typy, Funkcje, Context Managers ← W TRAKCIE (zadanie 03)
- [x] Comprehensions: Pythonowy flex
- [x] Context managers: try-with-resources po Pythonowemu
- [ ] Moduly: import, __init__.py, pip

**Status:** 🔄 W trakcie

---

## Modul 2: Async + FastAPI

**Cel:** Rozumiec jak dziala Pythonowy async i glowny framework backendowy.

- [ ] asyncio: event loop, async/await, Task
- [ ] FastAPI: routing, DI, middleware, Pydantic
- [ ] SQLAlchemy: ORM, relacje, migracje
- [ ] Uwierzytelnianie: JWT, OAuth2

**Status:** ⏳ Nie zaczety

---

## Modul 3: Testy + Review kodu AI

**Cel:** Moc ocenic czy AI dobrze wygenerowal kod. Umiec napisac testy.

- [ ] pytest: fixtures, parametrize, mock
- [ ] Ocena kodu AI: co sprawdzac, antywzorce
- [ ] Code review checklist

**Status:** ⏳ Nie zaczety

---

## Modul 4: Twoj projekt — Wireshark dla GenZ

**Cel:** Dociagnac projekt, rozumiec architektur, moc go zaprezentowac.

- [ ] Przeglad obecnego stanu projektu
- [ ] Refaktor: co poprawic
- [ ] Architektura: co i dlaczego
- [ ] Deploy: Docker, CI/CD

**Status:** ⏳ Nie zaczety

---

## Modul 5: Rozmowa kwalifikacyjna

**Cel:** Przejsc rozmowe na mida. Wiedziec co powiedziec, czego nie mowic.

- [ ] Pytania techniczne: Python, FastAPI, OOP, async
- [ ] System design: jak projektowac API
- [ ] Behavioral: co powiedziec o swoim doswiadczeniu
- [ ] Mock interviews

**Status:** ⏳ Nie zaczety

---

## Co juz umiem (z poprzedniego planu)

- [x] Podstawy Pythona: zmienne, typy, operatory
- [x] Kolekcje: listy, krotki, slowniki, zbiory
- [x] Kontrola przeplywu: if/elif/else, for, while
- [x] Funkcje: argumenty, *args, **kwargs
- [x] Comprehensions: list, dict, set
- [x] Obsluga bledow: try/except/finally
- [x] Moduly i pakiety: import, __init__.py, pip
- [x] Praca z plikami: open, context managers

---

## Notatki z sesji

### Sesja 2 — 2026-09-28

**Co zrobilismy:**
- Poprawiono zadanie 01-motorcycle.py (5 bledow)
- Dodano zadanie 02-motorcycle-advanced.py (@staticmethod, @classmethod, @dataclass)
- Dodano zadanie 03-functions-types-context.py (type hints, *args/**kwargs, context managers)

**Co uzytkownik rozumie:**
- self, __init__, @property, @setter
- _underscore = konwencja "prywatnego" pola
- @staticmethod vs @classmethod (kiedy co)
- Dlaczego from_string() to classmethod (jajko i kura)
- _count = zmienna klasy (shared między instancjami)

**Do poprawy (zrobione):**
- ✅ from_string() — dodano int() na engine_cc (linia 128)
- ✅ Unicode error na → w print() — zamieniono na -> 

---

### Sesja 3 — 2026-09-28

**Co zrobilismy:**
- Zadanie 02 zakonczone (int() fix, unicode fix)
- Zadanie 03 wytlumaczone i gotowe do zrobienia

**Co uzytkownik rozumie:**
- @staticmethod vs @classmethod (jajko i kura)
- _underscore = konwencja prywatnosci
- Dlaczego from_string to classmethod

**Do zrobienia:**
- Zadanie 03: calculate_bmi, build_url, DatabaseConnection
- Nastepna sesja: Moduly (import, __init__.py, pip)

---

## Do zrobienia przed nastepna sesja

### Zadanie 03 — gotowe do zrobienia:
1. ETAP 1: `calculate_bmi()` + `get_bmi_category()` — type hints
2. ETAP 2: `build_url()` — *args, **kwargs
3. ETAP 3: `DatabaseConnection` — context manager (__enter__, __exit__)

### Nastepna sesja:
- Moduly: import, __init__.py, pip
- Przejscie do Modulu 2: Async + FastAPI