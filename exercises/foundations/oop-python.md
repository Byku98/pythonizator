# OOP w Pythonie — jak to dziala od srodka

## Problem: "Czemu self, czemu __init__, czemu property?"

Spokojnie, narysuje Ci to. Jak schemat blokowy w Visio, tylko bez Visio.

---

## 1. Klasa to przepis, obiekt to ciasto

```
┌─────────────────────────────────────────────────────────┐
│                    CLASS (przepis)                       │
│                                                         │
│   class Person:                                         │
│       def __init__(self, name):                         │
│           self.name = name                              │
│                                                         │
│       @property                                         │
│       def name(self):                                   │
│           return self._name                             │
│                                                         │
│       @name.setter                                      │
│       def name(self, value):                            │
│           self._name = value                            │
└─────────────────────────────────────────────────────────┘
                          │
                          │ Tworzysz obiekt
                          ▼
┌─────────────────────────────────────────────────────────┐
│                    OBJECT (ciasto)                       │
│                                                         │
│   p = Person("Kowalski")                                │
│                                                         │
│   p ──────► { name: "Kowalski" }                        │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## 2. Co sie dzieje krok po kroku

```
Krok 1: Tworzysz obiekt
──────────────────────────────────────────────────────────

    p = Person("Kowalski")
        │
        ▼
    Python szuka __init__
        │
        ▼
    ┌───────────────────────────────┐
    │   def __init__(self, name):   │
    │       self.name = name        │
    └───────────────────────────────┘
        │
        ▼
    self = p (obiekt ktory wlasnie tworzysz)
    name = "Kowalski" (argument)
        │
        ▼
    p.name = "Kowalski" (zapisuje w obiekcie)


Krok 2: Odczytujesz wartosc
──────────────────────────────────────────────────────────

    print(p.name)
        │
        ▼
    Python szuka atrybutu 'name' w obiekcie p
        │
        ▼
    Znalazl @property → wywola metode name()
        │
        ▼
    ┌───────────────────────────────┐
    │   @property                   │
    │   def name(self):             │
    │       return self._name       │
    └───────────────────────────────┘
        │
        ▼
    Zwraca "Kowalski"


Krok 3: Zmieniasz wartosc
──────────────────────────────────────────────────────────

    p.name = "Nowak"
        │
        ▼
    Python widzi @name.setter → wywola metode name(value)
        │
        ▼
    ┌───────────────────────────────┐
    │   @name.setter                │
    │   def name(self, value):      │
    │       self._name = value      │
    └───────────────────────────────┘
        │
        ▼
    p._name = "Nowak"
```

---

## 3. Dlaczego self?

```
Bez self:
──────────────────────────────────────────────────────────

    class Person:
        def __init__(name):
            self.name = name    # BLAD! Skad Python wie
                                # ktory obiekt ma ustawic?

Z self:
──────────────────────────────────────────────────────────

    class Person:
        def __init__(self, name):
            self.name = name    # OK! self = obiekt
                                # ktory wlasnie tworzysz

    p = Person("Kowalski")
        │
        ▼
    Python wywola: Person.__init__(p, "Kowalski")
        │
        ▼
    self = p, name = "Kowalski"
        │
        ▼
    p.name = "Kowalski"
```

**Analogia:** Self to jak "ja" w zdaniu. "Ja jestem Kowalski" — bez "ja" nie wiadomo kto mowi. W Pythonie bez self nie wiadomo ktory obiekt ma dostac atrybut.

---

## 4. Dlaczego __init__?

```
Bez __init__:
──────────────────────────────────────────────────────────

    class Person:
        pass

    p = Person()
    p.name = "Kowalski"     # Działa, ale musisz recznie
    p.age = 30              # ustawic kazdy atrybut

