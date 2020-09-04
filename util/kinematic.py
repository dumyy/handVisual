import numpy as np

RED = "#FF0000"
GREEN = "#00FF00"
BLUE = "#0000FF"
PURPLE = "#A327EA"
ORANGE = "#F29721"
GREY = "#6E6672"
PICTON_BLUE = "#44BBF8"
AERO = "#6BC0EA"

def get_poseKinematic(rule="default"):
    kinematic=None
    color=None

    if rule=="hand_21":
        thumb=np.asarray([[0,1],[1,2],[2,3],[3,4]])
        index=np.asarray([[0,5],[5,6],[6,7],[7,8]])
        middle=np.asarray([[0,9],[9,10],[10,11],[11,12]])
        ring=np.asarray([[0,13],[13,14],[14,15],[15,16]])
        little=np.asarray([[0,17],[17,18],[18,19],[19,20]])
        kinematic=np.vstack((thumb,index,middle,ring,little))
        color=[RED]*4+[ORANGE]*4+[GREEN]*4+[BLUE]*4+[PURPLE]*4
    elif rule=="Hand_16":
        thumb=np.asarray([[0,1],[1,2],[2,3]])
        index=np.asarray([[0,4],[4,5],[5,6]])
        middle=np.asarray([[0,7],[7,8],[8,9]])
        ring=np.asarray([[0,10],[10,11],[11,12]])
        little=np.asarray([[0,13],[13,14],[14,15]])
        kinematic=np.vstack((thumb,index,middle,ring,little))
        color=[RED]*3+[ORANGE]*3+[GREEN]*3+[BLUE]*3+[PURPLE]*3
    if (kinematic is None) or (color is None):
        print("There is \"{}\" rule")
    return kinematic,color
