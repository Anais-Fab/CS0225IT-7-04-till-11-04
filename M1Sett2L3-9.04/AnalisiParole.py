def analizza_parole(testo):
    # Rendi il testo case-Insensitive e rimuovi la punteggiatura
    testo = re.sub(r'[^ \w\s]', ", testo.lower())