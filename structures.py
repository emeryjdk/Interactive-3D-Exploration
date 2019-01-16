def FCC(L_x,L_y,L_z):
    x=[]
    y=[]
    z=[]
    for O in range(L_x):
        for S in range(L_y*L_z):
            x.append(float(O))
    for O in range(L_x):
        for S in range(L_y):
            for A in range(L_z):
                y.append(float(S))
    for O in range(L_y):
        for S in range(L_x):
            for A in range(L_z):
                z.append(float(A))

    for O in range(L_x-1):
        for S in range((L_y-1)*(L_z)):
            x.append(float(O+.5))  
    for O in range(L_x-1):
        for S in range(L_y-1):
            for A in range(L_z):
                y.append(float(S+.5))
    for O in range(L_y-1):
        for S in range(L_x-1):
            for A in range(L_z):
                z.append(float(A))
            
    for O in range(L_x-1):
        for S in range((L_y)*(L_z-1)):
            x.append(float(O+.5))
    for O in range(L_x-1):
        for S in range(L_y):
            for A in range(L_z-1):
                y.append(float(S))
    for O in range(L_y):
        for S in range(L_x-1):
            for A in range(L_z-1):
                z.append(float(A+.5))
            
    for O in range(L_x):
        for S in range((L_y-1)*(L_z-1)):
            x.append(float(O))
    for O in range(L_x):
        for S in range(L_y-1):
            for A in range(L_z-1):
                y.append(float(S+.5))
    for O in range(L_y-1):
        for S in range(L_x):
            for A in range(L_z-1):
                z.append(float(A+.5))
    X = np.array(x)
    Y = np.array(y)
    Z = np.array(z)

    #remods atoms ond the back face so that when it is shifted no atoms are out of the crystil
    NX = np.concatenate((X[0:(L_y*L_z*(L_x-1))],X[L_y*L_z*L_x:-((L_y-1)*(L_z-1))]), axis = None)+.5
    NY = np.concatenate((Y[0:(L_y*L_z*(L_x-1))],Y[L_y*L_z*L_x:-((L_y-1)*(L_z-1))]), axis = None)
    NZ = np.concatenate((Z[0:(L_y*L_z*(L_x-1))],Z[L_y*L_z*L_x:-((L_y-1)*(L_z-1))]), axis = None)
    Nx = []
    Ny = []
    Nz = []

    #Na+ atoms on the x=0 face
    for O in range((L_y)*(L_z-1)):
        Nx.append(0.0)
    for O in range(L_y):
        for S in range(L_z-1):
            Ny.append(float(O))
    for O in range(L_y):
        for A in range(L_z-1):
            Nz.append(float(A+.5))
        
    for O in range((L_y-1)*(L_z)):
        Nx.append(0.0)
    for O in range(L_z):
        for S in range(L_y-1):
            Ny.append(float(S+.5))
    for O in range(L_z):
        for A in range(L_y-1):
            Nz.append(float(O))#do real math
    NX = np.concatenate((np.array(Nx),NX), axis = None)
    NY = np.concatenate((np.array(Ny),NY), axis = None)
    NZ = np.concatenate((np.array(Nz),NZ), axis = None)
    ipv.xyzlim(0,10)
    ipv.scatter(X, Y, Z, marker = 'sphere', size = 6.4, color = "green")
    ipv.scatter(NX, NY, NZ, marker = 'sphere', size = 4, color = "red",)
    ipv.show()