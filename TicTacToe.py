import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.game_board = [['' for _ in range(3)] for _ in range(3)]
        self.player_turn = 'X'

        for i in range(3):
            for j in range(3):
                button = tk.Button(self.window, text='', width=10, height=3,
                                   command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j)
                self.game_board[i][j] = button

        self.label = tk.Label(self.window, text="Player X's turn")
        self.label.grid(row=3, column=0, columnspan=3)

        self.window.mainloop()

    def on_button_click(self, i, j):
        if not self.game_board[i][j]['text']:
            self.game_board[i][j].config(text=self.player_turn)
            if self.check_winner(self.player_turn):
                self.label.config(text=f"Player {self.player_turn} wins!")
                self.disable_buttons()
            elif self.is_board_full():
                self.label.config(text="It's a draw!")
                self.disable_buttons()
            else:
                self.player_turn = 'O' if self.player_turn == 'X' else 'X'
                self.label.config(text=f"Player {self.player_turn}'s turn")

    def check_winner(self, player):
        for i in range(3):
            if all(self.game_board[i][j]['text'] == player for j in range(3)):
                return True
            if all(self.game_board[j][i]['text'] == player for j in range(3)):
                return True
        if all(self.game_board[i][i]['text'] == player for i in range(3)):
            return True
        if all(self.game_board[i][2 - i]['text'] == player for i in range(3)):
            return True
        return False

    def is_board_full(self):
        return all(self.game_board[i][j]['text'] for i in range(3) for j in range(3))

    def disable_buttons(self):
        for i in range(3):
            for j in range(3):
                self.game_board[i][j].config(state='disabled')

if __name__ == "__main__":
    TicTacToe()