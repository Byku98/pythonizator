# Python vs Java — co jest inaczej

Ten dokument przelozyc Java-owe koncepty na Pythona. Czytaj jak cheat sheet, nie jak tutorial.

## 1. Skladnia — podstawowe roznice

### Zmienne i typy

```java
// Java: static typing, deklaracja typu
String name = "Kowalski";
int age = 30;
final double PI = 3.14; // final = const
```

```python
# Python: dynamic typing, brak deklaracji
name = "Kowalski"  # type: str (optional)
age = 30
PI = 3.14  # nie ma final, ale jest UPPER_CASE convention
```

**Wazne:** W Pythonie typ jest ustalany w runtime, nie w compile time. Nie ma `int x = 5` — jest po prostu `x = 5`.

### Konkatenacja stringow

```java
// Java: + lub String.format
String greeting = "Hello " + name;
String formatted = String.format("Hello %s, age %d", name, age);
```

```python
# Python: f-string (najczestszy sposob)
greeting = f"Hello {name}"
formatted = f"Hello {name}, age {age}"
```

### Warunki

```java
// Java: nawiasy klamrowe
if (age >= 18) {
    System.out.println("Adult");
} else if (age >= 13) {
    System.out.println("Teen");
} else {
    System.out.println("Child");
}
```

```python
# Python: wciecia (indentation)
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")
```

**Wazne:** W Pythonie nie ma nawiasow klamrowych. Wciecia SA skladnia. Nie mozesz ich pominac.

### Petle

```java
// Java: for, while, for-each
for (int i = 0; i < 10; i++) {
    System.out.println(i);
}

for (String item : items) {
    System.out.println(item);
}
```

```python
# Python: for (for-each style), while
for i in range(10):
    print(i)

for item in items:
    print(item)

# while dziala tak samo
while condition:
    do_something()
```

**Wazne:** W Pythonie `for` to zawsze for-each. Nie ma klasycznej petli `for (int i = 0; i < n; i++)`. Uzywasz `range()`.

---

## 2. Kolekcje

### Listy

```java
// Java: ArrayList
List<String> names = new ArrayList<>();
names.add("Kowalski");
names.add("Nowak");
String first = names.get(0);
```

```python
# Python: list
names = ["Kowalski", "Nowak"]
first = names[0]

# Dodawanie
names.append("Wiśniewski")

# List comprehension (Pythonowy flex)
upper_names = [name.upper() for name in names]
```

### Slowniki (Map)

```java
// Java: HashMap
Map<String, Integer> ages = new HashMap<>();
ages.put("Kowalski", 30);
int age = ages.get("Kowalski");
```

```python
# Python: dict
ages = {"Kowalski": 30}
age = ages["Kowalski"]

# Bezpieczne pobieranie
age = ages.get("Kowalski", 0)  # domyslna wartosc

# Dict comprehension
upper_ages = {k.upper(): v for k, v in ages.items()}
```

### Sety

```java
// Java: HashSet
Set<String> unique = new HashSet<>();
unique.add("a");
unique.add("a"); // duplikat, nie dodany
```

```python
# Python: set
unique = {"a", "a"}  # zostanie tylko jedno "a"
unique.add("b")
```

### Tuple (nie ma odpowiednika w Javie)

```python
# Tuple: niezmienialna lista
coordinates = (10, 20)
x, y = coordinates  # unpacking

# Czesto uzywane do zwracania wielu wartosci z funkcji
def get_coords():
    return (10, 20)

x, y = get_coords()
```

---

## 3. Funkcje

### Podstawowe roznice

```java
// Java: static typing, return type
public static int add(int a, int b) {
    return a + b;
}
```

```python
# Python: dynamic typing, brak return type
def add(a, b):
    return a + b

# Type hints (opcjonalne, od Python 3.5)
def add(a: int, b: int) -> int:
    return a + b
```

### *args i **kwargs (nie ma w Javie)

```python
# *args: dowolna liczba argumentow pozycyjnych
def greet(*args):
    for name in args:
        print(f"Hello {name}")

greet("Kowalski", "Nowak", "Wiśniewski")

# **kwargs: dowolna liczba argumentow nazwanych
def greet(**kwargs):
    for name, age in kwargs.items():
        print(f"Hello {name}, age {kwargs.get('age', 'unknown')}")

greet(Kowalski=30, Nowak=25)
```

