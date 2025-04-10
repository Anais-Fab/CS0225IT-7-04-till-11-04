# Chiediamo il numero all'utente

numero = int(input("Inserisci un numero per vedere la sua Tabellina\n"))



# Mandiamo in Stampa la Tabellina da 1 a 10
print(f"Tabellina del numero {numero}:")
for i in range(1, 11):
    risultato = numero * i
    print(f"{numero} x {i} = {risultato}")


