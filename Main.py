from tkinter import *
from tkinter import ttk


class FoodTruck():
    
    def __init__(self, items):
        self.items = items
        self.salesTotal = 0

    def order(self, order):
        orderTotal = 0
        for item in order:
            orderTotal += self.items[item]
        self.salesTotal += orderTotal
        return orderTotal

    def resetSalesTotal(self):
        #At the start of a new day, we can reset salesTotal
        self.salesTotal = 0
    

class DisplayFoodTruck():
    def __init__(self, foodTruck):
        self.truck = foodTruck
        self.items = foodTruck.items
        #Sets up our window
        self.root = Tk()
        self.root.title("Food Truck")
        self.total = 'N/A'
        self.frame = ttk.Frame()
        self.frame.grid(column=0, row=0, sticky=(N, W, E, S))
        
        self.displayItems(self.frame)

        #Creating Order Button

        button = ttk.Button(self.frame, text='order', command=self.submitOrder)
        button.grid(row=len(self.items) + 1, column=2)

        orderTotal = ttk.Label(self.frame, textvariable=self.total)
        orderTotal.grid(row=len(self.items) + 1, column=3)

    def displayItems(self, frame):
        #Will assign each item to an instance of a class 
        #Where each item will have an entry box variable
        self.itemsDisplay = []
        for item in self.items:
            instance = DisplayItem(item, self.items[item])
            self.itemsDisplay.append(instance)
        
        for x in range(len(self.itemsDisplay)):
            item = self.itemsDisplay[x]
            row = x + 1
            item.createFields(frame, row)

    def submitOrder(self):
        print('calculating total')
        self.total = 0
        listOfTotals = []
        for item in self.itemsDisplay:
            input = item.itemVariable.get()
            if input != '':
                listOfTotals.append(int(input))
        self.total = sum(listOfTotals)
        return self.total



    def start(self):
        self.root.mainloop()

class DisplayItem():
    def __init__(self, item, price):
        self.itemText = f"{item} (${str(price)})"
        self.itemVariable = StringVar()

    def createFields(self, parent, row):
        print(f"creating fields for {self.itemText}")
        self.label = ttk.Label(parent, text=f"{self.itemText}").grid(column=1, row=row)
        self.quantity = ttk.Entry(parent, width=2, textvariable=self.itemVariable).grid(column=2, row=row)


        
#------------------------------------------------------------------

#Items are not hard coded into the Food Truck class and are changeable
items = {'Hot Dog': 2.50, 'Brat': 3.50, 'Hamburger': 5.00,
         'Fries': 2.00, 'Soda': 2.00, 'water': 0}

#For testing purposes 
order = ['Hot Dog', 'Soda', 'Fries']

foodTruck = FoodTruck(items)

truckDisplay = DisplayFoodTruck(foodTruck)
truckDisplay.start()


print(foodTruck.salesTotal)