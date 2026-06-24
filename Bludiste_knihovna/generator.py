import random
from .Bludiste import Bludiste
from .Resitel import incidencni_matice, nejkratsi_cesta

def generuj(velikost:int, sablona: str) -> Bludiste:
    start=(0,0)
    cil=(velikost-1,velikost-1)
    if sablona=="prazdne":
        bludiste=Bludiste.prazdne(velikost)
    
    elif sablona =="slalom":
        bludiste=Bludiste.slalom(velikost)
    
    bludiste.grid[start]=False
    bludiste.grid[cil]=False

    for x in range(velikost*velikost):
        i=random.randint(0,velikost-1)
        j=random.randint(0,velikost-1)
        if (i,j) == start:
            continue
        if(i,j) == cil:
            continue
        if bludiste.grid[i,j]:
            continue
        bludiste.grid[i,j]=True
        inc=incidencni_matice(bludiste)
        cesta=nejkratsi_cesta(inc)
        if cesta==None:
            bludiste.grid[i,j] = False
    return bludiste