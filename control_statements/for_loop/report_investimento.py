#Gli input del programma sono: 
# ammontare totale di investimento (float number)
# un periodo di anni (intero)
# un tasso di interesse (una percentuale espressa in interi)

#il programma utilizza una forma semplice di interesse composto, in cui l'interesse è computato una volta per ciascun anno e aggiunto
#all'ammontare totale investito.
#l'output del programma è un report in forma tabulare che mostra, per ciascun anno nei termi di investimento, i numeri di anni, 
#il bilancio iniziale all'inizio dell'anno, l'interesse per l'anno, e il bilancio finale dell'anno.
#le colonne sono tabulate per una facile lettura

investment_amount = float(input("Inserisci un ammontare iniziale: "))
anni = int(input("per quanti anni fai il calcolo dell'interesse maturato? inserisci un intero:  "))
tasso_interesse = float(input("inserisci il tasso di interesse per l'investimento: "))

interesse_maturato = 0.0
tasso = tasso_interesse / 100

print("%4s%18s%10s%16s" % ("Anno", "Bilancio iniziale", "Interesse", "Bilancio finale"))
for anno in range(1, anni + 1):
    interesse = investment_amount * tasso
    bilancio_finale = investment_amount + interesse
    print("%4d%18.2f%10.2f%16.2f" %(anno, investment_amount, interesse, bilancio_finale))
    investment_amount = bilancio_finale
    interesse_maturato += interesse