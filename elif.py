giorni = int(input ("Inserisci il numero dei giorni di noleggio: "))

if giorni == l:
    tariffa = 45.0
elif giorni ==2:
    tariffa = 80.0
elif giorni == 3:
    tariffa = 120.0
elif giorni == 4:
    tariffa = 160.0
else:
    tariffa = (giorni - 4) * 40.0 + 160.0
print ("Il costo è di:", tariffa)
