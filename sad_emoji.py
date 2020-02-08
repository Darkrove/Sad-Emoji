from tkinter import *
root = Tk()
'''center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r'''

myCanvas = Canvas(root,bg="lime", height=300, width=300)
myCanvas.pack()
#x=150,y=150,r=100
myCanvas.create_oval(50,50,250,250,fill="yellow",width=5)

#x=150,y=220,r=50
arc = myCanvas.create_arc(100, 170, 200, 270, start=30, extent=120,style="arc",width=4)

#x=110,y=125,r=15
myCanvas.create_oval(95,110,125,140,fill="black")
#x=190,y=125,r=15
myCanvas.create_oval(175,110,205,140,fill="black")
#x=150,y=30
myCanvas.create_text(150,30,text="Frowning Face")
root.mainloop()
