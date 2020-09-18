import numpy as np
import matplotlib.pyplot as plt
from txtop.readfile import get_lines,item_base
from util.kinematic import get_poseKinematic

lines=get_lines('data','CVPR19_MSRA_CrossInfoNet.txt')
hs3ds=item_base(lines[0:100],mode=2)
hs3ds=np.asarray(hs3ds).reshape(-1,21,3)
link,color=get_poseKinematic(rule='hand_21')
background=np.zeros((240,320))
background[0,0]=1

_,ax=plt.subplots(2,2)


for i in range(100):
    ax[0,0].imshow(background)
    ax[0,0].scatter(hs3ds[i][:,0],hs3ds[i][:,1])
    for color_,link_ in zip(color,link):
        ax[0,0].plot(hs3ds[i][link_][:,0],hs3ds[i][link_][:,1],c=color_)
    plt.pause(0.1)
    ax[0,0].cla()
