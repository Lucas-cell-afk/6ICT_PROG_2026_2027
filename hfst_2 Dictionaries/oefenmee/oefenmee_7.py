# Start de oefen mee met onderstaande dictionary. 
gasten = { # Sleutel is naam, waarde is job.
    "Jan":     "reporter",
    "Piet":    "acteur",
    "Joris":   "regisseur",
    "Korneel": "scenarist"
}
while True:

    naam = input("wat is de naam van de gast: ")
    if naam in gasten:
        print(f"welkom {gasten[naam]} {naam}")
        gasten.pop(naam)
        
        
    elif naam=="stop":
        break
    else:
        print(f"{naam} staat niet op de lijst")