from datetime import datetime
from checks import Controllo, Aggiungi

while True:
        scelta = input("cosa vuoi fare?\n a)prenotare campo\n b)controllare orari\n q)esci\n")
        
        if scelta == "q":
            break
        
        if scelta == "a": 
            print("Per prenotare a cavallo di due giorni, fai due prenotazioni per i due giorni diversi")
            nome = input("come ti chiami?")
            motivo = input("motivo della prenotazione?") 
            
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
                    
                    
                    
            x = Aggiungi(iniziale, finale, nome, motivo)
            print(x)
            
        if scelta == "b":
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
            
            
            x = Controllo(iniziale, finale)
            if x == True:
                print("è libero")
            else:
                print ("non è libero")
        
    
        