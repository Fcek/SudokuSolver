import numpy as np
import math
import CheckNumber

class SudokuGenerator(object):
    size = 0
    difficulty = 0

    def fillSudoku(self, emptyArray):
        stepY = 0
        stepX = 0
        size = len(emptyArray)
        falseCount = 0
        falseCountGlobal = 0
        while stepY < size:
            stepX = 0
            falseCountGlobal = 0
            falseRowCount = 0
            temp = np.arange(1,size+1)
            while stepX < size:
                if len(temp) != 1:
                    index = np.random.randint(0, len(temp))
                else:
                    index = 0
                if CheckNumber.checkIfNumberOk(self, emptyArray, temp[index], stepX, stepY):
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
                        falseRowCount += 1
                        if falseRowCount == size:
                            falseRowCount = 0
                            emptyArray[stepY,:] = np.zeros(size)
                            stepY -= 1
                        break
        return emptyArray

    def applyDifficulty(self, array, difficulty):
        y = 0
        while y < len(array):
            x = 0
            while x < len(array):
                if  difficulty > np.random.random_sample():
                    array[y,x] = 0
                x += 1
            y += 1
        return array

    def getSudokuArray(self, size, difficulty):
        self.size = size #only sizes avaible: 4, 9, 16, 25, 36, etc.
        self.difficulty = difficulty #0 -> easiest, 1 -> hardest
        return self.applyDifficulty(self.fillSudoku(np.zeros((self.size,self.size))), self.difficulty)