
# Poziomy logowania
DEBUG = 10
INFO = 20
WARNING = 30
ERROR = 40
LEVEL_NAMES = {
    DEBUG: "DEBUG",
    INFO: "INFO",
    WARNING: "WARNING",
    ERROR: "ERROR"
}

# Aktualny poziom (można zmieniać)
current_level = DEBUG

def set_level(level: int) -> None:
    """Ustawia minimalny poziom logowania"""
    global current_level
    current_level = level

def log(level: int, message: str) -> None:
    if level >= current_level:
        print(f"{LEVEL_NAMES[level]} {message}")

def debug(message: str) -> None:
    """Loguje na poziomie DEBUG"""
    log(DEBUG, message)

def info(message: str) -> None:
    """Loguje na poziomie INFO"""
    log(INFO, message)  

def warning(message: str) -> None:
    """Loguje na poziomie WARNING"""
    log(WARNING, message)

def error(message: str) -> None:
    """Loguje na poziomie ERROR"""
    log(ERROR, message)