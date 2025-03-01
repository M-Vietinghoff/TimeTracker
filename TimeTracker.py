import tkinter as tk

#Stopwatch GUI
#Author: Michaela V

root = tk.Tk()

root.title("Stopwatch")

def Stop_click():
    print("Stop")
    #replace with logic  
    
def Start_click():
    print("Start")  
    #replace with logic  

#Create out buttons
lbl = tk.Label(root, text="Enter a Time and press Start to begin")
lbl.grid(row=0, column=0, padx=10, pady=10)

btn_start = tk.Button(root, text="Start", command=Start_click)
btn_start.grid(row=1, column=1, padx=10,pady=50)

btn_stop = tk.Button(root, text="Stop", command=Stop_click)
btn_stop.grid(row=1, column=2, padx=30, pady=50)

root.mainloop()

# TODO: Install stopwatch logic