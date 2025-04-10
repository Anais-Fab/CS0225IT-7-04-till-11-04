# chiediamo una frase/stringa all'utente. 

stringa = input("Inserisci una stringa: ")

# Creiamo il contatore delle vocali 

vocali = "aeiouAEIOU"
conta_vocali = 0 

# Creiamo un ciclo per ogni carattere della stringa, per il riconoscimento delle vocali

for char in stringa:
    if char in vocali:
        conta_vocali += 1 

# Mandiamo in Stampa il risultato

print(f"Il numero di vocali nella stringa è: {conta_vocali}")

