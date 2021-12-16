from datetime import datetime, timedelta
from databaser import PrendiCalendario,AggiungiEventi


def Controllo(inizio, fine):
    """
    inizio : datetime
    fine : datetime 
    -------
    bool
        True indica prenotazione possibile.
    """
    Calendario = PrendiCalendario()  
    for Evento in Calendario:
        if Sovrapposizione(Evento[0] ,Evento[1], inizio, fine):
            return False
    return True

def Sovrapposizione(ev_inizio, ev_fine, inizio, fine):
    return not (ev_inizio>=fine or ev_fine<=inizio)
    

def Aggiungi(inizio, fine, nome, motivo):
     """
    inizio : datetime
    fine : datetime
    nome : string
    motivo : string
    -------
    str
        DESCRIPTION.

    """
     Calendario = PrendiCalendario()  # Correggi questa linea
     
     if inizio<datetime.now():
         return "Hai inserito una data vecchia"
     elif not Controllo(inizio, fine):
         return "Gli orari nei quai vuoi prenotare sono occupati, mi spiace"
     
     else:
         Calendario.append((inizio, fine, nome, motivo))
         Calendario=sorted(Calendario, key=lambda x: x[0])
         AggiungiEventi(Calendario)
         return "Hai prenotato, congratulazioni"

        
def StampaCalendario(giorno):  
    """Giorno = datetime"""
    Calendario = PrendiCalendario()  # Correggi questa linea
    L = []
    for Evento in Calendario:
        I = Evento[0]
        if I.year == giorno.year and I.month == giorno.month and I.day == giorno.day:
            L.append(Evento)
    DT = datetime(giorno.year, giorno.month, giorno.day, 0, 0, 0)
    CosaPrinto = ""
    delta = timedelta(minutes = 30)
    for i in range(48):
        CosaPrinto += DT.strftime("%H:%M")
        for Evento in L:
            I = Evento[0]
            F = Evento[1]
            if I <= DT and F >= DT + delta:
                CosaPrinto += '  Prenotante : ' + Evento[2] + ' Per : ' + Evento[3]
        CosaPrinto += "\n"
        DT = DT + delta
    print(CosaPrinto)   
    return

def CercaPersona(persona):
    Calendario = PrendiCalendario()
    B=[]
    for a in Calendario:
        if a[2]==persona:
            B=B+[a]
    return B
           
    
def ListaPersone():
    Calendario = PrendiCalendario()
    B=[]
    for a in Calendario:
       if a[2] not in B:
           B=B+[a[2]]
    return B

def Elimina(prenotazione):
    Calendario = PrendiCalendario()
    for a in Calendario:
        if a==prenotazione:
            Calendario.remove(a)
    AggiungiEventi(Calendario) 
           