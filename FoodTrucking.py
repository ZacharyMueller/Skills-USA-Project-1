from tkinter import *
from tkinter import ttk

class FoodTruck():
    
    def __init__(self, items):
        self.items = items

    def order(self, order):
        orderTotal = 0
        for item in order:
            orderTotal += self.items[item]
        self.salesTotal += orderTotal
        return orderTotal

    
class DisplayFoodTruck():
    def __init__(self, foodTruck):
        self.truck = foodTruck
        self.items = foodTruck.items
        #Sets up our window
        self.root = Tk()
        self.root.title("Contestant 1875, Project 1")
        self.total = StringVar()
        self.frame = ttk.Frame()

        self.dayTotal = StringVar()
        self.dayTotal.set('$' + str(0))

        self.frame.grid(column=0, row=0, sticky=(N, W, E, S))
        
        self.displayItems(self.frame)

        #Creating Order Button

        button = ttk.Button(self.frame, text='order', command=self.submitOrder)
        button.grid(row=len(self.items) + 4, column=1, columnspan=2)
        #New Day Button to reset total sales

        newDayButton = ttk.Button(self.frame, text="New Day", command=self.resetSalesTotal)
        newDayButton.grid(row=2, column=1, columnspan=2)

        self.totalText = ttk.Label(self.frame, text="Total: ")
        self.totalText.grid(row=len(self.items) + 5, column=1)
        self.orderTotal = ttk.Label(self.frame, textvariable=self.total)
        self.orderTotal.grid(row=len(self.items) + 5, column=2)

        #Error Display Label
        self.error = StringVar()
        self.errorLabel = ttk.Label(self.frame, textvariable=self.error)
        self.errorLabel.grid(row=len(self.items) + 6, column=1, columnspan=2)

        self.totalSalesLabel = ttk.Label(self.frame, textvariable=self.dayTotal).grid(row=1, column=2)
        self.totalSalesText = ttk.Label(self.frame, text="Total of all Sales").grid(row=1, column=1)

        for child in self.frame.winfo_children():
            child.grid_configure(padx=6, pady=6)
        

    def displayItems(self, frame):
        #Will assign each item to an instance of a class 
        #Where each item will have an entry box variable
        self.itemsDisplay = []
        for item in self.items:
            instance = DisplayItem(item, self.items[item])
            self.itemsDisplay.append(instance)
        
        for x in range(len(self.itemsDisplay)):
            item = self.itemsDisplay[x]
            row = x + 3
            item.createFields(frame, row)

    def submitOrder(self):
        listOfTotals = []
        try:
            for item in self.itemsDisplay:

                input = item.itemVariable.get().strip('$')

                if input != '':
                    if int(input) < 0:
                        self.error.set("Error: Enter a positive number")
                        break
                    listOfTotals.append(int(input))
                
            self.dayTotal.set('$' + str(int(self.dayTotal.get().strip('$')) + sum(listOfTotals)))
            self.total.set('$' + str(sum(listOfTotals)))
            self.error.set("")
        except:
            self.error.set("Error: Enter a number")
        return self.total

    def resetSalesTotal(self):
        #At the start of a new day, we can reset salesTotal
        self.dayTotal.set(str(0))

    def start(self):
        self.root.mainloop()

class DisplayItem():
    def __init__(self, item, price):
        self.itemText = f"{item} (${str(price)})"
        self.itemVariable = StringVar()

    def createFields(self, parent, row):
        self.label = ttk.Label(parent, text=f"{self.itemText}").grid(column=1, row=row)
        self.quantity = ttk.Entry(parent, width=2, textvariable=self.itemVariable).grid(column=2, row=row)

