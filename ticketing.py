#ticketing
#import tkinter
from tkinter import *

#create variables for stuff
tickets_sold = 0
dollars_earned = 0

#define ticket class
class Ticket:

    def __init__(self, time, price, capacity):
        self._time = time
        self._price = price
        self._capacity = capacity
        self._available = capacity
        tickets.append(self)
        ticket_times.append(self._time)

    def _buy_tickets(self, qty):
        self._available -= qty

#define function to set main label
def showings():
    showings_info.set("")
    for t in tickets:
        if t._time == "10am":
            showings_info.set(showings_info.get() + t._time + " - " + str(t._available)+ " available/" + str(t._capacity) +" capacity - $" + str(t._price) + " per ticket" + "\n")
        elif t._time == "3pm":
            showings_info.set(showings_info.get() + t._time + " - " + str(t._available)+ " available/" + str(t._capacity) +" capacity - $" + str(t._price) + " per ticket" + "\n")
        elif t._time == "8pm":
            showings_info.set(showings_info.get() + t._time + " - " + str(t._available)+ " available/" + str(t._capacity) +" capacity - $" + str(t._price) + " per ticket" + "\n")

#define function to set summary label
def summary_info():
    sold_info.set(str(tickets_sold) + " tickets sold today")
    earned_info.set("$" + str(dollars_earned) + " earned today")

      
#define function to buy tickets
def buy():
    global tickets_sold
    global dollars_earned
    for t in tickets:
        if t._time == selected_time.get():
            t._buy_tickets(int(no_tickets.get()))
            tickets_sold += int(no_tickets.get())
            cost_sale = int(no_tickets.get()) * t._price
            dollars_earned += cost_sale
    showings()
    summary_info()


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
buy_btn = Button(root, text="Buy Tickets", command=buy).grid(row=4, column=2)

#create summary labels
sold_info = StringVar()
earned_info = StringVar()
summary_info()
summary_lbl = Label(root, text="Summary").grid(row=5, columnspan=3)
sold_lbl = Label(root, textvariable=sold_info).grid(row=6, columnspan=3)
earned_lbl = Label(root, textvariable=earned_info).grid(row=7, columnspan=3)


#start main window running
root.mainloop()
