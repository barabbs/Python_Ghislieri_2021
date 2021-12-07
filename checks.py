from datetime import datetime
from databaserbarabba import PrendiCalendario,AggiungiEventi

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
    for Event in Calendario:
        while Event[1]<=inizio: #salta eventi precedenti
            pass
        if Event[0]>=fine: #controlla solo primo evento non precedente
            return True
        else:
            return False
    return True


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
         Calendario+=[inizio, fine, nome, motivo]
         Calendario=sorted(Calendario, key=lambda x: x[0])
         AggiungiEventi(Calendario)
         return "Hai prenotato, congratulazioni"

        
def StampaCalendario():
    Calendario = PrendiCalendario()  # Correggi questa linea
    for Evento in Calendario:
        pass
    