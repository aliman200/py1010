"""
Arbeidsoppgave 1 
Anta at du skal kjøpe bil. Det står mellom elbil og bensinbil, og du ønsker å sammenlikne de årlige kostnadene ved elbil sammenliknet med bensinbil.
Lag et Python-program som beregner og presenterer (i konsollen) de årlige totalkostnadene for elbil og for bensinbil samt årlig kostnadsdifferanse basert på informasjonen gitt nedenfor. Du kan her for enkelhets skyld se bort fra kostnader som renter på billån og verditap (du har da egentlig antatt at slike kostnader er like for elbil og bensinbil).
Nedenfor er informasjon som programmet skal baseres på (som selvsagt kan diskuteres, men ikke ifm. denne oppgaven :-)
Du kan selv velge antall kjørte km/år ut fra din typiske bilbruk. Ev. (hvis du ikke har bil) kan du anta 10.000 km.
Forsikring: Elbil: 5000 kr/år. Bensinbil: 7500 kr/år.
Trafikkforsikringsavgift: 8,38 kr/dag for både elbil og bensinbil.
Drivstoffbruk: Elbil: 0,2 kWh/km. Strømpris (antar kun hjemmelading): 2.00 kr/kWh. Bensinbil: 1,0 kr/km.
Bomavgift: Elbil: 0,1 kr/km. Bensinbil: 0,3 kr/km.

"""

#constans
forsikring_elbil = 5000
forsikring_bensinbil = 7500
trafikkforsikringsavgift = float(8.38)
arlig_trafikkforsikringsavgift = trafikkforsikringsavgift * 365

#fuel costs
driftsforbruk_per_km_elbil = float(0.2) * float(2.0)
driftsforbruk_per_km_bensin = float(1.0)

#toll costs
bomavgiftElbil =  0.1 
bomavgiftBensinbil = 0.3


antatt_km_arlig = int(input("Hvor mange kilometer forventer du å kjøre i år: ")) #get user input for assumed used in KM

#equations
kostnader_elbil = antatt_km_arlig * (driftsforbruk_per_km_elbil + bomavgiftElbil) + arlig_trafikkforsikringsavgift + forsikring_elbil 
kostnader_bensinbil = antatt_km_arlig * (driftsforbruk_per_km_bensin + bomavgiftBensinbil) + arlig_trafikkforsikringsavgift + forsikring_bensinbil

#outputs
print(f"Det koster {kostnader_elbil} KR årlig for kjøre {antatt_km_arlig} kilometer elbil") #output the approximately totall yearly costs for use electic car in the console
print(f"Det koster {kostnader_bensinbil} KR årlig for kjøre {antatt_km_arlig} kilometer bensin bil") #output the approximately totall yearly costs for use fuel car in the console 
