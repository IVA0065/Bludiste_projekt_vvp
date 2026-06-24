import numpy as np
from .Bludiste import Bludiste
def incidencni_matice(bludiste: Bludiste) -> np.ndarray:
    vrcholy=[]
    for i in range(bludiste.grid.shape[0]):
        for j in range(bludiste.grid.shape[0]):
            if bludiste.grid[i,j]==False:
                vrcholy.append((i,j))
    
    index_vrcholu={}
    for index, vrchol in enumerate(vrcholy):
        index_vrcholu[vrchol]=index
    
    hrany=[]

    for i,j in vrcholy:
        if j+1 < bludiste.grid.shape[0] and not bludiste.grid[i,j+1]:
            u = index_vrcholu[(i,j)]
            v= index_vrcholu[(i,j+1)]
            hrany.append((u,v))

            
    for i,j in vrcholy:
        if i+1 < bludiste.grid.shape[0] and not bludiste.grid[i+1,j]:
            u = index_vrcholu[(i,j)]
            v= index_vrcholu[(i+1,j)]
            hrany.append((u,v))

    inc_matice=np.zeros((len(vrcholy), len(hrany)), dtype=int)

    for e, (u,v) in enumerate(hrany):
        inc_matice[u,e] = 1
        inc_matice[v,e] = 1
    
    return inc_matice

def nejkratsi_cesta(inc_matice: np.ndarray):
    #Pro hledání nejkratší cesty bude použit algoritmus BFS
    cil=inc_matice.shape[0]-1
    fronta=[0]
    navstivene=[]
    predchudce=[]
    for i in range(inc_matice.shape[0]):
        navstivene.append(False)
        predchudce.append(None)
        
    navstivene[0]=True

    while len(fronta)>0:

        vrchol=fronta.pop(0)

        if vrchol == cil:
            break

        for hrana in range(inc_matice.shape[1]):
            if inc_matice[vrchol, hrana] == 1:
                spojene_vrcholy=np.where(inc_matice[:,hrana]==1)[0]

                for soused in spojene_vrcholy:
                    if soused !=vrchol and not navstivene[soused]:
                        navstivene[soused]=True
                        predchudce[soused]=vrchol
                        fronta.append(soused)
    
    if not navstivene[cil]:
        return None
    
    cesta=[]
    aktualni=cil

    while aktualni != None:
        cesta.append(aktualni)
        aktualni= predchudce[aktualni]

    cesta.reverse()

    return cesta
