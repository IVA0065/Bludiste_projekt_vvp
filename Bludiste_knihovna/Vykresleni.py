import numpy as np
import matplotlib.pyplot as plt
def vykresli_cestu(bludiste: Bludiste, cesta: list[int]|None, vrcholy:list[tuple[int,int]]) -> None:
    grid=bludiste.grid

    img=np.ones((grid.shape[0],grid.shape[0],3),dtype=float)

    for i in range(grid.shape[0]):
        for j in range (grid.shape[0]):
            if grid [i,j]:
                img[i,j]=[0,0,0]
    
    if cesta is not None:
        for x in cesta:
            i,j = vrcholy[x]
            img[i,j]=[1,0,0]

    plt.imshow(img)
    plt.axis("off")
    plt.show()
