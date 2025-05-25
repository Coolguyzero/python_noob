from tkinter import *

root = Tk()

root.title ("LoRAMD")
root.geometry("500x600")

btn1 = Button(root, text="function1")
btn1.pack(side=LEFT,padx=10,pady=10)

btn2 = Button(root, text="function2")
btn2.pack(side=CENTER,padx=10,pady=10)

btn3 = Button(root, text="function3")
btn3.pack(side=RIGHT,padx=10,pady=10)

root.mainloop()
