#ticketing
#import tkinter
from tkinter import *

#define ticket class
class Ticket:

    def __init__(self, time, price, capacity):
        self._time = time
        self._price = price
        self._capacity = capacity
        tickets.append(self)
        ticket_times.append(self._time)

#create list to store objects 
tickets = []
ticket_times = []

#create objects
Ticket("10am", 5, 150)
Ticket("3pm", 5, 150)
Ticket("8pm", 12, 250)

#create main window
root = Tk()
root.title("Ticketing")
root.geometry('330x300')
root.configure(background='pink')

#create labels for all the info
title_lbl = Label(root, text="Current Showings").grid(row=0, columnspan=3)
ten_lbl = Label(root, text="10am - 150 available/150 capacity - $5 per ticket").grid(row=1, columnspan=3)
three_lbl = Label(root, text="3pm - 150 available/150 capacity - $5 per ticket").grid(row=2, columnspan=3)
eight_lbl = Label(root, text="8pm - 120 available/250 capacity - $12 per ticket").grid(row=3, columnspan=3)

#create the dropdown menu to pick a show
selected_time = StringVar()
selected_time.set(ticket_times[0])
times_drop = OptionMenu(root, selected_time, *ticket_times)
times_drop.grid(row=4, column=1)

#start main window running
root.mainloop()
