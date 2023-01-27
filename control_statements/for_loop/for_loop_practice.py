for count in range(5):
    print(count + 1, end = " ")
#1 2 3 4 5
print("\n")
for count in range(1, 4):
    print(count, end = " ")
#1 2 3 
print("\n")
for count in range(1, 6, 2):
    print(count, end = " ")
#1 3 5 
print("\n")
for count in range(6, 1 , -1):
    print(count, end = " ")
#6 5 4 3 2

#Scrivi un loop che stampa il tuo nome 100 volte. Ciascuna stampa inizia su una nuova linea
nome = "Giancarlo"
for iterazione in range (100):
    print('\n' + nome + " iterazione numero " + str(iterazione))

#scrivi un loop che stampa i primi 128 valori ASCII  seguiti dal corrispondente carattere
for iterazione in range(0, 127):
    print("valore ASCII " + str(iterazione) + " carattere corrisponte " + chr(iterazione))

for character in "teststring":
    print("il carattere \'" + character + "\'" + " ha valore ASCII " + str(ord(character)))