Z __init__:
──────────────────────────────────────────────────────────

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    p = Person("Kowalski", 30)  # Wszystko od razu
```

**Analogia:** __init__ to jak konstruktor w Javie. Wywola sie automatycznie jak tworzysz obiekt. Bez niego musisz recznie ustawiac kazdy atrybut.

---

## 5. Dlaczego property?

```
Bez property (bezposredni dostep):
──────────────────────────────────────────────────────────

    class Person:
        def __init__(self, name):
            self.name = name

    p = Person("Kowalski")
    print(p.name)           # "Kowalski"
    p.name = ""             # Pusty string! Brak walidacji!
    p.name = 123            # Liczba! Brak type check!

Z property (kontrolowany dostep):
──────────────────────────────────────────────────────────

    class Person:
        def __init__(self, name):
            self._name = name   # zapisujemy z podkreślnikiem
        
        @property
        def name(self):
            return self._name   # odczyt
        
        @name.setter
        def name(self, value):
            if not value:       # walidacja!
                raise ValueError("Name cannot be empty")
            self._name = value  # zapis

    p = Person("Kowalski")
    print(p.name)           # "Kowalski"
    p.name = ""             # ValueError!
    p.name = 123            # TypeError (jak dodasz type check)
```

**Analogia:** Property to jak drzwi z zamkiem. Bez property — otwarte drzwi, kazdy moze wejsc i zrobic co chce. Z property — kontrolujesz kto wchodzi i co moze zrobic.

---

## 6. Caly flow — od deklaracji do uzycia

```
┌─────────────────────────────────────────────────────────────┐
│  DEKLARACJA KLASY                                           │
│                                                             │
│  class Person:                                              │
│      def __init__(self, name):      # Konstruktor           │
│          self._name = name          # Zapisz w obiekcie     │
│                                                             │
│      @property                                             │
│      def name(self):                # Getter               │
│          return self._name                                 │
│                                                             │
│      @name.setter                                          │
│      def name(self, value):         # Setter               │
│          self._name = value                                │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ Tworzysz obiekt
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  __init__ (konstruktor)                                     │
│                                                             │
│  p = Person("Kowalski")                                     │
│       │                                                     │
│       ▼                                                     │
│  self = p, name = "Kowalski"                                │
│       │                                                     │
│       ▼                                                     │
│  self._name = "Kowalski"    # Zapisuje w obiekcie           │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ Odczytujesz
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  @property (getter)                                         │
│                                                             │
│  print(p.name)                                              │
│       │                                                     │
│       ▼                                                     │
│  Python widzi @property → wywola name()                     │
│       │                                                     │
│       ▼                                                     │
│  return self._name → "Kowalski"                             │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ Zmieniasz
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  @name.setter (setter)                                      │
│                                                             │
│  p.name = "Nowak"                                           │
│       │                                                     │
│       ▼                                                     │
│  Python widzi @name.setter → wywola name("Nowak")           │
│       │                                                     │
│       ▼                                                     │
│  self._name = "Nowak"                                       │
└─────────────────────────────────────────────────────────────┘
```

---

## 7. Kiedy uzywac property?

```
NIE uzywaj property jesli:
──────────────────────────────────────────────────────────
- Atrybut jest prosty (name, age)
- Nie potrzebujesz walidacji
- Nie potrzebujesz obliczen

class Person:
    def __init__(self, name, age):
        self.name = name    # OK, bez property
        self.age = age      # OK, bez property


UZYWAJ property jesli:
──────────────────────────────────────────────────────────
- Chcesz walidowac dane
- Chcesz obliczac wartosc w locie
- Chcesz kontrolowac dostep

class Person:
    def __init__(self, birth_year):
        self._birth_year = birth_year
    
    @property
    def age(self):              # Obliczana wartosc
        return 2026 - self._birth_year
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name required")
        self._name = value
```

---

## 8. Podsumowanie — jednym zdaniem

```
__init__  = "Ustaw poczatkowe wartosci"
self      = "To ja, ten obiekt"
property  = "Kontrolowany dostep do atrybutu"
```

Teraz lepiej? Jak tak — to lecimy z zadaniem praktycznym.