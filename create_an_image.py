from tkinter import *
from random import *
size=750
okno=Tk()
platno=Canvas(okno, bg="#000000", width=size,height=size)

def draw_halfcircles(x,y):
	platno.create_arc(x,y,y,x,fill=cc(),start=270.0,extent=90.0)
	platno.create_arc(size-x,size-y,size-y,size-x,fill=cc(),start=90.0,extent=90.0)
	platno.create_arc(x,size-y,y,size-x,fill=cc(),start=0.0,extent=90.0)
	platno.create_arc(size-x,y,size-y,x,fill=cc(),start=180.0,extent=90.0)
def draw(x,y):
	platno.create_rectangle(x,y,y,x,outline=cc(),width=3.0)
	platno.create_rectangle(size-x,size-y,size-y,size-x,outline=cc())
	platno.create_rectangle(x,size-y,y,size-x, outline=cc(),width=3.0)
	platno.create_rectangle(size-x,y,size-y,x,outline=cc())	
	
	platno.create_oval(x,y,y,x,outline=cc())
	platno.create_oval(size-x,size-y,size-y,size-x,outline=cc())
	platno.create_oval(x,size-y,y,size-x,outline=cc())
	platno.create_oval(size-x,y,size-y,x,outline=cc())	
	
	platno.create_line(x,y,y,x,fill=cc())
	platno.create_line(size-x,size-y,size-y,size-x,fill=cc(),width=3.0)
	platno.create_line(x,size-y,y,size-x,fill=cc())
	platno.create_line(size-x,y,size-y,x,fill=cc(),width=3.0)

def cc():
	r=randint(0,255)
	g=randint(0,255)
	b=randint(0,255)
	rgb=change_to_hex([r,g,b])
	the_color='#{}{}{}'.format(rgb[0],rgb[1],rgb[2])
	return the_color

def change_to_hex(list):
	new_list=[]
	for i in list:
		print(hex(i)[2:])
		if len(hex(i)[2:])==1:
			new_list.append("1"+hex(i)[2:])
		else:
			new_list.append(hex(i)[2:])

	return new_list

for i in range(4):
	r1=randint(0,size)
	r2=randint(0,size)
	draw(r1,r2)

draw_halfcircles(r1,r2)

platno.pack()
okno.mainloop()