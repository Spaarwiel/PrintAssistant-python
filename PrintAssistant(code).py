print("PrintAssistant--v1.0!")
print("")
print("")
print("Hard cover book.")
SquareSpine = input("For squareback book(Board in spine)Enter 1.")
print("")
print("")
print("Please enter bookblock dimensions:")
print("")
A = int(input("Book height:"))
B = int(input("Book Width:"))
C = int(input("Width of the book block spine:"))
D = int(input("Thickness of the board in micron: 1000,1250,1500,1800,2300,3000:"))

if D == 1000:
    Z = B - 5
    X = 8


if D == 1250:
    Z = B - 5
    X = 8

if D == 1500:
    Z = B - 4
    X = 9.5

if D == 1800:
    Z = B - 3
    X = 9.5

if D == 2300:
    Z = B - 3
    X = 10

if D == 3000:
    Z = B - 2
    X = 11


print("")
print("Results....")
print("")
print("Boards:")
print("The size of the board will be: (Height)", A + 6, "mm", "X", "(Width)", Z, "mm")
print("The size of the spine board will be: (Height)", A + 6, "mm", "X", "(Width)", C + 0.5, "mm")
print("")
print("Cloth/Caselining:")
print("The size of the cloth/caselining will be: (Height)", A + 38, "mm", "X", "(Width)", B + B + X + X + C + 26, "mm")
print("")
print("")
print("Have a nice day!!")
print("")
print("")
print("#This is for square back books only!#")
print("#Worked on the average turn-in of 16mm#")
print("#All still in testing phase!#")
print("")
print("Version 1.1 to come soon!!")
print("")
print("***For any problems or comments/ideas send a email to jovancarlleroux@msn.com***")
Wait = input("Press any key to exit.")
