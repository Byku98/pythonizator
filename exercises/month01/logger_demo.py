from logger import debug, info, warning, error, set_level, DEBUG, INFO, ERROR, WARNING

if __name__ == "__main__":
    # Test z domyślnym poziomem (DEBUG)
    debug("To jest debug")
    info("To jest info")
    warning("To jest warning")
    error("To jest error")

    print("\n--- Zmiana poziomu na INFO ---\n")

    # Zmień poziom na INFO
    set_level(INFO)
    debug("To nie powinno się wyświetlić")
    info("To powinno się wyświetlić")
    error("To też")