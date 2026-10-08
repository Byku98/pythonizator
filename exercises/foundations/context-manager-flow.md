# Context Manager — jak self przeplywa przez __enter__ i __exit__

## Problem: "Skad sie bierze 'db' w 'with ... as db'?"

To jest jak pytanie: "Skad kelner wie ktory stolik obsluguje?"
Odpowiedz: Sam sie przedstawia.

---

## Rysunek 1: Caly flow krok po kroku

```
    with DatabaseConnection("postgres://localhost/mydb") as db:
         |                         |                        |
         |                         |                        |
         ▼                         ▼                        ▼
    ┌─────────────────────────────────────────────────────────────┐
    │  Krok 1: Tworzysz obiekt                                    │
    │                                                             │
    │  conn = DatabaseConnection("postgres://localhost/mydb")     │
    │                                                             │
    │  conn = { conn_str: "postgres://localhost/mydb" }           │
    └─────────────────────────────────────────────────────────────┘
                                │
                                ▼
    ┌─────────────────────────────────────────────────────────────┐
    │  Krok 2: Python wywola __enter__                            │
    │                                                             │
    │  conn.__enter__()                                           │
    │      │                                                      │
    │      ▼                                                      │
    │  def __enter__(self):      # self = conn                    │
    │      print("Laczenie...")                                   │
    │      return self            # zwraca siebie!                │
    │      │                                                      │
    │      ▼                                                      │
    │  return conn               # to idzie do "db"               │
    └─────────────────────────────────────────────────────────────┘
                                │
                                ▼
    ┌─────────────────────────────────────────────────────────────┐
    │  Krok 3: db = conn                                          │
    │                                                             │
    │  with DatabaseConnection(...) as db:                        │
    │                               │                             │
    │                               ▼                             │
    │                          db = conn (ten sam obiekt!)         │
    │                                                             │
    │  Teraz mozesz uzywac:                                       │
    │    db.query("SELECT * FROM users")                          │
    │    db.query("SELECT * FROM orders")                         │
    └─────────────────────────────────────────────────────────────┘
                                │
                                ▼
    ┌─────────────────────────────────────────────────────────────┐
    │  Krok 4: Kod w srodku "with" sie wykonuje                   │
    │                                                             │
    │  with DatabaseConnection(...) as db:                        │
    │      db.query("SELECT * FROM users")    # dziala!           │
    │      db.query("SELECT * FROM orders")   # dziala!           │
    └─────────────────────────────────────────────────────────────┘
                                │
                                ▼
    ┌─────────────────────────────────────────────────────────────┐
    │  Krok 5: Python wywola __exit__ (ZAWSZE!)                   │
    │                                                             │
    │  conn.__exit__(None, None, None)   # jesli NIE bylo bledu   │
    │  lub                                                           │
    │  conn.__exit__(ExcType, ExcVal, ExcTb)  # jesli BYL blad    │
    │                                                             │
    │  def __exit__(self, exc_type, exc_val, exc_tb):             │
    │      print("Zamykanie polaczenia")                          │
    │      return False           # nie tlumie wyjatkow           │
    └─────────────────────────────────────────────────────────────┘
```

---

## Rysunek 2: Analogia z hotelem

```
    with HotelRoom("Pokoj 101") as room:
         |                         |
         |                         |
         ▼                         ▼
    ┌─────────────────────────────────────────────┐
    │  __enter__                                  │
    │  "Prosze bardzo, oto karta do pokoju 101"   │
    │  return self  →  room = self                 │
    └─────────────────────────────────────────────┘
                        │
                        ▼
    ┌─────────────────────────────────────────────┐
    │  Uzywasz pokoju                             │
    │  room.sleep()                               │
    │  room.watch_tv()                            │
    └─────────────────────────────────────────────┘
                        │
                        ▼
    ┌─────────────────────────────────────────────┐
    │  __exit__ (zawsze!)                         │
    │  "Dzien dobry, sprzatamy pokoj 101"         │
    │  Nawet jesli wyszedles w srodku nocy!       │
    └─────────────────────────────────────────────┘
```

---

## Rysunek 3: Co sie dzieje jak jest blad?

```
    with DatabaseConnection(...) as db:
        db.query("SELECT * FROM users")        # OK
        raise Exception("Cos sie wywalilo!")    # BLAD!
        db.query("SELECT * FROM orders")        # NIE WYKONA SIE

    ┌─────────────────────────────────────────────────────────────┐
    │  __exit__ I TAK sie wywola!                                 │
    │                                                             │
    │  __exit__(Exception, "Cos sie wywalilo!", traceback)        │
    │      │                                                      │
    │      ▼                                                      │
    │  print("Zamykanie polaczenia")  # zawsze sie wykona         │
    │  return False                   # nie tlumie wyjatku        │
    └─────────────────────────────────────────────────────────────┘
```

---

## Rysunek 4: self vs db — to jest TEN SAM obiekt!

```
    class DatabaseConnection:
        def __init__(self, conn_str):
            self.conn_str = conn_str          # ← self to obiekt

        def __enter__(self):
            #          ^^^^
            #          self = obiekt ktory wlasnie tworzysz
            print(f"Laczenie: {self.conn_str}")
            return self                       # ← zwraca SIEBIE

        def __exit__(self, ...):
            #         ^^^^
            #         self = ten sam obiekt co wyzej
            print("Zamykanie")


    with DatabaseConnection("postgres://...") as db:
    #                                               ^^
    #                                               db = self (ten sam!)
        db.query("...")   # to jest to samo co self.query("...")
```

```
    ┌──────────────────────────────────────────────────────┐
    │                                                      │
    │   __init__  ──►  self = {conn_str: "postgres://..."} │
    │                       │                               │
    │                       ▼                               │
    │   __enter__ ──►  self = ten sam obiekt               │
    │                       │                               │
    │                       ▼                               │
    │   return self ──►  db = ten sam obiekt               │
    │                       │                               │
    │                       ▼                               │
    │   with ... as db ──►  db.query(...) = self.query(...)</span>│
    │                       │                               │
    │                       ▼                               │
    │   __exit__  ──►  self = ten sam obiekt (zamykasz)    │
    │                                                      │
    └──────────────────────────────────────────────────────┘
```

---

## Podsumowanie jednym zdaniem:

```
__enter__  = "Otwieram zasob i zwracam SIEBIE jako 'db'"
__exit__   = "Zamykam zasob (zawsze, nawet przy bledzie)"
self       = "To ja, ten obiekt — caly czas ten sam"
```

---

## Kiedy uzywac context managera?

| Sytuacja | Uzyj `with`? |
|----------|-------------|
| Otwierasz plik | ✅ `with open(...) as f:` |
| Polaczenie z baza | ✅ `with DatabaseConnection(...) as db:` |
| Mierzysz czas | ✅ `with Timer() as t:` |
| Zwykla klasa (Motorcycle) | ❌ Nie trzeba |