from datetime import datetime
from databaser import PrendiCalendario,AggiungiEventi

def Controllo(inizio, fine):
    """
    inizio : datetime
    fine : datetime 
    -------
    bool
        True indica prenotazione possibile.
    """
    Calendario = PrendiCalendario()  # Correggi questa linea
    #Assumiamo che calendario sia ordinata in ordine cronologico
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
     if not Controllo(inizio, fine):
         return "Gli orari nei quai vuoi prenotare sono occupati, mi spiace"
     else:
         Calendario.append((inizio, fine, nome, motivo))
         Calendario=sorted(Calendario, key=lambda x: x[0])
         AggiungiEventi(Calendario)
         return "Hai prenotato, congratulazioni"

        
def StampaCalendario():
    Calendario = PrendiCalendario()  # Correggi questa linea
    for Evento in Calendario:
        pass
    