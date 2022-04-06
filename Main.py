from tkinter import *
from tkinter import ttk
from FoodTrucking import FoodTruck, DisplayFoodTruck


#Items are not hard coded into the Food Truck class and are changeable
items = {'Hot Dog': 2.50, 'Brat': 3.50, 'Hamburger': 5.00,
         'Fries': 2.00, 'Soda': 2.00, 'water': 0}

foodTruck = FoodTruck(items)
truckDisplay = DisplayFoodTruck(foodTruck)
truckDisplay.start()


