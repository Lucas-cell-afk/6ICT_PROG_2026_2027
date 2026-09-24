# Start de oefen mee met onderstaande dictionary.
fruitmand = { # Sleutel is fruit, waarde is aantal
    "appels": 2,
    "bananen": 3,
    "kersen": 10,
    "mango's": 1
}
for fruit,aantal in fruitmand.items():
    vraag=int(input(f"hoveel {fruit} wilt kopen er zijn er {fruitmand[fruit]}: "))
    fruitmand[fruit]=aantal+vraag

for fruit,aantal in fruitmand.items():
    print(f"{aantal} {fruit}")