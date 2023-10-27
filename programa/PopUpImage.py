import tkinter
from PIL import Image,ImageTk


class PopUpImage():
    def __init__(self,parent,url):
        self.new_pic = ImageTk.PhotoImage(Image.open(url).resize((100, 120))) 
        self.label = tkinter.Label(parent, image=self.new_pic)