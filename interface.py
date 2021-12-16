from datetime import datetime
from checks import Controllo, Aggiungi, StampaCalendario, CercaPersona

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
    
while True:
        scelta = input("cosa vuoi fare?\n a)prenotare campo\n b)controllare orari\n c)visualizzare calendario di un giorno\n d)visualizzare prenotazioni di una persona\n q)esci\n>").lower()
        
        if scelta == "q":
            break
        
        elif scelta == "a": 
            print("Per prenotare a cavallo di due giorni, fai due prenotazioni per i due giorni diversi")
            nome = input("come ti chiami? >")
            motivo = input("motivo della prenotazione? >") 
            iniziale,finale=input_data_ora()
            print(iniziale.strftime("%m/%d/%Y, %H:%M") + " - " + finale.strftime("%H:%M") + " - " + nome + " - " + motivo)
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
            nome = input("inserisci il nominativo > ")
            CercaPersona(nome)
            