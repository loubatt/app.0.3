from tkinter import *
from gui import Gui

root = Tk()
root.title("Tools Buat Kerja")
root.iconbitmap(r'D:\\PROJECTS\\PYTHON\\python-app\\Kantor\\AppDesktop\\app.0.3\\images\\turtle.ico')

ui   = Gui(root)
ui.Menu()
ui.Render()
root.geometry("1000x500")
root.mainloop()