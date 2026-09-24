# Start de oefen mee met onderstaande dictionary.
recept = { # Sleutel is ingredi?nt, waarde is hoeveelheid
    "Aardappelen": 800,
    "Wortelen": 500,
    "erwten": 300,
    "Worsten": 400
}
vraag=int(input("voor hoeveel man kook je: "))
print("het recept voor wortelen en erwten")
for ingrediënt, hoeveelheid in recept.items():
    hoeveelheid=hoeveelheid/4 * vraag
    print(f"{ingrediënt} {hoeveelheid}")