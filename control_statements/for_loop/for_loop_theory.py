#un for loop viene utilizzato per iterazione (ripetere) una stessa azione un numero definito di volte

#un for loop ha un loop header in cui viene defenito il numero di iterazioni
#for <variabile> in range(<numero intero che definisce il numero di ripetizioni>)

#un for loop ha un loop body in cui vengono scritte le istruzioni da eseguire ad ogni iterazione
#   <statement-1>
#   .
#   .
#   .
#   <statement-n>

for ciascuna_iterazione in range(5):
    print('iterazione numero ' + str(ciascuna_iterazione))
    print('altra istruzione di iterazione numero ' + str(ciascuna_iterazione))
# output    
#   iterazione numero 0
#   altra istruzione di iterazione numero 0
#   iterazione numero 1
#   altra istruzione di iterazione numero 1
#   iterazione numero 2
#   altra istruzione di iterazione numero 2
#   iterazione numero 3
#   altra istruzione di iterazione numero 3
#   iterazione numero 4
#   altra istruzione di iterazione numero 4

#calcolare 2 elevato alla 3
#devo ripetere la moltiplicazione su 2, tre volte

numero_da_elevare = 2
esponente = 3
prodotto = 1

for iterazione in range (esponente):
    prodotto = prodotto * numero_da_elevare
    #stampa per tracciare se il loop fa quello che vogliamo
    print(prodotto, end=" ")
print("\n2 elevato alla 3 è uguale a " + str(prodotto))

#for <variabile> in range (<limite inferiore>, <limite superiore> + 1):

#sommare i numeri da un numero ad un altro
limite_inferiore = int(input("Inserisci il limite inferiore della sommatoria: "))
limite_superiore = int(input("Inserisci il limite superiore della sommatoria: "))
sommatoria = 0
for numero in range(limite_inferiore, limite_superiore + 1):
    sommatoria = sommatoria + numero
    #controllo su ciascuna iterazione
    print("il risultato della sommatoria all'iterazione numero " + str(numero) + " è "+ str(sommatoria))
print(f"\nLa sommatoria con limite inferiore {limite_inferiore} e limite superio {limite_superiore} è uguale a {sommatoria}")


##specificare un valore per saltare nel range
#calcola la somma dei numeri pari tra 1 e 10
somma = 0
for conta in range(2, 11, 2):
    somma += conta
print(somma) 

##loop che contano al contrario

for count in range (10, 0 , -1):
    print( count, end = " ")