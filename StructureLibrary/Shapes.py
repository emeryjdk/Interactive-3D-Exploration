import ipyvolume as ipv
import numpy as np
def SphereHiRes(xp,yp,zp,r,res,Color_):
    thetavec = np.arange(0,np.pi+np.pi/res,np.pi/res) #Create theta vector, spacing is pi/res.
    phivec = np.arange(0,2*np.pi,np.pi/res) #Create phi vector, spacing is pi/res.
    th, ph = np.meshgrid(thetavec, phivec)
    
    X = r*np.sin(th)*np.cos(ph) + xp
    Y = r*np.sin(th)*np.sin(ph) + yp
    Z = r*np.cos(th) + zp
    ipv.pylab.plot_mesh(X, Z, Y, color=Color_, wireframe=False, surface=True,wrapx=True, wrapy=False)
def Arrow(x1,y1,z1, x2,y2,z2, R1,R2, Hi,res,Color):
    v = [x1-x2,y1-y2,z1-z2] # Vector paralles to arrow with same magniitude
    v_ = [0,0,((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)**(1/2)] # vector in the z direction with same maginitude
    cos= -v[2]/(v_[2]) # to find cos take v DOT v_ and devide by their Maginitude squaired
    sin= (1-cos**2)**(1/2) # sin^2 + cos^2 = 1
    v_crosv = [v[1]*v_[2],-v[0]*v_[2],0] # Cross product of v and v_
    Dv_crosV = (v_crosv[0]**2+v_crosv[1]**2)**(1/2) # the Maginitue of the crosproduct
    l = v_crosv[0]/Dv_crosV # used in the Matrix
    m = v_crosv[1]/Dv_crosV # ||
    M = [[l*l*(1-cos)+cos, m*l*(1-cos),     m*sin]   ,
         [l*m*(1-cos),     m*m*(1-cos)+cos, (-l)*sin],
         [0-m*sin,         l*sin,           cos],    ] # Matrix for vector transformation
    C1H = Hi * v_[2] #cilindar one hight
    Hight = np.arange(0,2*C1H,C1H) # List of [0,C1H]
    thetavec = np.arange(0,2*np.pi+np.pi/res,np.pi/res) # res incromets of angles
    C1hi, C1th = np.meshgrid(Hight, thetavec) # mesh to make the plot
    X1_ = np.cos(C1th)*R1
    Y1_ = np.sin(C1th)*R1
    Z1_ = C1hi # to create the x,y,z positns of the cilindar
    Radius = np.arange(0,2*R1,R1)
    P1ra, P1th = np.meshgrid(Radius, thetavec)
    X2_ = np.cos(P1th)*P1ra
    Y2_ = np.sin(P1th)*P1ra
    Z2_ = P1ra*0 # to create the x,y,z positns of the bottom cercle
    if R2 <= R1: # of the radisu of the cone is less then the radius of he cilindar
        X3_ = X2_
        Y3_ = Y2_
        Z3_ = Z2_+C1H
    else:
        Radius = np.arange(0,2*R2,R2)
        P2ra, P2th = np.meshgrid(Radius, thetavec)
        X3_ = np.cos(P2th)*P2ra
        Y3_ = np.sin(P2th)*P2ra
        Z3_ = P2ra*0+C1H # to create the x,y,z positns of the top cercle
    C2H = (1 - Hi) * v_[2] # the hight of the cone
    Hight = np.arange(0,2*C2H,C2H)
    C2hi, C2th = np.meshgrid(Hight, thetavec)
    X4_ = np.cos(C2th)*R2*-(C2hi/C2H-1)
    Y4_ = np.sin(C2th)*R2*-(C2hi/C2H-1)
    Z4_ = C2hi+C1H # to create the x,y,z positns of the cone
    #convert!!
    X1 = M[0][0]*X1_ + M[0][1]*Y1_ + M[0][2]*Z1_ +x1
    Y1 = M[1][0]*X1_ + M[1][1]*Y1_ + M[1][2]*Z1_ +y1
    Z1 = M[2][0]*X1_ + M[2][1]*Y1_ + M[2][2]*Z1_ +z1

    X2 = M[0][0]*X2_ + M[0][1]*Y2_ + M[0][2]*Z2_ +x1
    Y2 = M[1][0]*X2_ + M[1][1]*Y2_ + M[1][2]*Z2_ +y1
    Z2 = M[2][0]*X2_ + M[2][1]*Y2_ + M[2][2]*Z2_ +z1
    
    X3 = M[0][0]*X3_ + M[0][1]*Y3_ + M[0][2]*Z3_ +x1
    Y3 = M[1][0]*X3_ + M[1][1]*Y3_ + M[1][2]*Z3_ +y1
    Z3 = M[2][0]*X3_ + M[2][1]*Y3_ + M[2][2]*Z3_ +z1
    
    X4 = M[0][0]*X4_ + M[0][1]*Y4_ + M[0][2]*Z4_ +x1
    Y4 = M[1][0]*X4_ + M[1][1]*Y4_ + M[1][2]*Z4_ +y1
    Z4 = M[2][0]*X4_ + M[2][1]*Y4_ + M[2][2]*Z4_ +z1
    
    #Plot everything
    ipv.pylab.plot_mesh(X1, Y1, Z1, color=Color, wireframe = False,surface=True,wrapx=True,wrapy=False)
    ipv.pylab.plot_mesh(X2, Y2, Z2, color=Color, wireframe = False,surface=True,wrapx=True,wrapy=False)
    ipv.pylab.plot_mesh(X3, Y3, Z3, color=Color, wireframe = False,surface=True,wrapx=True,wrapy=False)
    ipv.pylab.plot_mesh(X4, Y4, Z4, color=Color, wireframe = False,surface=True,wrapx=True,wrapy=False)
def unetCellBoundry(Size = 1):
    A = np.array([0.,0.,0.,0.,1.,1.,1.,1.,1.,1.,0.,0.,0.,1.,1.,0.])*Size
    B = np.array([0.,1.,1.,1.,1.,1.,1.,0.,0.,0.,0.,0.,1.,1.,0.,0.])*Size
    C = np.array([0.,0.,1.,0.,0.,1.,0.,0.,1.,0.,0.,1.,1.,1.,1.,1.])*Size
    ipv.pylab.plot(A,B,C, color='black')
