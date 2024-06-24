class TicTacToe:
    def __init__(self):
        self._board = [[" ", " ", " "] for _ in range(3)]
        self._player = "X"

    def mark(self, r, c):
        if not (0 <= r <= 2 and 0 <= c <= 2):
            raise ValueError(f"Invalid board position: ({r}, {c})")
        if self._board[r][c] != " ":
            raise ValueError(f"Position ({r}, {c}) has already been marked.")

        if self.winner() is not None:
            raise ValueError("Game is already complete")

        self._board[r][c] = self._player
        self._switch_player()

    def _switch_player(self):
        self._player = "X" if self._player == "O" else "O"

    def _is_win(self, mark):
        board = self._board
        return (
            mark == board[0][0] == board[0][1] == board[0][2] or
            mark == board[1][0] == board[1][1] == board[1][2] or
            mark == board[2][0] == board[2][1] == board[2][2] or
            mark == board[0][0] == board[1][0] == board[2][0] or
            mark == board[0][1] == board[1][1] == board[2][1] or
            mark == board[0][2] == board[1][2] == board[2][2] or
            mark == board[0][0] == board[1][1] == board[2][2] or
            mark == board[0][2] == board[1][1] == board[2][0]
        )
    
    def winner(self):
        for mark in "XO":
            if self._is_win(mark):
                return mark
        return None

    def __str__(self):
        rows = [' | '.join(self._board[r]) for r in range(3)]
        return "\n-- --- ---\n".join(rows) + "\n"


game = TicTacToe()
game.mark(0, 0)
game.mark(1, 0)

game.mark(0, 1)
game.mark(1, 1)

# X wins
game.mark(0, 2)

print(game)
print("winner: ", game.winner())

