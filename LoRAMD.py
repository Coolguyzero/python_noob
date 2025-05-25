from tkinter import *
"""using tkinter for setting workspace"""
root = Tk()
"""by using setting Tk main display and also define as root"""
root.title ("LoRAMD")
"""define display's title"""
root.geometry("500x600")
"""resize display's width/hight when launched right away"""
btn1 = Button(root, text="function1")
btn1.pack(side=LEFT,padx=10,pady=10)
"""added button named as <function1> which is arranged from left(the inside of root)"""
btn2 = Button(root, text="function2")
btn2.pack(side="top",padx=10,pady=10)
"""same with btn1's case but the button arranged from top"""
btn3 = Button(root, text="function3")
btn3.pack(side=RIGHT,padx=10,pady=10)
"""same with btn1's case but the button arranged from right"""
root.mainloop()
"""preventing closing screen"""
