class TicTacToe:

    # 核心想法：如果垂直、水平、兩個對角線的叉圈數量 = n 即這個玩家獲勝 => O(1)

    def __init__(self, n: int):
        # initialize size of the board
        self.n = n
        self.rows = [0] * n # 有 n 個 row 可以獲勝
        self.cols = [0] * n # 有 n 個 col 可以獲勝
        self.diag = 0
        self.anti_diag = 0
        
    def move(self, row: int, col: int, player: int) -> int:
        # use +1 & -1 to count player 1 & player 2's points
        value = 1 if player == 1 else -1

        # putting the move

        # 1. update row & col
        self.rows[row] += value
        self.cols[col] += value

        # 2. update diagonal
        if row == col:
            self.diag += value
        if row + col == self.n - 1:
            self.anti_diag += value

        # check the winner 
        if (abs(self.rows[row]) == self.n or 
            abs(self.cols[col]) == self.n or 
            abs(self.diag) == self.n or
            abs(self.anti_diag) == self.n
            ):
            return player

        return 0



# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
