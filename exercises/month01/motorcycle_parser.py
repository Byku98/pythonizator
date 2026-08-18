# --- Dane ---
raw_data = """
Ducati;Panigale V4;1198;214;89999
Yamaha;YZF-R1;998;200;72999
Honda;CBR1000RR;1000;189;64999
Kawasaki;ZX-10R;998;203;67999
BMW;S1000RR;999;205;74999
"""

def parse_motorcycle_data(raw_data: str) -> list[dict]:
    
    motorcycle_list = raw_data.strip().split("\n")
    for i in range(len(motorcycle_list)):
        motorcycle_list[i] = motorcycle_list[i].split(";")
        motorcycle_list[i] = {
            "Marka": str(motorcycle_list[i][0]),
            "Model": str(motorcycle_list[i][1]),
            "Pojemność": int(motorcycle_list[i][2]),
            "Prędkość maksymalna": int(motorcycle_list[i][3]),
            "Cena": int(motorcycle_list[i][4])
        }
        
    return motorcycle_list
    
def find_fastest(motorcycles: list[dict]) -> dict:
    
    fastest_motorcycle = motorcycles[0]
    for motorcycle in motorcycles:
        if motorcycle["Prędkość maksymalna"] > fastest_motorcycle["Prędkość maksymalna"]:
            fastest_motorcycle = motorcycle
    
    return fastest_motorcycle

def average_price(motorcycles: list[dict]) -> float:

    total_price = 0
    for motorcycle in motorcycles:
        total_price += motorcycle["Cena"]    
    
    return total_price / len(motorcycles)
    
if __name__ == "__main__":
    motorcycles = parse_motorcycle_data(raw_data)
    print(f"Znaleziono {len(motorcycles)} motocykli.")
    print(f"Najszybszy motocykl: {find_fastest(motorcycles)}")
    print(f"Średnia cena motocykli: {average_price(motorcycles):.2f} PLN")