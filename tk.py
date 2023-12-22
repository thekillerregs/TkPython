# OOP :D :D :D :D

class model(object):

    # constructor
    def __init__(self, numlayers, numunits, name):
        self.layers = numlayers  # attributes
        self.units = numunits
        self.name = name
        self.weights = 1

    def howManyUnits(self):
        totalUnits = self.layers * self.units
        print(f'There are {totalUnits} units in the model')

    def train(self, x):
        self.weights += x
        return self.weights

    def __str_(self):
        return self.name

m1 = model(2, 5, 'TkModel')

m1.howManyUnits()

print(m1.train(2.5))
