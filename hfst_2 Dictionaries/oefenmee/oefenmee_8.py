# Start de oefen mee met onderstaande dictionary.
steden_temp = { # Sleutel is stad, waarde is temp 
    "Hasselt": 25,
    "Oostende": 21,
    "Antwerpen": 24,
    "Brussel": 23,
    "Luik": 23,
    "Namen": 24
}
vraag=input("welke stad bent u: ")
if vraag not in steden_temp:
    print("geef een goede stad")
else:

    temp=steden_temp.get(vraag)
    print(f"in {vraag} is het {temp}")