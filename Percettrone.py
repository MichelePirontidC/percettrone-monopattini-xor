"""
Percettrone semplice con due dataset dimostrativi.


Scenari disponibili:
- "monopattini": esempio originale dell'elaborato, linearmente separabile.
- "xor": esempio classico non linearmente separabile.

Per cambiare scenario, può modificare il valore della variabile SCENARIO.
"""

# ---------------------------------------------------------------------------
# CONFIGURAZIONE DELL'ESECUZIONE
# ---------------------------------------------------------------------------
# Selezionare lo scenario da eseguire.
# Valori ammessi: "monopattini" oppure "xor".
SCENARIO = "monopattini"

# Il learning rate stabilisce l'ampiezza della correzione dei pesi.
learning_rate = 1

# Numero massimo di epoche di addestramento.
# Un'epoca corrisponde a una passata completa su tutti gli esempi del dataset.
max_epoche = 20


# ---------------------------------------------------------------------------
# DATASET DISPONIBILI
# ---------------------------------------------------------------------------
# Dataset 1: manutenzione di monopattini elettrici.
#
# Ogni esempio è composto da tre ingressi binari:
# x1 = batteria bassa
# x2 = zona ad alta richiesta
# x3 = problema tecnico segnalato
#
# Il target vale:
# +1 = manutenzione prioritaria
# -1 = nessuna manutenzione prioritaria
#
# Questo dataset rappresenta il caso applicativo originale descritto
# nell'elaborato. È costruito in modo da essere linearmente separabile,
# quindi il percettrone può imparare a classificarlo correttamente.
dataset_monopattini = [
    ([0, 0, 0], -1),
    ([1, 0, 0], -1),
    ([1, 1, 0], 1),
    ([0, 1, 1], 1),
    ([0, 0, 1], -1),
    ([1, 0, 1], 1),
    ([0, 1, 0], -1),
    ([1, 1, 1], 1),
]

# Dataset 2: funzione XOR.
#
# Il target vale +1 quando i due ingressi sono diversi,
# mentre vale -1 quando i due ingressi sono uguali.
#
# Questo dataset è incluso per mostrare il limite del singolo percettrone:
# i punti positivi e negativi non sono separabili con una sola retta.
dataset_xor = [
    ([0, 0], -1),
    ([1, 0], 1),
    ([0, 1], 1),
    ([1, 1], -1),
]


# ---------------------------------------------------------------------------
# SELEZIONE DEL DATASET
# ---------------------------------------------------------------------------
# In base al valore della variabile SCENARIO viene scelto il dataset
# da usare nell'esecuzione. Se il valore non è valido, il programma
# si interrompe con un messaggio di errore.
if SCENARIO == "monopattini":
    dataset = dataset_monopattini
    nome_scenario = "Manutenzione monopattini elettrici"
elif SCENARIO == "xor":
    dataset = dataset_xor
    nome_scenario = "XOR"
else:
    raise ValueError("SCENARIO deve essere 'monopattini' oppure 'xor'.")


# ---------------------------------------------------------------------------
# INIZIALIZZAZIONE DEL PERCETTRONE
# ---------------------------------------------------------------------------
# Il numero di pesi è pari al numero di ingressi del dataset più uno.
# Il peso aggiuntivo rappresenta il bias.
#
# Il bias viene trattato come un peso associato a un ingresso costante x0 = 1.
# Questa scelta rende l'aggiornamento del bias identico a quello degli altri pesi.
numero_ingressi = len(dataset[0][0])
pesi = [0] * (numero_ingressi + 1)

print("Scenario:", nome_scenario)
print("Pesi iniziali:", pesi)
print()


# ---------------------------------------------------------------------------
# ADDESTRAMENTO DEL PERCETTRONE
# ---------------------------------------------------------------------------
# Per ogni epoca il programma scorre tutti gli esempi del dataset.
# Per ciascun esempio:
# 1. aggiunge l'ingresso costante del bias;
# 2. calcola il potenziale di attivazione z;
# 3. applica la funzione di attivazione a soglia;
# 4. confronta l'output prodotto con il target;
# 5. aggiorna i pesi solo se la classificazione è errata.
for epoca in range(1, max_epoche + 1):
    errori = 0

    for x, target in dataset:
        x_con_bias = [1] + x

        # Calcolo del potenziale di attivazione:
        # z = w0*x0 + w1*x1 + ... + wn*xn
        z = 0
        for i in range(len(pesi)):
            z += pesi[i] * x_con_bias[i]

        # Funzione di attivazione a soglia.
        # Se z è positivo, il percettrone assegna la classe +1;
        # altrimenti assegna la classe -1.
        if z > 0:
            output = 1
        else:
            output = -1

        # Regola di aggiornamento:
        # wi <- wi + learning_rate * target * xi
        #
        # L'aggiornamento avviene solo quando l'output prodotto è diverso
        # dal target corretto. In questo modo il percettrone corregge i pesi
        # degli ingressi presenti nell'esempio che ha generato l'errore.
        if output != target:
            for i in range(len(pesi)):
                pesi[i] = pesi[i] + learning_rate * target * x_con_bias[i]

            errori += 1

    print("Epoca", epoca, "- errori:", errori, "- pesi:", pesi)

    # Se un'intera epoca termina senza errori, il dataset è stato classificato
    # correttamente e l'addestramento può interrompersi.
    if errori == 0:
        print("\nAddestramento completato: nessun errore nell'ultima epoca.")
        break


# ---------------------------------------------------------------------------
# VERIFICA FINALE DEL MODELLO
# ---------------------------------------------------------------------------
# Dopo l'addestramento, il programma applica i pesi finali a tutti gli esempi
# del dataset e stampa, per ciascuno di essi:
# - gli ingressi;
# - il valore z calcolato dal percettrone;
# - l'output prodotto;
# - il target atteso;
# - l'esito della classificazione.
#
# Questa parte permette di verificare concretamente se il percettrone ha
# imparato il dataset scelto. Nel caso "monopattini" ci si aspetta una
# classificazione corretta di tutti gli esempi; nel caso "xor" no, perché
# il problema non è linearmente separabile.
print("\nVerifica finale:")

corretti = 0

for x, target in dataset:
    x_con_bias = [1] + x

    z = 0
    for i in range(len(pesi)):
        z += pesi[i] * x_con_bias[i]

    if z > 0:
        output = 1
    else:
        output = -1

    if output == target:
        corretti += 1
        risultato = "corretto"
    else:
        risultato = "errato"

    print("Input:", x, "| z:", z, "| output:", output, "| target:", target, "|", risultato)


# ---------------------------------------------------------------------------
# SINTESI DEL RISULTATO
# ---------------------------------------------------------------------------
# La sintesi finale rende immediatamente visibile il comportamento del modello.
# Se tutti gli esempi sono corretti, il percettrone ha trovato un confine
# lineare adeguato. Se restano errori, il dataset scelto non è stato appreso
# perfettamente dal singolo percettrone.
print("\nClassificazioni corrette:", corretti, "/", len(dataset))

if corretti == len(dataset):
    print("Il percettrone ha classificato correttamente tutti gli esempi.")
else:
    print("Il percettrone non ha classificato correttamente tutti gli esempi.")
    print("Questo può accadere quando il problema non è linearmente separabile, come nel caso XOR.")
