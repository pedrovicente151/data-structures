class TicTacToe:

    def __init__(self):
        self._board = [[' '] * 3 for i in range(3)]
        self._player = 'X'

    def mark(self, i, j):
        if not (0 <= i <= 2 and 0 <= j <= 2):
            raise ValueError("Invalid board position.")
        if self._board[i][j] != ' ':
            raise ValueError('Board position occupied')
        if self.winner() is not None:
            raise ValueError('Game is already complete')
        self._board[i][j] = self._player
        if self._player == 'X':
            self._player = 'O'
        else:
            self._player = "X"

    def _is_win(self, mark):
        board = self._board
        return ()  #Marks

    def winner(self):
        for mark in 'XO':
            if self._is_win(mark):
                return mark
        return None

    def __str__(self):
        rows = ['|'.join(self._board[i]) for i in range(3)]
        return '\n-----\n'.join(rows)
