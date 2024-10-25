import tkinter as tk
from random import choice


class Cell:
    def __init__(self):
        self.has_ship = False
        self.is_hit = False

    def fire(self):
        if not self.is_hit:
            self.is_hit = True
            return self.has_ship
        return None  # Indicates that the cell was already fired at


class Ship:
    def __init__(self, size):
        self.size = size
        self.hits = 0

    def hit(self):
        self.hits += 1
        return self.hits >= self.size


class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell() for _ in range(cols)] for _ in range(rows)]

    def place_ship(self, ship, start_row, start_col, horizontal=True):
        if horizontal:
            for col in range(start_col, start_col + ship.size):
                self.grid[start_row][col].has_ship = True
        else:
            for row in range(start_row, start_row + ship.size):
                self.grid[row][start_col].has_ship = True

    def fire_at(self, row, col):
        cell = self.grid[row][col]
        return cell.fire()


class BattleshipUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Battleship Game")
        self.board = Board(6, 6)  # 6x6 grid
        self.create_board()

        # Dummy ship placement (for testing)
        ship = Ship(3)  # Ship of size 3
        self.board.place_ship(ship, 1, 1, horizontal=True)  # Horizontal ship starting at (1,1)

    def create_board(self):
        board_frame = tk.Frame(self.root)
        board_frame.grid(row=0, column=0, padx=10, pady=10)

        self.buttons = {}  # Store buttons to update later
        for row in range(6):
            for col in range(6):
                btn = tk.Button(board_frame, text="", width=5, height=2,
                                command=lambda r=row, c=col: self.fire_at(r, c))
                btn.grid(row=row, column=col)
                self.buttons[(row, col)] = btn

        # Create a dummy button for testing
        self.test_button = tk.Button(self.root, text="Test Firing", command=self.test_fire)
        self.test_button.grid(row=1, column=0, pady=10)

    def fire_at(self, row, col):
        result = self.board.fire_at(row, col)
        if result is None:
            # Already fired at this cell
            self.display_message("Already fired at this cell!")
        elif result:
            # Hit
            self.buttons[(row, col)].config(text="O", bg="red")
            self.display_message(f"Hit at {row + 1}, {col + 1}!")
        else:
            # Miss
            self.buttons[(row, col)].config(text="X", bg="blue")
            self.display_message(f"Miss at {row + 1}, {col + 1}!")

    def test_fire(self):
        # Simulate firing at a random cell for testing
        row, col = choice(range(6)), choice(range(6))
        self.fire_at(row, col)

    def display_message(self, message):
        # Simple print message to display result
        print(message)


if __name__ == "__main__":
    root = tk.Tk()
    game = BattleshipUI(root)
    root.mainloop()
