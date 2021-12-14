import csv
from datetime import datetime


FILENAME = "Prenotazioni.csv"
FORMAT = "%Y/%m/%d %H:%M:%S"


def PrendiCalendario():
    """restituisce una lista, con elementi le prenotazioni (in formato (datetime-datetime-str-str))"""
    try:
        with open("Prenotazioni.csv", 'r', newline='') as csvfile:
            numrig = 0
            ans = []
            for row in csvfile.readlines():
                if numrig >0 :
                    a = row.strip().split(',')
                    # print(a)
                    a[0] = datetime.strptime(a[0], FORMAT)
                    a[1] = datetime.strptime(a[1], FORMAT)
                    ans.append(tuple(a))
                numrig += 1
        return  ans
    except FileNotFoundError:
        return []

def Creatabella(nomecsv):
	with open(nomecsv, 'w', newline='') as csvfile:
		fieldnames = ['Inizio', 'Fine', 'Nome', 'Motivo']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
	return


def AggiungiPrenotazione(tup):
	""" tup = (datetime, datetime, stringa, stringa) = (inizio, fine, nome, motivo)"""
	Inizio = tup[0].strftime(FORMAT)
	Fine = tup[1].strftime(FORMAT)
	Nome = tup[2]
	Motivo = tup[3]
	with open(FILENAME, 'a', newline='') as csvfile:
		fieldnames = ['Inizio', 'Fine', 'Nome', 'Motivo']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writerow({'Inizio': Inizio, 'Fine': Fine, 'Nome': Nome, 'Motivo': Motivo,})
	return




def AggiungiEventi(calendario):
    """calendario deve essere una lista di eventi in formato standard (tupla etc.) scrive un csv"""
    Creatabella(FILENAME)
    for evento in calendario:
        # print(evento)
        AggiungiPrenotazione(evento)
        


	


# inizio = datetime(2021, 2, 12, 13,45)
# fine = datetime(2021, 2, 12, 14,55)
# nome = 'PITUCCI'
# motivo = 'CRACK'
# tuplaesempio = (inizio, fine, nome, motivo)

# #print(data.year)
# #print(data.strftime(FORMAT))

# # AggiungiEventi([])
# AggiungiPrenotazione(tuplaesempio)

# A = PrendiCalendario()

# # print(A)	

# AggiungiEventi(A)




