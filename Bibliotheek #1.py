from operator import itemgetter

groep1 = ["Harry Potter", "De Hobbit", "De Da Vinci Code", "De Hobbit", "De Da Vinci Code", "Twilight", "De Vijfde Golf", "Harry Potter", "De Hobbit"]
groep2 = ["De Da Vinci Code", "De Alchemist", "Harry Potter", "De Hobbit", "Twilight", "The Hunger Games", "Gone Girl", "Twilight", "De Hobbit"]

#Vraag 1
set1 = set(groep1)
set2 = set(groep2)

print(groep1)
print(groep2)

intersection = set1.intersection(set2)

print(intersection)

#Vraag 2
union = set1.union(set2)
print(union)

#Vraag 3
print()
boek1 = set1.difference(set2)
boek2 = set2.difference(set1)

print("Boeken alleen geleend door groep 1: ", ", ".join(boek1))
print("Boeken alleen geleend door groep 2: ", ", ".join(boek2))

#Vraag 4
bieb1 = {}
for boek in groep1:
    if boek in bieb1:
        bieb1[boek] += 1
    else:
        bieb1[boek] = 1

print("\nAantal keer geleend door groep 1: ")
print(bieb1)

bieb2 = {}
for boek in groep2:
    if boek in bieb2:
        bieb2[boek] += 1
    else:
        bieb2[boek] = 1

print("\nAantal keer geleend door groep 1: ")
print(bieb2)

#Vraag 5
while True:
    boekenlijst_sorteren = input("\nResultaten sorteren? (ja/nee) ").lower()
    print()
    if boekenlijst_sorteren == "ja":
        lijst_gesorteerd1 = sorted(bieb1.items(), key=itemgetter(1), reverse=True)
        lijst_gesorteerd2 = sorted(bieb2.items(), key=itemgetter(1), reverse=True)
    # Even voor de leesbaarheid...
        print("\033[4mLijst gesorteerd van Groep 1\033[0m:")
        for boek, geleend in lijst_gesorteerd1:
            print(f"\"{boek}\" - {geleend} keer uitgeleend")
        print("\033[4mLijst gesorteerd van Groep 2\033[0m:")
        for boek, geleend in lijst_gesorteerd2:
            print(f"\"{boek}\" - {geleend} keer uitgeleend")
        break
    elif boekenlijst_sorteren == "nee":
        break
    else:
        print("Ongeldige invoer")