def gemiddelde(grades):
    if not grades:
        return 0
    return sum(grades.values()) / len(grades)

grades = {"Java": 7, "Python": 8, "C#": 6, "HTML": 9, "CSS": 8}
gemiddelde = gemiddelde(grades)
print(gemiddelde)