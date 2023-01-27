#gli statement if-else costituiscono i selection statement più utilizzati. 
# Indirizzano la computazione nella scelta tra due alternativi corsi di azione.
# Sono utilizzati per fare un controllo su errori e per rispondere in caso di errore.

import math

area = float(input("Enter the area: "))
if area > 0:
    radius = area / math.pi
    print("the radius is ", radius)
else:
    print("Error: the area must be a positive number")
    
#if <condizione>:
#   <statements>
#else:
#   <statements>

#nella condizione deve esserci una espressione booleana: una espressione che valuta se è vera o falsa.

#stampa il massimo e il minimo tra due numeri in input
first = int(input("inserisci il primo numero: "))
second = int(input("inserisci il secondo numero: "))
if first > second:
    maximum = first
    minimum = second
else:
    maximum = second
    minimum = first
print("Maximum: ", maximum)
print("Minimum: ", minimum)

#python dispone di due funzioni che rendono inutile un if-else del genere. 
print("calcolato con le funzioni built-in max e min")
print("Maximum: ", max(first, second))
print("Minimum: ", min(first, second))

#la forma più semplice di selezione è if statement. 
#tale tipo di control statement è anche chiamata selezione ad una via, perché consiste di un una condizione 
# e soltanto una singola sequenza di statement. Le la condizione è vera esegue tale sequenza, altrimenti procede allo 
# step successivo, esterni all'if, eseguendo gli step rimanenti.
#if <condizione>:
#   <sequenza di istruzioni>

#gli if statement vengono spesso utilizzati per prevenire l'esecuzione di alcuni comandi senza che siano nella giusta condizione.
x = "qualcosa"
if x < 0:
    x= -x
    
#multiway if statements: quando bisogna testare varie condizioni e agire in base ad esse

number = int(input("Inserisci un numero per una votazione: "))
if number > 89:
    lettera = 'A'
elif number > 79:
    lettera ='B'
elif number > 69:
    lettera ='C'
else:
    lettera = 'F'
print("Il voto in lettere è ", lettera)