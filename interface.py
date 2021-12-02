from datetime import datetime

scelta = input("cosa vuoi fare?\n a)prenotare campo\n b)controllare orari\n")

if scelta == "b": #chiamare fz prenotare

    nome = input("come ti chiami?")
    motivo = input("motivo della prenotazione?")
    
        
    scelta_anno = input("anno")
    scelta_mese = input ("mese")
    scelta_giorno = input("giorno")
    scelta_ora_inizio = input ("ora inizio")
    scelta_minuto_inizio = input ("minuto inizio") 
    scelta_ora_fine = input ("ora fine") 
    scelta_minuto_fine = input ("minuto fine")
    
    d1= datetime.datetime(scelta_anno, scelta_mese, scelta_giorno, scelta_ora_inizio, scelta_minuto_inizio)
    d2= datetime.datetime(scelta_anno, scelta_mese, scelta_giorno, scelta_ora_fine, scelta_minuto_fine)
    
    