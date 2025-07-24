 #**Digital clock in Python**

import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

#define the clock label
clock_label = tk.Label(root, font=("Helvetica", 48), background ="black", foreground = "cyan")
clock_label.pack(anchor ="center", fill ="both", expand = True)

#function to update the time
def update_time():
    current_time = strftime("%H:%M:%S %p") #%p is used to display AM/PM
    clock_label.config(text= current_time) # config() method is used to update the label text
    clock_label.after(1000, update_time) # update the time every 1000 milliseconds(1 second)

update_time() #call the function to start the clock
root.mainloop() # start the Tkinter event loop to display the clock