bibliotheek = {
    "The Silent Patient": {
        "auteur": "Alex Michaelides",
        "genre": "Thriller",
        "publicatiejaar": 2019
    },
    "Where the Crawdads Sing": {
        "auteur": "Delia Owens",
        "genre": "Fictie",
        "publicatiejaar": 2018
    },
    "The Night Circus": {
        "auteur": "Erin Morgenstern",
        "genre": "Fantasy",
        "publicatiejaar": 2011
    },
    "Educated": {
        "auteur": "Tara Westover",
        "genre": "Memoir",
        "publicatiejaar": 2018
    },
    "Circe": {
        "auteur": "Madeline Miller",
        "genre": "Fantasy",
        "publicatiejaar": 2018
    }
}

#Je gaat een bibliotheekprogramma maken. Het programma moet de volgende functionaliteiten hebben:
#1. De gebruiker moet boeken kunnen toevoegen aan de bibliotheek. Een boek heeft de volgende eigenschappen:
#   - Naam
#   - Auteur
#   - Genre
#   - Publicatiejaar

#2. De gebruiker moet een lijst van alle boeken in de bibliotheek kunnen opvragen. De lijst moet de volgende informatie bevatten:
#   - Naam
#   - Auteur
#   - Genre
#   - Publicatiejaar

#3. De gebruiker moet een lijst van alle boeken in een bepaald genre kunnen opvragen. De gebruiker moet het genre kunnen invoeren en het programma moet alle boeken in dat genre tonen. De lijst moet de volgende informatie bevatten:
#   - Naam
#   - Auteur
#   - Publicatiejaar

#4. De gebruiker moet het programma kunnen stoppen.

#Een paar tips voor het maken van dit programma:
# Als je een keuze menu maakt, kun je een while loop gebruiken die blijft loopen totdat de gebruiker kiest om te stoppen.
# Je keuze menu is eigenlijk een if-elif-else statement. Je kunt de keuze van de gebruiker opslaan in een variabele en dan met if-elif-else bepalen wat er moet gebeuren.


#functies

print("Welkom bij de bibliotheek!")

def boek_toevoegen():
    naam = input("\nTitel: ")
    auteur = input("Auteur: ")
    genre = input("Genre: ")
    jaar = input("Jaar van uitgave: ")
    bibliotheek[naam] = { "auteur": auteur, "genre": genre, "publicatiejaar": int(jaar) }
    print(f"\"{naam}\" is aan de bibliotheek toegevoegd.")

def toon_boeken():
    print("\n\033[4mCatalogus\033[0m:")
    for naam, info in bibliotheek.items():
        print(f"\"{naam}\" - {info['auteur']} ({info['publicatiejaar']})\n\tGenre: {info['genre']}\n")

def toon_genre(genre):
    print(f"\nCategorie: {genre}")
    gevonden = False
    for naam, info in bibliotheek.items():
        if info['genre'].lower() == genre.lower():
            print(f"\"{naam}\" - {info['auteur']} ({info['publicatiejaar']})")
            gevonden = True
    if not gevonden:
        print("Geen boeken gevonden.")

# Hoofdmenu
keuze_menu = { "Boek toevoegen": 1, "Alle boeken tonen": 2, "Boeken per genre tonen": 3, "Stoppen": 4 }

while True:
    print("\n\033[4mHoofdmenu\033[0m")  # onderstreepte tekst
    for i, optie in enumerate(keuze_menu.keys(), start=1):
        print(f"{i}) {optie}")

    keuze = input("\nMaak een keuze (1-4): ")

    if keuze == "1":
        boek_toevoegen()
    elif keuze == "2":
        toon_boeken()
    elif keuze == "3":
        genre = input("Voer het genre in: ")
        toon_genre(genre)
    elif keuze == "4":
        break
    else:
        print("Ongeldige invoer, probeer opnieuw.")
