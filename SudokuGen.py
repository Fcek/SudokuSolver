import numpy as np
import math

class SudokuGenerator:
    size = 0
    difficulty = 0
    def __init__(self, size, difficulty): #TODO: add difficulty after generation
        self.size = size
        self.difficulty = difficulty
        self.sudokuArray = self.fillSudoku(np.zeros((self.size,self.size)))

    def fillSudoku(self, emptyArray):
        stepY = 0
        stepX = 0
        size = len(emptyArray)
        falseCount = 0
        falseCountGlobal = 0
        while stepY < size:
            stepX = 0
            falseCountGlobal = 0
            temp = np.arange(1,size+1)
            while stepX < size:
                if len(temp) != 1:
                    index = np.random.randint(1, len(temp))
                else:
                    index = 0
                if self.checkIfNumberOk(emptyArray, temp[index], stepX, stepY):
                    emptyArray[stepY, stepX] = temp[index]
                    temp = np.delete(temp, index)
                    stepX += 1
                    falseCount = 0
                    if stepX == size:
                        stepY += 1
                else:
                    falseCount += 1
                    if falseCount == len(temp): #reset one element and try to fit it
                        falseCountGlobal += 1
                        if stepX != 0:
                            stepX -= 1
                        falseCount = 0
                        temp = np.concatenate((temp[:0], [emptyArray[stepY,stepX]], temp[0:]))
                        emptyArray[stepY, stepX] = 0
                    if falseCountGlobal == math.pow(size,2): #reset whole row if cant find solution
                        falseCount = 0
                        falseCountGlobal = 0
                        emptyArray[stepY,:] = np.zeros(size)
                        break
        return emptyArray

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

s = SudokuGenerator(9,0)
print(s.sudokuArray)

