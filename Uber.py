diensten = { "Uber Black": 2.00, "Uber Van": 3.50, "Uber X": 1.50 }

# menu
print("\033[4mOnze diensten\033[0m")
for i, dienst in enumerate(diensten.keys(), start=1):
    print(f"#{i} \"{dienst}\"")

# keuze gebruiker
while True:
    keuze = int(input("\nMaak uw keuze (1-3): "))
    if 1 <= keuze <= 3:
        selectie_dienst = list(diensten.keys())[keuze - 1]
        break
    else:
            print("Ongeldige invoer, probeer opnieuw")

# afstand en kostenberekening
prijs_per_km = diensten[selectie_dienst]
km = float(input("Aantal kilometers: "))
reiskosten = km * prijs_per_km

# output
print(f"\nGeselecteerde dienst - {selectie_dienst}\nAfstand - {km} kilometer")
print(f"\nTotale kosten: €{reiskosten:.2f}")