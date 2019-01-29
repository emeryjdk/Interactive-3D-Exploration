# Add goals and approach.
import ipyvolume as ipv
import numpy as np
def NACL(L_x,L_y=None,L_z=None,ColorNa='red',ColorCl='green'):
    if L_y == None:
        L_y = L_x
    if L_z == None:
        L_z = L_x
    if L_x%1 !=0 or L_x%1 !=0 or L_x%1 !=0:
        print("All inputs must be integers.")
        return()
    if L_x > L_y:
        Max = L_x
    else: Max = L_y
    if L_z > Max:
        Max = L_z#defined as a function highest of L_xyz
    #define a list of positions to append to
    Clx=[]
    Cly=[]
    Clz=[]
    Nax=[]
    Nay=[]
    Naz=[]
    #for each layer of the atom in the x direction. the *2-1 is so that L_x is the number of unit cells
    for O in range(L_x*2-1):
        #for each layer in the y direction.
        for S in range(L_y*2-1):
            #for each layer in the z direction.
            for A in range(L_z*2-1):
                #if in this position there shoud be a Cl atom
                if (O+S+A)%2 == 0:
                    #the 0.5 is becasue L_xyz was multiplied by 2
                    Clx.append(float(O*.5))
                    Cly.append(float(S*.5))
                    Clz.append(float(A*.5))
                #if there should be a Na atom
                elif(O+S+A)%2 == 1:
                    Nax.append(float(O*.5))
                    Nay.append(float(S*.5))
                    Naz.append(float(A*.5))
                #if there should not be an atom
                #in theory this could be used to remove other atoms to make cubic or BCC structure
    #the x, y, z limits
    ipv.xyzlim(0,Max)
    #the color and size the Na and Cl atoms
    ipv.scatter(np.array(Clx), np.array(Cly), np.array(Clz), marker = 'sphere', size = 6.5, color = "green")
    if len(Nax) == 0:
        ipv.show()
        return()
    ipv.scatter(np.array(Nax), np.array(Nay), np.array(Naz), marker = 'sphere', size = 4, color = "red",)
    ipv.show()
def BCC(L_x,L_y,L_z,Color = 'red'):
    if L_x > L_y:
        Max = L_x
    else: Max = L_y
    if L_z > Max:
        Max = L_z#defined as a function highest of L_xyz
    #for each layer of the atom in the x direction. the *2-1 is so that L_x is the number of unit cells
    Ax = []
    Ay = []
    Az = []
    for O in range(L_x*2-1):
        #for each layer in the y direction.
        for S in range(L_y*2-1):
            #for each layer in the z direction.
            for A in range(L_z*2-1):
                if (O+S+A)%2 == 0:
                    #the 0.5 is becasue L_xyz was multiplied by 2
                    Ax.append(float(O*.5))
                    Ay.append(float(S*.5))
                    Az.append(float(A*.5))
                elif S%2 == 1 and O%2 == 1 and A%2 == 1:
                    Ax.append(float(O*.5))
                    Ay.append(float(S*.5))
                    Az.append(float(A*.5))
                #if there should not be an atom
                #in theory this could be used to remove other atoms to make cubic or BCC structure
    #the x, y, z limits
    ipv.xyzlim(0,Max) #define as a function highest of L_xyz
    ipv.scatter(np.array(Ax), np.array(Ay), np.array(Az), marker = 'sphere', size = 6.5, color = Color)
    ipv.show()
def FCC(L_x,L_y,L_z,Color = 'red'):
    if L_x > L_y:
        Max = L_x
    else: Max = L_y
    if L_z > Max:
        Max = L_z#defined as a function highest of L_xyz
    Ax = []
    Ay = []
    Az = []
    #for each layer of the atom in the x direction. the *2-1 is so that L_x is the number of unit cells
    for O in range(L_x*2-1):
        #for each layer in the y direction.
        for S in range(L_y*2-1):
            #for each layer in the z direction.
            for A in range(L_z*2-1):
                if (O+S+A)%2 == 0:
                    #the 0.5 is becasue L_xyz was multiplied by 2
                    Ax.append(float(O*.5))
                    Ay.append(float(S*.5))
                    Az.append(float(A*.5))
                elif S%2 == 1 and O%2 == 1 and A%2 == 0:
                    Ax.append(float(O*.5))
                    Ay.append(float(S*.5))
                    Az.append(float(A*.5))
                #if there should not be an atom
                #in theory this could be used to remove other atoms to make cubic or BCC structure
    #the x, y, z limits
    ipv.xyzlim(0,Max) #defined as a function highest of L_xyz
    ipv.scatter(np.array(Ax), np.array(Ay), np.array(Az), marker = 'sphere', size = 6.5, color = Color)
    ipv.show()
def SC(L_x,L_y,L_z,Color = 'red'):
    if L_x > L_y:
        Max = L_x
    else: Max = L_y
    if L_z > Max:
        Max = L_z#defined as a function highest of L_xyz
    Ax = []
    Ay = []
    Az = []
    for O in range(L_x):
        #for each layer in the y direction.
        for S in range(L_y):
            #for each layer in the z direction.
            for A in range(L_z):
                Ax.append(float(O))
                Ay.append(float(S))
                Az.append(float(A))
    #the x, y, z limits
    ipv.xyzlim(0,Max) #defined as a function highest of L_xyz
    ipv.scatter(np.array(Ax), np.array(Ay), np.array(Az), marker = 'sphere', size = 6.5, color = Color)
    ipv.show()