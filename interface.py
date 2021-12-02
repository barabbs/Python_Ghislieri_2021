from datetime import datetime
from checks import Controllo, Aggiungi

scelta = input("cosa vuoi fare?\n a)prenotare campo\n b)controllare orari\n")

if scelta == "a": 

    nome = input("come ti chiami?")
    motivo = input("motivo della prenotazione?")
    
        
    x=0
    while x==0:    
        try: 
            x=1
            scelta_anno = int(input("anno"))
            scelta_mese = int(input ("mese"))
            scelta_giorno = int(input("giorno"))
            scelta_ora_inizio = int(input ("ora inizio"))
            scelta_minuto_inizio = int(input ("minuto inizio")) 
            scelta_ora_fine = int(input ("ora fine")) 
            scelta_minuto_fine = int(input ("minuto fine"))
           
        except ValueError:
            x=0
            print("inserisci la data nel formato AAAA-MM-GG e l'ora nel formato HH-MM")
           
        
        
    iniziale= datetime(scelta_anno, scelta_mese, scelta_giorno, scelta_ora_inizio, scelta_minuto_inizio)
    finale= datetime(scelta_anno, scelta_mese, scelta_giorno, scelta_ora_fine, scelta_minuto_fine)
    
    x = Aggiungi(iniziale, finale, nome, motivo)
    print(x)
    
if scelta == "b":
    
    x=0
    while x==0:    
        try: 
            x=1
            scelta_anno = int(input("anno"))
            scelta_mese = int(input ("mese"))
            scelta_giorno = int(input("giorno"))
            scelta_ora_inizio = int(input ("ora inizio"))
            scelta_minuto_inizio = int(input ("minuto inizio")) 
            scelta_ora_fine = int(input ("ora fine")) 
            scelta_minuto_fine = int(input ("minuto fine"))
           
        except ValueError:
            x=0
            print("inserisci la data nel formato AAAA-MM-GG e l'ora nel formato HH-MM")
        
        
    iniziale= datetime(scelta_anno, scelta_mese, scelta_giorno, scelta_ora_inizio, scelta_minuto_inizio)
    finale= datetime(scelta_anno, scelta_mese, scelta_giorno, scelta_ora_fine, scelta_minuto_fine)
    
    x = Controllo(iniziale, finale)
   
    if x == True:
        print("è libero")
    else:
        print ("non è libero")