#1275 - Find Winner on a Tic Tac Toe Game

from typing import List

# Approach to the solution

# first find the size of the board (n = 3)
# count the sums of each row and column (rows, cols = [0] * n, [0] * n)
# track the main and secondary diagonals (d1, d2)
# the first player A should start at 1, then player B will start at -1
# loop over the moves, then iterate through all the moves that will have been played -> if a player marks(0, 1) row[0] and col[1] will be incremented
# check if the move is on the main diagonal, if yes add to d1 : add to d2
# return 1 if player  == 1 : return B then set the current player to B
# then check if all the boxes have been occupied, then return Draw : Pending


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        rows, cols = [0] * n, [0] * n
        d1, d2 = 0, 0
        player = 1 # this is player A, we will have player B starting from -1
        
        # loop over the moves
        for r, c in moves:
            # iterate through all moves played
            rows[r] += player
            cols[c] += player

            # if the move is on the main diagonal, add value to d1
            # if the move is on the secondary diagonal, add value to d2
            if r == c:
                d1 += player
            if r+c == n - 1:
                d2 += player
            if abs(rows[r]) == n or abs(cols[c]) == n or abs(d1) == n or abs(d2) == n:
                if player == 1:
                    return "A"
                else:
                    return "B"
                
            player *= -1 # switch player turn
            
        if len(moves) == n * n:
            return "Draw"
        else:
            return "Pending"