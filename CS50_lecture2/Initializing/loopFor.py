names = ['Alice', 'Bob', 'Charlie']

times = int(input("Enter a number: "))
for i in range(times):
    print(i)

for name in names:
    print(name)

largo = len(names)
index = int(input(f"Enter the index of the array (length:{largo}): "))
print(names[index])