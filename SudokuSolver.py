from CheckNumber import checkIfNumberOk
from SudokuGen import SudokuGenerator
import numpy as np
class SudokuSolver(object):

    def solve(self, sudoku):
        emptyCells = self.findEmpytCells(sudoku)
        print(emptyCells)
        index = 0
        values = list()
        while index < len(emptyCells):
            valueId = 0
            if index == len(values):
                values.append(np.arange(1,len(sudoku)+1))
            while valueId < len(values[index]):
                posX = emptyCells[index][1]
                posY = emptyCells[index][0]
                value = values[index][valueId]
                if checkIfNumberOk(self, sudoku, value, posX, posY):
                    sudoku[posY, posX] = value
                    values[index] = np.delete(values[index],valueId)
                    index += 1
                    break
                else:
                    values[index] = np.delete(values[index],valueId)
                    #valueId += 1
                    while len(values[index]) == 0:
                        posX = emptyCells[index][1]
                        posY = emptyCells[index][0]
                        values[index] = np.arange(1,len(sudoku)+1)
                        sudoku[posY, posX] = 0
                        #print(sudoku[posY, posX])
                        if index != 0:
                            index -= 1
        return sudoku          

        
    def findEmpytCells(self, array):
        emptyCells = list()
        y = 0
        while y < len(array):
            x = 0
            while x < len(array):
                if array[y,x] == 0:
                    emptyCells.append((y,x))
                x +=1
            y += 1
        return emptyCells # posY, posX
