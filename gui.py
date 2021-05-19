from tkinter import *
from PIL import ImageTk, Image
import cartoonifyvid as cr
import cartoonifyimg as ci
import pencilSketch as ps


def image():
    ci.cartoonimg()
def video():
    cr.cartoonvid()
def sketch():
    ps.pencilSketch()

    
window=Tk()
window.geometry('400x400')
window.title('Cartoonify Your Image ! ~ Lokesh')
window.configure(background='white')
label=Label(window,background='#CDCDCD', font=('calibri',30,'bold'))


#Create canvas
my_canvas = Canvas(window,width=500,height=600)
my_canvas.pack(fill="both", expand=True)

img= Image.open(r"C:\Users\LOKESH\OneDrive\Desktop\Cartoonify_Capstone\sukuna.jpg")
img = img.resize((420, 480), Image.ANTIALIAS)
bg = ImageTk.PhotoImage(img)

#Set image in canvas
my_canvas.create_image(0,0,anchor="nw",image=bg)

pic=Button(window,text="Choose Image to Cartoonify",command = image, padx=10,pady=5)
pic.configure(background='#364156', foreground='white',font=('calibri',10,'bold'))
pic.pack(side=TOP,pady=50)
pic.place(x=108, y=240)

vid=Button(window,text="Open Camera for Video",command = video, padx=10,pady=5)
vid.configure(background='#364156', foreground='white',font=('calibri',10,'bold'))
vid.pack(side=TOP,pady=50)
vid.place(x=120, y=200)

sketch=Button(window,text="Pencil Sketch Effect",command = sketch, padx=10,pady=5)
sketch.configure(background='#364156', foreground='white',font=('calibri',10,'bold'))
sketch.pack(side=TOP,pady=50)
sketch.place(x=130, y=280)
