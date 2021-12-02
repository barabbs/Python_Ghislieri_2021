from datetime import datetime

def Controllo(FasciaOraria, Calendario):
    inizio=FasciaOraria[0]
    fine=FasciaOraria[1]
    for Event in Calendario:
        if not (fine<=Event[0] or inizio>=Event[1]):
            return False
    return True

inizio=datetime(2020,1,13)
fine=datetime(2020,1,16)
Calendario=[(datetime(2020,1,14),datetime(2020,1,15),"Pippo", "motivo")]

print(Controllo((inizio,fine), Calendario))