### Domknięcia (Closures)

```python
# Funkcja wewnatrz funkcji — zamyka zmienne z otoczenia
def make_adder(x):
    def adder(y):
        return x + y
    return adder

add5 = make_adder(5)
print(add5(3))  # 8
```

---

## 4. OOP — najwieksza roznica

### Klasy i self

```java
// Java: this jest opcjonalny
public class Person {
    private String name;
    
    public Person(String name) {
        this.name = name;
    }
    
    public String getName() {
        return name;
    }
}
```

```python
# Python: self jest OBOWIAZKOWY
class Person:
    def __init__(self, name: str):
        self.name = name  # public!
    
    def get_name(self) -> str:
        return self.name

# Tworzenie obiektu
p = Person("Kowalski")
print(p.name)  # mozna bezposrednio!
```

**Wazne:** W Pythonie nie ma `private`, `public`, `protected`. Wszystko jest publiczne. Jest konwencja `_name` (protected) i `__name` (name mangling), ale to nie jest enkapsulation jak w Javie.

### Dziedziczenie

```java
// Java: extends
public class Employee extends Person {
    private String company;
    
    public Employee(String name, String company) {
        super(name);
        this.company = company;
    }
}
```

```python
# Python: ()
class Employee(Person):
    def __init__(self, name: str, company: str):
        super().__init__(name)  # lub Person.__init__(self, name)
        self.company = company
```

### Property (zamiast getterow/setterow)

```java
// Java: getter/setter
public class Person {
    private String name;
    
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}
```

```python
# Python: property
class Person:
    def __init__(self, name: str):
        self._name = name
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        self._name = value

# Uzycie
p = Person("Kowalski")
print(p.name)  # getter
p.name = "Nowak"  # setter
```

### dataclass (Python 3.7+)

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    
    # Automatycznie generuje __init__, __repr__, __eq__
    # Nie musisz pisac tego wszystkiego recznie

p = Person("Kowalski", 30)
print(p)  # Person(name='Kowalski', age=30)
```

---

## 5. Wyjatki

```java
// Java: checked exceptions
try {
    riskyOperation();
} catch (IOException e) {
    System.err.println("Error: " + e.getMessage());
} finally {
    cleanup();
}
```

```python
# Python: nie ma checked exceptions
try:
    risky_operation()
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected: {e}")
finally:
    cleanup()

# Wlasne wyjatki
class MyError(Exception):
    pass

raise MyError("Something went wrong")
```

---

## 6. Context Managers (try-with-resources)

```java
// Java: try-with-resources
try (BufferedReader br = new BufferedReader(new FileReader("file.txt"))) {
    String line;
    while ((line = br.readLine()) != null) {
        System.out.println(line);
    }
}
```

```python
# Python: with statement
with open("file.txt") as f:
    for line in f:
        print(line)

# Wlasny context manager
class MyResource:
    def __enter__(self):
        print("Opening")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing")
        return False  # nie obslugujemy wyjatkow

with MyResource() as r:
    print("Using resource")
```

---

## 7. Importy

```java
// Java: import
import java.util.List;
import java.util.ArrayList;
```

```python
# Python: import
import os
from pathlib import Path
from typing import List, Optional

# Aliasy
import numpy as np
from datetime import datetime as dt
```

---

## 8. Co NIE MA odpowiednika w Javie

1. **Comprehensions** — list, dict, set
2. **Decorators** — @decorator
3. **Generators** — yield
4. **Walrus operator** — := (Python 3.8+)
5. **f-strings** — f"Hello {name}"
6. **Unpacking** — a, b, c = [1, 2, 3]
7. ***args, **kwargs** — dowolna liczba argumentow
8. **dataclass** — automatyczne generowanie __init__
9. **Protocol** — structural typing (odpowiednik interfejsow)

---

## Co dalej

Jak przejrzysz te roznice, idz do `oop-python.md` — tam jest glebiej o OOP w Pythonie.