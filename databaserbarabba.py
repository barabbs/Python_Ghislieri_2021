from datetime import datetime

FILENAME = "PrenotazioniBarabba.csv"
FORMAT = "%m/%d/%Y %H:%M:%S"

def PrendiCalendario():
    eventi = list()
    with open(FILENAME) as f:
        for l in f.readlines():
            i=l[:-1].split(",")
            eventi.append((datetime.strptime(i[0], FORMAT), datetime.strptime(i[1], FORMAT), i[2], i[3]))
    return eventi

def AggiungiEventi(evento):
    with open(FILENAME, "a") as f:
        f.write(",".join((evento[0].strftime(FORMAT),evento[2].strftime(FORMAT),evento[2],evento[3])) + "\n")
                
