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

#
def showings():
    showings_info.set("")
    for t in tickets:
        showings_info.set(t._time + " - " + str(t._capacity )+ " available/" + str(t._capacity) +" capacity - $" + str(t._price) + " per ticket" + "\n")

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
root.geometry('450x300')
root.configure(background='pink')

#create labels for all the info
showings_info = StringVar()
showings()
title_lbl = Label(root, text="Current Showings").grid(row=0, columnspan=3)
options_lbl = Label(root, textvariable=showings_info).grid(row=1, columnspan=3)

#create the dropdown menu to pick a show
selected_time = StringVar()
selected_time.set(ticket_times[0])
times_drop = OptionMenu(root, selected_time, *ticket_times)
times_drop.grid(row=4, column=0)

#entry field for entering how many tickets
no_tickets = StringVar()
no_tickets.set("Number of tickets")
tickets_entry = Entry(root, textvariable=no_tickets).grid(row=4, column=1)

#button to buy tickets
buy_btn = Button(root, text="Buy Tickets").grid(row=4, column=2)

#create summary labels
summary_lbl = Label(root, text="Summary").grid(row=5, columnspan=3)
sold_lbl = Label(root, text="0 tickets sold today").grid(row=6, columnspan=3)
earned_lbl = Label(root, text="$0 earned today").grid(row=7, columnspan=3)


#start main window running
root.mainloop()
