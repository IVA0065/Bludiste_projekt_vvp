import numpy as np
from pathlib import Path

class Bludiste:
    def __init__(self,grid: np.ndarray):
        self.grid=grid.astype(bool)
        self.size=grid.shape[0]
    
    @classmethod
    def nacteni_z_csv(cls, path: str | Path) -> "Bludiste":
        grid=np.loadtxt(path, delimiter=",", dtype=int)

        return cls(grid.astype(bool))
    
    @classmethod #Zde budou implementovany metody pro generování prázdného a slalomového bludiště
    def prazdne(cls, size: int) -> "Bludiste":
        grid=np.zeros((size, size), dtype=bool)
        return cls(grid)
    @classmethod
    def slalom(cls, size: int) -> "Bludiste":
        grid=np.zeros((size,size), dtype=bool)

        for i in range(1,size-1,2):
            if (i//2)%2==0:
                grid[i,:-1]=True
                grid[i,-2]=False
            else:
                grid[i,1:]=True
                grid[i,1]=False
        grid[0,0]=False
        grid[-1,-1]=False

        return cls(grid)
    