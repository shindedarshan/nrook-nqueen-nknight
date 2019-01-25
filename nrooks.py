#!/usr/bin/env python

"""
Created on Tue Sep 4 21:15:58 2018
@author: Darshan
"""

#
# nrooks.py : Solve the N-Rooks problem!
# The N-rooks problem is: Given an empty NxN chessboard, place N rooks on the board so that no rooks
# can take any other, i.e. such that no two rooks share the same row or column.

import sys
from datetime import datetime

# Count # of pieces in given row
def count_on_row(board, row):
    return sum( board[row] ) 

# Count # of pieces in given column
def count_on_col(board, col):
    return sum( [ row[col] for row in board ] ) 

# Count total # of pieces on board
def count_pieces(board):
    return sum([ sum(row) for row in board ] )

# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    return "\n".join([ " ".join([ "R" if col else "_" for col in row ]) for row in board])

# Add a piece to the board at the given position, and return a new board (doesn't change original)
def add_piece(board, row, col):
    return board[0:row] + [board[row][0:col] + [1,] + board[row][col+1:]] + board[row+1:]

# Add a piece to the board at the given position, and return a new board (doesn't change original)
def add_piece1(board, row, col):
   # if (count_pieces(board) < N):
        new_board = board[0:row] + [board[row][0:col] + [1,] + board[row][col+1:]] + board[row+1:]
        if (new_board != board):
            return new_board 
    #else:
     #   return 
    
# Get list of successors of given board state
def successors(board):
    return [ add_piece(board, r, c) for r in range(0, N) for c in range(0,N) ]

# Get list of successors of given board state
def successors2(board):
    successors = []
    for c in range(0,N):
        for r in range(0, N):
            successor = add_piece1(board, r, c)
            if successor != None:
                successors.append(successor)
    return successors

# Get list of successors of given board state
def successors3(board):
    successors = []
    p = count_pieces(board)
    if p < N:
        for r in range(p, p+1):
            for c in range(p, p+1):
                if (count_on_col(board, c) > 0) :
                    continue
                successors.append(add_piece(board, r, c))
    return successors

# check if board is a goal state
def is_goal(board):
    return count_pieces(board) == N and \
        all( [ count_on_row(board, r) == 1 for r in range(0, N) ] ) and \
        all( [ count_on_col(board, c) == 1 for c in range(0, N) ] )

# Solve n-queens!
def solve(initial_board):
    fringe = [initial_board]
    while len(fringe) > 0:
        curr_node = fringe.pop()
        for s in successors3( curr_node ):    
            if is_goal(s):
                return(s)
            if (s not in fringe): 
                print (str(printable_board(s)) + "\n")
                fringe.append(s)
    return False

# This is N, the size of the board. It is passed through command line arguments.
#N = int(sys.argv[1])
N = input("Enter a number: ");

# The board is stored as a list-of-lists. Each inner list is a row of the board.
# A zero in a given square indicates no piece, and a 1 indicates a piece.
initial_board = [[0]*N]*N
print ("Starting from initial board:\n" + printable_board(initial_board) + "\n\nLooking for solution...\n")
start = datetime.now()
solution = solve(initial_board)
end = datetime.now() 
time = end - start
time = time.seconds*1000 + time.microseconds/1000
print (printable_board(solution) if solution else "Sorry, no solution found. :(")
print("time", time)


