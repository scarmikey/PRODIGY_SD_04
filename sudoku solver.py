import tkinter as tk
import numpy as np

class SudokuSolver:
    def __init__(self, board):
        self.board = board
        self.gui = tk.Tk()
        self.gui.title("Sudoku Solver")
        self.table = [[tk.Entry(self.gui, width=2) for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                self.table[i][j].grid(row=i, column=j)
                if board[i][j] != 0:
                    self.table[i][j].insert(tk.END, str(board[i][j]))

        solve_button = tk.Button(self.gui, text="Solve", command=self.solve)
        solve_button.grid(row=9, column=0, columnspan=9)

    def is_valid(self, pos, num):
        for i in range(9):
            if self.board[i][pos[1]] == num and pos[0] != i:
                return False
            if self.board[pos[0]][i] == num and pos[1] != i:
                return False
        box_x = pos[1] // 3
        box_y = pos[0] // 3
        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x*3, box_x*3 + 3):
                if self.board[i][j] == num and (i,j) != pos:
                    return False
        return True

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def solve(self):
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find

        for i in range(1,10):
            if self.is_valid((row, col), i):
                self.board[row][col] = i
                self.table[row][col].delete(0, tk.END)
                self.table[row][col].insert(tk.END, str(i))
                self.gui.update_idletasks()

                if self.solve():
                    return True

                self.board[row][col] = 0
                self.table[row][col].delete(0, tk.END)
                self.gui.update_idletasks()

        return False

    def start(self):
        self.gui.mainloop()

if __name__ == "__main__":
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    solver = SudokuSolver(board)
    solver.start()
