# Creiamo un calcolatore di perimetro di figure Geometriche 

import math  # (aggiongiamo l'import math per la libreria di matematica per aggiungere il pi greco)

def perimetroQuadrato(lato):
    return (lato * 4)

def perimetroCerchio(raggio):
    return (2 * math.pi * raggio )
    
def basexAltezzaRettangolo(base, altezza):
    return (base * 2 + altezza * 2)

# Chiediamo all'utente quale forma Geometrica vuole calcolare

print("\n\n*** Benvenuti nel Calcolatore Digitale di Anais ***\n\n")
input_utente = input("Quale forma vuoi calcolare oggi? Scegli tra le seguenti:\n1 - Quadrato\n2 - Cerchio\n3 - Rettanngolo\n\n")

# Chiediamo all'utente che unità di misura vuole usare:

unita = input("Quale unità di misura vuoi usare? (es. mm, cm, m:)  ")

# Adesso organizziamo i vari casi anche di Key-sensitive in cui l'utente possa rispondere e le condizioni.

if input_utente == "Quadrato" or input_utente == "1" or input_utente == "1 - Quadrato" "or 1 - quadrato" or input_utente == "quadrato":
    lato = input("Misura del lato che vuoi calcolare?\n ") 
    perimetro = perimetroQuadrato(int(lato))
    print(f"Il perimetro del tuo quadrato è: {perimetro} {unita}")

elif input_utente == "Cerchio" or input_utente == "2" or input_utente == "2 - Cerchio" or input_utente =="2 - cerchio" or input_utente == "cerchio":
    raggio = input("Misura del raggio che vuoi calcolare?\n ") 
    perimetro = perimetroCerchio(int(raggio))
    print(f"Il raggio del tuo cerhio è: {perimetro} {unita}")

else:
    base = input("Misura della base?  ") 
    altezza = input("Misura Altezza?  ")
    perimetro = basexAltezzaRettangolo(int(base),int(altezza))
    print(f"Il perimetro del tuo quadrato è: {perimetro} {unita}")

# Il programma esegue in modo corretto tutti i comandi. 