# dictionary
# come on... its called hashmap

D = dict()

D['name'] = 'Tk'

print(D['name'])

print(D.__contains__('name'))

intone = int(input('Enter number 1'))
inttwo = int(input('Enter number 2'))

product = intone * inttwo

newDict = dict()

newDict['firstNumber'] = intone
newDict['secondNumber'] = inttwo
newDict['product'] = product


print(newDict.items())
