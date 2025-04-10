# Chiediamo all'utente di inserire i numeri separati da uno spazio:
input_numeri = input("Inserisci una lista dei numeri \nseparati da uno spazio: ")

# Convertiamo la stringa in una lista di numeri interi
listaNumeri = [int(num) for num in input_numeri.split()]

# Troviamo il massimo
massimo = max(listaNumeri)

# Mandiamo in Stampa
print(f"Il massimo numero nella lista è: {massimo}")

