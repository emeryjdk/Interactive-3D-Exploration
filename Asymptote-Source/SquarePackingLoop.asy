//settings.outformat = "pdf";       //Enable to output pdf files directly.
//settings.outformat = "prc";     //Enable to output prc files to load into TeX
import solids;                    //Enables filling and drawing of surfaces of revolution
import three;											//Enables 3D plotting
size(7.5cm,0);
viewportmargin=4mm;
currentprojection=orthographic(
camera=(5,5,1000),
up=(-1,0,0),
target=(5,5,0),
zoom=0.5,
center=true); 										//Center puts rotation at center.
pen color1=0.80*blue+0.20*white+opacity(1);		//High opacity - for solid sphere slices.
pen color2=0.20*blue+0.80*white+opacity(0.8);   //Medium opacity - for middle atom.
pen color3=blue+white+opacity(0.1);   //Low opacity - for full atoms.


real r=1;												  //Atomic radius
real a=2r;												//Lattice Parameter

render render=render(compression=0.5,merge=true); 				 //Set render field. 0.5 is low resolution.

//Create transparent unit spheres to represent full atoms.

for (int i=0; i<5; ++i)
{
	for (int j=0; j<5; ++j)
	{
		draw(shift(a*i,a*j,0)*unitsphere, color1, render);
	}
}

for (int i=0; i<4; ++i)
{
	for (int j=0; j<4; ++j)
	{
		draw(shift(a/2+a*i,a/2+a*j,a/2)*unitsphere, color2, render);
	}
}

/*xaxis3(Label("$x$",1),xmax=a+1,Arrow3);
yaxis3(Label("$y$",1),ymax=a+1,Arrow3);
zaxis3(Label("$z$",1),zmax=a+1,Arrow3);*/
		