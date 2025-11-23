def woordenteller(zin):
    return len(zin.split())

invoer = input("Voer een zin in: ")
aantal = woordenteller(invoer)
print(f"Deze zin bevat {aantal} woorden.")
