import Miners
from tkinter import *
import node_constants

root = Tk()
root.geometry("500x500")
frame = Frame(root)
frame.pack()

leftframe = Frame(root)
leftframe.pack(side=LEFT)

rightframe = Frame(root)
rightframe.pack(side=RIGHT)

label = Label(frame, text = "Welcome to the multitool! Select your tool:")
label.pack()

button1 = Button(leftframe, text = "Button1")
button1.pack(padx = 3, pady = 3)
button2 = Button(rightframe, text = "Button2")
button2.pack(padx = 3, pady = 3)

print("The number of impure iron nodes is ", node_constants.IRON_IMPURE)
print("The number of normal iron nodes is ", node_constants.IRON_NORMAL)
print("The number of pure iron nodes is", node_constants.IRON_PURE)

root.title("Satisfactory Multitool")
root.mainloop()