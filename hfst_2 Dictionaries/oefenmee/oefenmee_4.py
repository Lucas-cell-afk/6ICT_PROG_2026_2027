# Gebruik een zelfgemaakte dictionary (of onderstaande).
fruitmand = { # Sleutel is fruit, element is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}
vraag=input("welk fruit zoek je: ")
if vraag in fruitmand:  
    print(fruitmand[vraag])
else:print("fruit niet gevonden")