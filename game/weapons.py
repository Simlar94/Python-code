"""
Dina funktioner innehåller onödig kod.
Istället för att skapa listor och sedan göra slices av dessa, så skulle du kunna returnera strängarna direkt.
Se nedan i exempel def sword().

Ett annat alternativ är ju att skapa weaponlist globalt i scriptet (som då innehåller alla vapen).
Sedan, i varje funktion kan man returnera specikfikt vapen på ett specifikt index.
Se exempel sist i den här filen.
"""


def dagger():
    weaponlist = ["dagger"]
    givenweapon = weaponlist[:1]
    return givenweapon[0]


def stick():
    weaponlist = ["stick"]
    givenweapon = weaponlist[:1]
    return givenweapon[0]


def axe():
    weaponlist = ["axe"]
    givenweapon = weaponlist[:1]
    return givenweapon[0]

def sword():
    return "sword"

weapons = ["shotgun", "sword", "cannon"]
def getWeapon(index):
    return weapons[index]
