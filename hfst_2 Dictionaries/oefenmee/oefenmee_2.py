# Start de oefen mee met onderstaande dictionary.
fruitmand = { # Sleutel is fruit, waarde is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}
# Print de dictionary-waarde gekoppeld aan onderstaande variabele
fruitmand["mango"] =1

fruitmand["banaan"] =8


fruitmand["kers"] =fruitmand["kers"]-43
print(fruitmand)
fruitmand.pop("kers")
print(fruitmand)
