import tkinter
from PIL import Image,ImageTk

class BgImage():
    def __init__(self,parent,url):
        self.new_pic = ImageTk.PhotoImage(Image.open(url).resize((400, 300))) 
        self.label = tkinter.Label(parent, image=self.new_pic)