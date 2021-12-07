import csv
from datetime import datetime


FILENAME = "Prenotazioni.csv"
FORMAT = "%m/%d/%Y %H:%M:%S"




def Creatabella():
	with open(FILENAME, 'w', newline='') as csvfile:
		fieldnames = ['Inizio', 'Fine', 'Nome', 'Motivo']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		writer.writerow({'Inizio': '1230', 'Fine': '1300', 'Nome': 'Barabba', 'Motivo': 'Sì'})
	return
	
#Creatabella()


inizio = datetime(2021, 2, 12, 13,45)
fine = datetime(2021, 2, 12, 14,55)
nome = 'PITUCCI'
motivo = 'crack'
tuplaesempio = (inizio, fine, nome, motivo)

#print(data.year)
#print(data.strftime(FORMAT))


def AggiungiPrenotazione(tup):
	""" tup = (datetime, datetime, stringa, stringa) = (inizio, fine, nome, motivo)"""
	Inizio = tup[0].strftime(FORMAT)
	Fine = tup[1].strftime(FORMAT)
	Nome = tup[2]
	Motivo = tup[3]
	with open(FILENAME, 'a', newline='') as csvfile:
		fieldnames = ['Inizio', 'Fine', 'Nome', 'Motivo']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writerow({'Inizio': Inizio, 'Fine': Fine, 'Nome': Nome, 'Motivo': Motivo})
	
	return
	
	
AggiungiPrenotazione(tuplaesempio)
