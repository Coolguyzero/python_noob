from tkinter import *
"""using tkinter for setting workspace"""
root = Tk()
"""by using setting Tk main display and also define as root"""
root.title("LoRAMD")
"""define display's title"""
root.geometry("500x600")
"""resize display's width/height when launched right away"""
click_counts = {"function1": 0, "function2": 0, "function3": 0}
"""displaying click counts"""
label = Label(root, text="Click Counts: function1=0, function2=0, function3=0")
"""displaying click counts for each of button"""
label.pack()
def button_clicked(button_name):
    click_counts[button_name] += 1
    label.config(text=f"Click Counts: function1={click_counts['function1']}, function2={click_counts['function2']}, function3={click_counts['function3']}")
"""adding click event"""
btn1 = Button(root, text="function1", command=lambda: button_clicked("function1"))
btn1.pack(padx=0, pady=0)
"""added button named as <function1> which is connected with click counts"""
btn2 = Button(root, text="function2", command=lambda: button_clicked("function2"))
btn2.pack(padx=0, pady=0)
"""added button named as <function2> which is connected with click counts"""
btn3 = Button(root, text="function3", command=lambda: button_clicked("function3"))
btn3.pack(padx=0, pady=0)
"""added button named as <function3> which is connected with click counts"""
root.mainloop()
"""preventing closing screen"""
