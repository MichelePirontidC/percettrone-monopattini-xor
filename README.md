# Percettrone semplice – Esempio dimostrativo

Questo repository contiene un piccolo programma Python realizzato come supporto all'elaborato sul **percettrone** per il corso di Intelligenza Artificiale.

L'obiettivo del codice è mostrare in modo semplice:

- come un percettrone calcola il proprio output;
- come vengono aggiornati i pesi durante l'addestramento;
- perché il percettrone funziona con problemi linearmente separabili;
- perché non riesce a risolvere correttamente un problema non linearmente separabile come XOR.


## Scenari disponibili

Il programma permette di eseguire due scenari diversi.

### 1. Manutenzione monopattini elettrici

È l'esempio originale usato nell'elaborato.

Il percettrone deve decidere se un monopattino deve ricevere manutenzione prioritaria oppure no, sulla base di tre ingressi binari:

- batteria bassa;
- zona ad alta richiesta;
- problema tecnico segnalato.

Il target vale:

- `+1` = manutenzione prioritaria;
- `-1` = nessuna manutenzione prioritaria.

Questo scenario è linearmente separabile, quindi il percettrone riesce a classificare correttamente tutti gli esempi.

### 2. XOR

Il secondo scenario riproduce la funzione XOR.

Il target vale `+1` quando i due ingressi sono diversi e `-1` quando sono uguali.

Questo scenario è utile per mostrare il limite del singolo percettrone: i casi positivi e negativi non possono essere separati con una sola retta, quindi il modello non riesce a classificare correttamente tutti gli esempi.

## Come scegliere lo scenario

Nel file Python è presente la variabile:

SCENARIO = "monopattini"

Per eseguire l'esempio dei monopattini, lasciare:

```python
SCENARIO = "monopattini"
```

Per eseguire l'esempio XOR, modificare la riga in:

```python
SCENARIO = "xor"
```

## Come eseguire il programma

Aprire il terminale nella cartella del repository ed eseguire:

```bash
python Percettrone.py
```

In alternativa, su alcuni sistemi Windows può essere necessario usare:

```bash
py Percettrone.py
```

## Output del programma

Il programma stampa:

- lo scenario selezionato;
- i pesi iniziali;
- per ogni epoca, il numero di errori e i pesi aggiornati;
- la verifica finale sul dataset;
- il numero di classificazioni corrette.

Nel caso dei monopattini, il programma dovrebbe arrivare a classificare correttamente tutti gli esempi.

Nel caso XOR, invece, il programma mostra che un singolo percettrone non riesce a eliminare completamente gli errori, perché il dataset non è linearmente separabile.

