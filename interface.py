from datetime import datetime
from checks import Controllo, Aggiungi, StampaCalendario, CercaPersona, ListaPersone

def input_data_ora():
    while True:    
        try:
            scelta_anno = int(input("anno"))
            scelta_mese = int(input ("mese"))
            scelta_giorno = int(input("giorno"))
            scelta_ora_inizio = int(input ("ora inizio"))
            scelta_minuto_inizio = int(input ("minuto inizio")) 
            scelta_ora_fine = int(input ("ora fine")) 
            scelta_minuto_fine = int(input ("minuto fine"))
            
            iniziale= datetime(scelta_anno, scelta_mese, scelta_giorno, scelta_ora_inizio, scelta_minuto_inizio)
            finale= datetime(scelta_anno, scelta_mese, scelta_giorno, scelta_ora_fine, scelta_minuto_fine)
            break
        except ValueError:
            print("inserisci la data nel formato AAAA-MM-GG e l'ora nel formato HH-MM")
    return iniziale, finale

def input_data():
    while True:    
        try:
            scelta_anno = int(input("anno"))
            scelta_mese = int(input ("mese"))
            scelta_giorno = int(input("giorno"))
            
            data= datetime(scelta_anno, scelta_mese, scelta_giorno)            
            break
        except ValueError:
            print("inserisci la data nel formato AAAA-MM-GG e l'ora nel formato HH-MM")
    return data

def stampa_evento(evento):
     print(evento[0].strftime("%m/%d/%Y, %H:%M") + " - " + evento[1].strftime("%H:%M") + " - " + evento[2] + " - " + evento[3])
    
while True:
        scelta = input("cosa vuoi fare?\n a)prenotare campo\n b)controllare orari\n c)visualizzare calendario di un giorno\n d)visualizzare prenotazioni di una persona\n e)eliminare prenotazione\n q)esci\n>").lower()
        
        if scelta == "q":
            break
        
        elif scelta == "a": 
            print("Per prenotare a cavallo di due giorni, fai due prenotazioni per i due giorni diversi")
            nome = input("come ti chiami? >")
            motivo = input("motivo della prenotazione? >") 
            iniziale,finale=input_data_ora()
            stampa_evento((iniziale, finale, nome, motivo))
            conferma = input("confermi questa prenotazione?: \n a)sì\n b)no\n>")
            if conferma.lower()=="a":            
                x = Aggiungi(iniziale, finale, nome, motivo)
                print(x)
            
        elif scelta == "b":
            iniziale,finale=input_data_ora()
            x = Controllo(iniziale, finale)
            if x == True:
                print("è libero")
            else:
                print ("non è libero")
                
        elif scelta == "c":
            data=input_data()
            StampaCalendario(data)
            
        elif scelta == "d":
            print()
            x = ListaPersone()
            for i in x:
                print(i)
            nome = input("inserisci il nominativo > ")
            if nome in x:
                for evento in CercaPersona(nome):
                    stampa_evento(evento)
            else:
                print("Il nome non è nella lista dei prenotati")
        
        elif scelta == "e":
                   
            
            pass