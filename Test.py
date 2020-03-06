from CheckNumber import checkIfNumberOk
from SudokuGen import SudokuGenerator
from SudokuSolver import SudokuSolver
print('generating...')
s1 = SudokuGenerator()
sudoku1 = s1.getSudokuArray(9,0.3)
print(sudoku1)

print('start solving...')
s = SudokuSolver()
print(s.solve(sudoku1))