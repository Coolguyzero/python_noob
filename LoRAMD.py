from tkinter import *
#using tkinter for setting workspace
root = Tk()
#by using setting Tk main display and also define as root"""
root.title("LoRAMD")
#define display's title
root.geometry("500x600")
#resize display's width/height when launched right away
btn1 = Button(root, text="function1")
btn1.pack(padx=0, pady=0)
#added button named as <function1> which is connected with click counts
btn2 = Button(root, text="function2")
btn2.pack(padx=0, pady=0)
#added button named as <function2> which is connected with click counts
btn3 = Button(root, text="function3")
btn3.pack(padx=0, pady=0)
#added button named as <function3> which is connected with click counts
root.mainloop()
#preventing closing screen
