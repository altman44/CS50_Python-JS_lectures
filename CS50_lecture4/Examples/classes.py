class Flight:
    # __init__ method will take the parameters (self as the first one) to instantiate an object
    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration

def main():
    # Create flight
    f = Flight(origin="New York", destination="Paris", duration=540)

    # Change the value of a variable.
    f.duration += 10

    # Print details about flight.
    print(f.origin)
    print(f.destination)
    print(f.duration)

# if I'm running this particular file named "classes.py"
if __name__ == "__main__":
    main()