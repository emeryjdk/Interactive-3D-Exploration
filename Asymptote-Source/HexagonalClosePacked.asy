settings.outformat = "pdf";       //Enable to output pdf files directly.
//settings.outformat = "prc";     //Enable to output prc files to load into TeX
import solids;                    //Enables filling and drawing of surfaces of revolution
import three;											//Enables 3D plotting
size(7.5cm,0);
viewportmargin=4mm;
currentprojection=orthographic(
camera=(9,6,2),
up=(0,0,1),
target=(0,0,0),
zoom=0.8,
center=true); 										//Center puts rotation at center.
pen color=blue+white+opacity(0.9);		//High opacity - for solid sphere slices.
pen color2=blue+white+opacity(0.1);   //Low opacity - for full atoms.
pen color3=blue+white+opacity(0.7);   //Medium opacity - for middle atom.

real r=1;												  //Atomic radius
real a=2r;												//Lattice Parameter
real xproj = cos(30*pi/180);
real yproj = sin(30*pi/180);
real zproj = sqrt(8/3);

pair F(real x) {return (x,sqrt(r^2-x^2));}		//Equation for a unit circle in 2D - for rotation.

path p1=graph(F,0,-r,operator ..)--(-r,0)--(0,0)--cycle;   //Create path to be rotated.
path3 p31=rotate(90,Y)*path3(p1);													 //Rotate path 90 degrees about Y.

render render=render(compression=0.5,merge=true); 				 //Set render field. 0.5 is low resolution.

//Translate and revolve partial spheres... not very systematic.
draw(surface(shift(0,0,0)*revolution(p31,Z,240,360)),color,render);
draw(surface(shift(a*cos(30*pi/180),-a*sin(30*pi/180),0)*revolution(p31,Z,0,60)),color,render);
draw(surface(shift(0,a,0)*revolution(p31,Z,180,240)),color,render);
draw(surface(shift(a*cos(30*pi/180),-a*sin(30*pi/180)+a,0)*revolution(p31,Z,60,180)),color,render);
draw(surface(shift(0,0,sqrt(8/3)*a)*rotate(180,X)*rotate(270,Z)*revolution(p31,Z,270,390)),color,render);
draw(surface(shift(a*cos(30*pi/180),-a*sin(30*pi/180),sqrt(8/3)*a)*rotate(180,X)*rotate(90,Z)*revolution(p31,Z,30,90)),color,render);
draw(surface(shift(0,a,sqrt(8/3)*a)*rotate(180,X)*rotate(90,Z)*revolution(p31,Z,210,270)),color,render);
draw(surface(shift(a*cos(30*pi/180),-a*sin(30*pi/180)+a,sqrt(8/3)*a)*rotate(180,X)*rotate(270,Z)*revolution(p31,Z,90,210)),color,render);


//Create and translate edges for partial spheres.
surface s11=rotate(90,Y)*surface(p1);
surface s12=rotate(180,Y)*rotate(-90,X)*rotate(-30,Y)*surface(p1);
surface s21=shift(a*cos(30*pi/180),-a*sin(30*pi/180),0)*rotate(90,Y)*surface(p1);
surface s22=shift(a*cos(30*pi/180),-a*sin(30*pi/180),0)*rotate(90,Y)*rotate(-60,X)*surface(p1);
surface s31=shift(0,a,0)*rotate(90,Y)*rotate(180,X)*surface(p1);
surface s32=shift(0,a,0)*rotate(90,Y)*rotate(120,X)*surface(p1);
surface s41=shift(a*cos(30*pi/180),a*sin(30*pi/180),0)*rotate(90,Y)*rotate(90,Z)*surface(p1);
surface s42=shift(a*cos(30*pi/180),a*sin(30*pi/180),0)*rotate(90,Y)*rotate(-60,X)*surface(p1);
draw(s11,color,render);
draw(s12,color,render);
draw(s21,color,render);
draw(s22,color,render);
draw(s31,color,render);
draw(s32,color,render);
draw(s41,color,render);
draw(s42,color,render);
surface sz11=shift(0,0,sqrt(8/3)*a)*rotate(-90,Y)*surface(p1);
surface sz12=shift(0,0,sqrt(8/3)*a)*rotate(-90,Y)*rotate(-120,X)*surface(p1);
surface sz21=shift(a*cos(30*pi/180),-a*sin(30*pi/180),sqrt(8/3)*a)*rotate(270,Y)*rotate(60,X)*surface(p1);
surface sz22=shift(a*cos(30*pi/180),-a*sin(30*pi/180),sqrt(8/3)*a)*rotate(90,Y)*rotate(270,Z)*surface(p1);
surface sz31=shift(0,a,sqrt(8/3)*a)*rotate(270,Y)*rotate(180,X)*surface(p1);
surface sz32=shift(0,a,sqrt(8/3)*a)*rotate(180,Y)*rotate(90,X)*rotate(30,Y)*surface(p1);
surface sz41=shift(a*cos(30*pi/180),a*sin(30*pi/180),sqrt(8/3)*a)*rotate(270,Y)*rotate(60,X)*surface(p1);
surface sz42=shift(a*cos(30*pi/180),a*sin(30*pi/180),sqrt(8/3)*a)*rotate(270,Y)*rotate(180,X)*surface(p1);
draw(sz11,color,render);
draw(sz12,color,render);
draw(sz21,color,render);
draw(sz22,color,render);
draw(sz31,color,render);
draw(sz32,color,render);
draw(sz41,color,render);
draw(sz42,color,render);


