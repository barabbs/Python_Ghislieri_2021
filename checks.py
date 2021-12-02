from datetime import datetime

def Controllo(inizio, fine, Calendario):
    for Event in Calendario:
        if not (fine<=Event[0] or inizio>=Event[1]):
            return False
    return True

inizio=datetime(2020,1,13)
fine=datetime(2020,1,16)
Calendario=[(datetime(2020,1,12),datetime(2020,1,17),"Pippo", "motivo")]

print(Controllo(inizio, fine, Calendario))

def Aggiungi(inizio, fine, nome, motivo, Calendario):
     if Controllo(inizio, fine, Calendario)==False:
         return "Ah che dispiazere"
     else:
         Calendario+=[inizio, fine, nome, motivo]
         Calendario=sorted(Calendario, key=lambda x,y: x[0]<y[0])
         
#def Stampa(Calendario):
    
    