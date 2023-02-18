#legge il contenuto del file data.txt ma lo memorizza
#with open('data.txt','r') as f:
#size_to_read = 100
#    f_contents = f.read(size_to_read)
#    print(f_contents)
#f.close()

#via efficiente stampo ogni singola linea del file
with open('data.txt','r') as f:
    for line in f:
        print(line, end='')
f.close()

#creare e scrivere qualcosa su un file
with open('data2.txt','w') as f:
    #pass
    f.write('Giancarlo pythonista')
f.close()

#copiare il contenuto di un file su un altro file
with open('data2.txt', 'r') as rf:
    with open('data2_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
rf.close()
wf.close()

#aggiungere un altro contenuto sul file creato in precedenza
with open('data.txt', 'r') as rf:
    with open('data2_copy.txt', 'a') as af:
        for line in rf:
            af.write(line)
rf.close()
af.close()
