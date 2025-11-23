def list_names(names):
    capitalized = [name.capitalize() for name in names]

    if len(capitalized) == 1:
        return capitalized[0]

    return ", ".join(capitalized[:-1]) + " en " + capitalized[-1]

names = []
for i in range(4):
    name = input(f"Voer naam nr. {i+1} in: ")
    names.append(name)

result = list_names(names)
print()
print(result)