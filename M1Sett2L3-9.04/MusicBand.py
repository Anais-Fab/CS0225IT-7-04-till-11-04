musicBand = {
    "nome": ""
}

cittaOrigine = {
    "nome": ""
}

nomeAnimaleDomestico = {
    "nome": ""
}

cittaOrigine["nome"] = input ("Quale è il nome della tua città d'origine?\n")
nomeAnimaleDomestico["nome"] = input ("Invece il nome del tuo animale domestico?\n")

musicBand["nome"] = cittaOrigine["nome"] + nomeAnimaleDomestico["nome"]
print("\n!!!Congratulazioni!!!\nIl nome della tua Band è: " + musicBand["nome"].upper())