//Create transparent unit spheres to represent full atoms.
draw(shift(0,0,0)*scale(0.999*r,0.999*r,0.999*r)*unitsphere, color2, render);
draw(shift(a*cos(30*pi/180),-a*sin(30*pi/180),0)*scale(0.999*r,0.999*r,0.999*r)*unitsphere, color2, render);
draw(shift(0,a,0)*scale(0.999*r,0.999*r,0.999*r)*unitsphere, color2, render);
draw(shift(a*cos(30*pi/180),-a*sin(30*pi/180)+a,0)*scale(0.999*r,0.999*r,0.999*r)*unitsphere, color2, render);

draw(shift(0,0,sqrt(8/3)*a)*scale(0.999*r,0.999*r,0.999*r)*unitsphere, color2, render);
draw(shift(a*cos(30*pi/180),-a*sin(30*pi/180),sqrt(8/3)*a)*scale(0.999*r,0.999*r,0.999*r)*unitsphere, color2, render);
draw(shift(0,a,sqrt(8/3)*a)*scale(0.999*r,0.999*r,0.999*r)*unitsphere, color2, render);
draw(shift(a*cos(30*pi/180),-a*sin(30*pi/180)+a,sqrt(8/3)*a)*scale(0.999*r,0.999*r,0.999*r)*unitsphere, color2, render);

draw(shift(r/cos(30*pi/180),0,sqrt(8/3)*a/2)*scale(0.999*r,0.999*r,0.999*r)*unitsphere, color3, render);



//Labels and measures.
//draw((a*cos(30*pi/180),-a*sin(30*pi/180)+a)--(a*cos(30*pi/180),-a*sin(30*pi/180)+a,sqrt(8/3)*a),red+linewidth(1));
draw((0,a,0)--(0,a,sqrt(8/3)*a),red+linewidth(1));
draw((a*cos(30*pi/180),a-r,0)--(0,a,0),red+linewidth(1));
draw((a*cos(30*pi/180),-a*sin(30*pi/180),0)--(a*cos(30*pi/180),-a*sin(30*pi/180)+r,0),black+linewidth(1));
draw((a*cos(30*pi/180),-a*sin(30*pi/180),-0.02*a)--(a*cos(30*pi/180),-a*sin(30*pi/180),0.02*a),black+linewidth(1));
draw((a*cos(30*pi/180),-a*sin(30*pi/180)+r,-0.02*a)--(a*cos(30*pi/180),-a*sin(30*pi/180)+r,0.02*a),black+linewidth(1));
label("$c$",(0,a,sqrt(8/3)*a/2),E,red);
label("$a$",(a*cos(30*pi/180)/2,a-r/2,0),E,red);
label("$r_0$",(a*cos(30*pi/180),-a*sin(30*pi/180)+r/2,0),S,black);
label("$o$",(0,0,0),NW);

draw((-cos(30*pi/180),sin(30*pi/180),0)--((a+2)*cos(30*pi/180),-(a+2)*sin(30*pi/180),0),Arrow3);
label("$x$",((a+2)*cos(30*pi/180),-(a+2)*sin(30*pi/180),0),S);
draw((0,-1,0)--(0,a+2,0),Arrow3);
label("$y$",(0,a+2,0),S);
zaxis3(Label("$z$",1),zmax=sqrt(8/3)*a+2,Arrow3);

//unitcell
