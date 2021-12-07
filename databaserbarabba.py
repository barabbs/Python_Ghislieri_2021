from datetime import datetime

FILENAME = "PrenotazioniBarabba.csv"
FORMAT = "%Y/%m/%d %H:%M:%S"

def PrendiCalendario():
    eventi = list()
    with open(FILENAME) as f:
        for l in f.readlines():
            i=l[:-1].split(",")
            eventi.append((datetime.strptime(i[0], FORMAT), datetime.strptime(i[1], FORMAT), i[2], i[3]))
    return eventi

def AggiungiEventi(calendario):
    with open(FILENAME, "w") as f:
        for evento in calendario:
            f.write(",".join((evento[0].strftime(FORMAT),evento[1].strftime(FORMAT),evento[2],evento[3])) + "\n")
                
