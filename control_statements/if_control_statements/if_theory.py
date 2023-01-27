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