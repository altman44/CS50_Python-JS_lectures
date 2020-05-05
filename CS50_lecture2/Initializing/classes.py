# functions that begin with double underscore (__) are called special functions as they have special meaning
class Marks:
    # anytime I create a new point this function is executed
    # __init__() gets called whenever a new object of this class is instantiated
    def __init__(self, mark1, mark2):
        self.mark1 = mark1
        self.mark2 = mark2


print("First class:")
p = Marks(3, 5)
print(p.mark1)
print(p.mark2)
print("Second class:")
c = Marks(2,7)
print(c.mark1)
print(c.mark2)

print()

points = set()
points.add(Marks(4, 6))
print("set 'points': {}".format(points))

print()

ob = {'Alexis': Marks(1,8), 'Sophie': Marks(3,6)}
print("Alexis's mark1: {}".format(ob['Alexis'].mark1))
print("Sophie's mark2: {}".format(ob['Sophie'].mark2))

print()

class arr:
    def __init__(self, values):
        self.array = values

objeto = arr([1,2,3])
print(objeto.array[0])

print()

class CreateObject:
    def __init__(self, ob):
        self.ob = ob

obby = CreateObject({'FirstNumber': 5, 'SecondNumber': 8})
print("FirstNumber: {}".format(obby.ob['FirstNumber']))
print("SecondNumber: {}".format(obby.ob['SecondNumber']))

class i:
    def __init__(self, msg):
        print(msg)

i('')
i('Printing something with an object instantiated by a class called "i"')
i('Printing something else')
