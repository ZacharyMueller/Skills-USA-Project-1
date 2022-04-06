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



#------------------------------------------------------------------

#Items are not hard coded into the Food Truck class and are changeable
items = {'Hot Dog': 2.50, 'Brat': 3.50, 'Hamburger': 5.00,
         'Fries': 2.00, 'Soda': 2.00, 'water': 0}

#For testing purposes 
order = ['Hot Dog', 'Soda', 'Fries']

foodTruck = FoodTruck(items)
foodTruck.order(order)

print(foodTruck.salesTotal)