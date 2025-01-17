'''
Oppg 1) Du skal her lage et program som skal starter med alder = int(input('Hvilket år er du født? ') )
Programmet skal så regne ut hvor gammel personen blir nå i løpet av år 2024 og skrive svaret til skjerm med passende tekst.
'''

from datetime import datetime
current_year = datetime.now().year
birth_year = int(input("hvilket år er du fått"))
if birth_year >= current_year:
    print("invalid date")

else:
    age = current_year - birth_year
    print(f"Du blir {age} år i løpet av året {current_year}.")





'''  Oppg 2) Det skal arrangeres en klassefest og man antar at hver elev spiser 1/4 pizza. Lag et program som tar inn antall elever fra konsollen ved
antall_elever = int(input('Skriv inn antall elever:' ))
Programmet skal så regne ut hvor mange pizzaer som skal handles inn til festen og skrive svaret til skjerm. Merk, man kan ikke kjøpe 4 og en kvart pizza på butikken (man må da kjøpe 5).
Hint1: Gir programmet ditt et fornuftig svar hvis det f.eks er 21 elever i klassen?
Hint2: Det er ikke vanlig å si/skrive: ‘Det må handles inn 6.0 pizzaer til festen’. Hvordan kan sikre at antall pizzaer skrives ut som et heltall (ikke desimaltall)? '''

import math

number_of_students = int(input("Skriv inn antall eleve: "))
assumed_pizza_eachperson = .25

sum = number_of_students * assumed_pizza_eachperson
print(f" Det må handles inn {math.ceil(sum)} pizzaer til festen. ")


'''
Oppg 3) Lag et program med en funksjon som regner om fra grader til radianer. Programmet skal starte med:
import numpy as np
v_grad = float(input('Skriv inn gradtallet:' ))
Radiantallet til vinkelen regnes så ut ved følgende formel: v_rad = v_grad*np.pi/180 Resultatet v_rad skrives til skjerm med passende tekst og verdi.
Merk: np.pi er en ferdiglaget funksjon som gir verdien 3.1415....
'''
import numpy as np 

v_grad = float(input('Skriv inn gradtallet:' ))
v_rad = v_grad*np.pi/180

print (f"Radiantallet til vinkelen er:   {v_rad} " )


# oppgave 4

data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
}


land = input("skriv inn land navn vil du ha info om: ")

if land in data:
    print(f"{data[land][0]} er hovedstaden i {land} og det er {data[land][1]} mill. innbyggere {data[land][0]} ")


else:
    print ("Landet du har skrevet er ikke i lagret i Dictionaryen ")

    nyland = input ("Vil du oppdatere Dictionaryen? tast ja eller nei").strip().lower()

    if nyland == "ja":

        hovedstad = input("Skriv hovedstaden: ").strip()
        befolkning = float(input("Skriv befolkningen (i millioner): ").strip())
        data[land] = [hovedstad, befolkning]

        print("\nOppdatert Dictionary:")
        print(data)

    else:
        print ("ingen ble gjort")


# oppgave 5

import math
def beregn_areal_og_omkrets(a, b):

    r = a / 2

    halvsirkel_areal = (math.pi * r**2) / 2
    halvsirkel_omkrets = math.pi * r
    trekant_areal = (a * b) / 2

    hypotenus = math.sqrt(a**2 + b**2)
    trekant_omkrets = a + b + hypotenus

    # Totalt areal
    total_areal = halvsirkel_areal + trekant_areal

    # Ytre omkrets- linjene i figuren
    ytre_omkrets = b + hypotenus + halvsirkel_omkrets

    # Skriv ut resultatene
    print(f"Totalt Areal: {total_areal:.2f}")
    print(f"Ytre Omkrets: {ytre_omkrets:.2f}")

    return total_areal, ytre_omkrets

# Eksempelbruk
a = 10  # Grunnlinje (og diameteren til halvsirkelen)
b = 5   # Høyde
beregn_areal_og_omkrets(a, b)



# oppgave 6 
import numpy as np
import matplotlib.pyplot as plt

# Definer funksjonen f(x)
def f(x):
    return -x**2 - 5

# Lag et array med 200 punkter jevnt fordelt mellom -10 og 10
x = np.linspace(-10, 10, 200)

# Beregn f(x) for hvert punkt i x
y = f(x)

# Plot grafen
plt.plot(x, y, label="f(x) = -x² - 5", color="blue")

# Legg til tittel og akseetiketter
plt.title("Graf av f(x) = -x² - 5")
plt.xlabel("x")
plt.ylabel("f(x)")

# Legg til et rutenett for bedre lesbarhet
plt.grid(True)

# Legg til en forklaring
plt.legend()

# Vis grafen
plt.show()
