def palindroom(woord: str) -> bool:
    woord = woord.lower()
    return woord == woord[::-1]


def palindroom_zin(zin: str) -> bool:
    zin = zin.lower()
    zin = zin.replace(" ", "")
    for ch in [",", ".", "!", "?", ";", ":"]:
        zin = zin.replace(ch, "")
    return zin == zin[::-1]


words = ['radar', 'fiets', 'lepel', 'python']
resultaten = {w: palindroom(w) for w in words}
print(resultaten)

zin1 = "Dit is een testzin om te testen of dit programma werkt"
print(palindroom_zin(zin1))

zin2 = "Eva can I see bees in a cave"
print(palindroom_zin(zin2))