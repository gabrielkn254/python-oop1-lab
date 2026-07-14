#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price
    
    def __setattr__(self, name, value):
        if name == "size":
            if name != "Small" or "Medium" or "Large":
                print("size must be Small, Medium, or Large")
        
        self.__dict__[name] = value
    
    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1