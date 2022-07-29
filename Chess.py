# Шахматная доска (цвета если одинаковые то...)
print("Hello, look at the chessboard, enter")
print("2 numbers vertically and 2 numbers horizontally, and I will tell you if the colors match or not")
numX1 = int(input("Enter the first number vertically"))
numY1 = int(input("Enter the first number horizontally"))
if (numY1 + numX1) % 2 == 0:
    print("black colour")
else:
    print("White color")
###
numX2 = int(input("Enter the second number vertically"))
numY2 = int(input("Enter the second number horizontally"))
if (numX2 + numY2) % 2 == 0:
    print("black colour")
else:
    print("White color")
notext = (input("Click on the key 'ENTER'"))
if notext == "":
    if (numX1 + numY1 + numX2 + numY2) % 2 == 0:
        print("Colors match")
    else:
        print("Colors don't match")
else:
    print("Why should I write something? Just click on 'ENTER'")
    print("Start the program again")
