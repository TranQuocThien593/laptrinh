filename = input("Enter a file name: ")

try:
    file = open(filename, 'r')
except:
    print("File cannot be opened:", filename)
    exit()

for line in file:
    print(line.rstrip().upper())
