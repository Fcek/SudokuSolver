import math
def checkIfNumberOk(self, array, number, x, y): #function to check numbers in y and x axis and in the 'square'
        if number not in array[:,x] and number not in array[y,:]:
            squareSize = int(math.pow(len(array),0.5))
            squarePosX = int(math.floor(x/squareSize) * squareSize)
            squarePosY = int(math.floor(y/squareSize) * squareSize)
            for y in range(squarePosY, squarePosY + squareSize):
                for x in range(squarePosX, squarePosX + squareSize):
                    if number != array[y,x]:
                        continue
                    else:
                        return False
            return True
        else:
            return False