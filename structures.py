# Add goals and approach.

def FCC(L_x,L_y,L_z):
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
                #in theory this could be used to remod other atoms to make cubic or BCC structure
                else:
    #the x, y, z limits
    ipv.xyzlim(0,10) #define as a function highest of L_xyz
    #the color and size the Na and Cl atoms
    ipv.scatter(np.array(Clx), np.array(Cly), np.array(Clz), marker = 'sphere', size = 6.5, color = "green")
    ipv.scatter(np.array(Nax), np.array(Nay), np.array(Naz), marker = 'sphere', size = 4, color = "red",)
    ipv.show()

