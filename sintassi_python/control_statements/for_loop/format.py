print("%8s" % "four")
print("%-2s" % "four")

#<format string> % <datum>
#<format string> è composta da un % segnaposto, il numero di spazi (da 5 è uno) e s che indica stringa (d per intero, f per float
#formattare decimali
#<%field width>.<precision>f
salario = 100.00
print("il tuo salario è $%0.3f" % salario)
#il tuo salario è $100.000
amount = 24.325
print("il tuo salario è $%0.2f" % amount)
#24.32
print("l'area è di %0.1f" % amount)
#24.3
print("%7f" % amount)
#   24.325000

print("%6d %6d %6d" % (1, 10, 20))

print("%0.2f" % 10.240635)

salari = [10.2003, 23.32441, 25.34242321, 241234.2491358]

for salario in salari:
    print("%12.2f" % salario)