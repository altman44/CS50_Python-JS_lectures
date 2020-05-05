# the function must be declared before it is called

def square(x):
    return x * x

def main():
    for i in range(1,10):
        print("{} squared is {}".format(i, square(i)))

# if i'm currently running this particular file (functions.py):
if __name__ == "__main__":
    main()