import tkinter as tk
from tkinter import messagebox

class SudokuSolverGUI:
    def __init__(self, master):
        self.master = master
        master.title("Sudoku Solver")

        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()

        solve_button = tk.Button(master, text="Solve", command=self.solve)
        solve_button.grid(row=10, column=0, columnspan=9, pady=10)

    def create_grid(self):
        for row in range(9):
            for col in range(9):
                e = tk.Entry(self.master, width=2, font=("Arial", 18), justify="center")
                e.grid(row=row, column=col, padx=2, pady=2)
                self.cells[row][col] = e

    def get_grid(self):
        grid = []
        for row in self.cells:
            current_row = []
            for cell in row:
                val = cell.get()
                current_row.append(int(val) if val.isdigit() else 0)
            grid.append(current_row)
        return grid

    def set_grid(self, grid):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)
                if grid[i][j] != 0:
                    self.cells[i][j].insert(0, str(grid[i][j]))

    def is_valid(self, grid, row, col, num):
        for x in range(9):
            if grid[row][x] == num or grid[x][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if grid[start_row + i][start_col + j] == num:
                    return False
        return True

    def solve_sudoku(self, grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(grid, row, col, num):
                            grid[row][col] = num
                            if self.solve_sudoku(grid):
                                return True
                            grid[row][col] = 0
                    return False
        return True

    def solve(self):
        grid = self.get_grid()
        if self.solve_sudoku(grid):
            self.set_grid(grid)
        else:
            messagebox.showerror("Error", "No solution exists for this Sudoku puzzle.")

# Run the GUI
root = tk.Tk()
app = SudokuSolverGUI(root)
root.mainloop()
