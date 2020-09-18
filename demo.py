import numpy as np
import matplotlib.pyplot as plt
from txtop.readfile import get_lines,item_base
from util.kinematic import get_poseKinematic
import cv2

lines=get_lines('data','CVPR19_MSRA_CrossInfoNet.txt')
hs3ds=item_base(lines[0:100],mode=2)
hs3ds=np.asarray(hs3ds).reshape(-1,21,3)
link,color=get_poseKinematic(rule='hand_21')
background=np.zeros((240,320))
background[0,0]=1

_,ax=plt.subplots(2,2)
"""
ax[0,0]: image show 
ax[0,1]: pose 2d
ax[1,0]: pose with image
ax[1,1]: pose 3d
"""



class NaivePltVisualization():
    def __init__(self,imglist,s2ds,cam_info,rule):
        self.imglist=imglist
        self.s2ds=s2ds
        self.cam_info=cam_info
        self.rule=rule
        self.gen_camera_matrix()
        self.assert_data()
    def assert_data(self):
        flag_im=flag_pose=False
        if self.imglist is not None:
            self.imgslen=len(self.imglist)
            flag_im=True
        if self.s2ds is not None:
            self.s2dslen=len(self.s2ds)
            flag_pose=True
        if flag_im and flag_pose:
            assert self.imgslen==self.s2dslen,'__error-data-len__'
        if not flag_im and not flag_pose:
            print("no valid data: ims or pose")
            raise
        return
    def gen_camera_matrix(self):
        camera_matrix=np.eye(3)
        camera_matrix[0,0]=self.cam_info[0]
        camera_matrix[1,1]=self.cam_info[1]
        camera_matrix[0,2]=self.cam_info[2]
        camera_matrix[1,2]=self.cam_info[3]
        self.camera_matrix=camera_matrix

    def read_images(self):
        imgs=[]
        for i in range(self.imgslen):
            im=cv2.imread(self.imglist[i])
            imgs.append(im)
        return imgs
    @staticmethod
    def draw_s2d(img,s2d,fig,rule):
        if rule is not None:
            link,color=get_poseKinematic(rule)
        else:
            raise
        ax=fig.add_subplot(111)
        ax.imshow(img)
        ax.scatter(s2d[:,0],s2d[:,1])
        for link_,color_ in zip(link,color):
            ax.plot(s2d[link_][:,0],s2d[link_][:,1],c=color_)
        plt.show()

    def draw_s3d(self):
        pass
    def draw_alls(self):
        pass
    def animate(self):
        pass

# for i in range(100):
#     ax[0,0].imshow(background)
#     ax[0,0].scatter(hs3ds[i][:,0],hs3ds[i][:,1])
#     for j in range(21):
#         ax[0,0].text(hs3ds[i][j,0],hs3ds[i][j,1],s=str(j),fontsize=10)
#     for color_,link_ in zip(color,link):
#         ax[0,0].plot(hs3ds[i][link_][:,0],hs3ds[i][link_][:,1],c=color_,)
#     plt.pause(0.1)
#     ax[0,0].cla()

