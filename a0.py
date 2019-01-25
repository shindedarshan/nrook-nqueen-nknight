# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 21:15:58 2018

@author: Darshan
"""
#!/usr/bin/env python2

import sys
from datetime import datetime 

# Count # of pieces in given row
def count_on_row(board, row):
    return sum( board[row] ) 

# Count # of pieces in given column
def count_on_col(board, col):
    return sum( [ row[col] for row in board ] ) 

#def count_on_diag(board, row, col):
#    count = 0
#    for r in range(0,N):
#        for c in range(0, N):
#            if (r != row and c != col and ((row - r)*(row - r) == (col - c)*(col - c))):
#                if (board[r][c]):
#                    count+=1
#    return count

def count_on_diag(board, row, col):
    count = 0
    for i in range(1, N):
        #if(row != row - i and col != col - i):
        if((row - i) in range(0, N) and (col - i) in range(0, N) and board[row-i][col-i] == 1):
            count += 1
        if((row - i) in range(0, N) and (col + i) in range(0, N) and board[row-i][col+i] == 1):
            count += 1
    return count

def count_on_knight_pos(board, row, col):
    count = 0
    #if((row - 2) in range(0, N) and (col - 1) in range(0, N) and board[row-2][col-1] == 1):
    #    count += 1
    #if((row - 2) in range(0, N) and (col + 1) in range(0, N) and board[row-2][col+1] == 1):
    #    count += 1
    #if((row - 1) in range(0, N) and (col - 2) in range(0, N) and board[row-1][col-2] == 1):
    #    count += 1
    #if((row - 1) in range(0, N) and (col + 2) in range(0, N) and board[row-1][col+2] == 1):
    #    count += 1
    if((row + 2) in range(0, N) and (col - 1) in range(0, N) and board[row+2][col-1] == 1):
        count += 1
    if((row + 2) in range(0, N) and (col + 1) in range(0, N) and board[row+2][col+1] == 1):
        count += 1
    if((row + 1) in range(0, N) and (col - 2) in range(0, N) and board[row+1][col-2] == 1):
        count += 1
    if((row + 1) in range(0, N) and (col + 2) in range(0, N) and board[row+1][col+2] == 1):
        count += 1
    return count

# Count total # of pieces on board
def count_pieces(board):
    return sum([ sum(row) for row in board ] )

# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    board_string = ""
    char = ""
    for r in range(0, N):
        for c in range(0, N):
            if (r,c) in blocks:
                char = "x"
            elif T == "nqueen" and board[r][c] == 1: 
                char = "Q"
            elif T == "nrook" and board[r][c] == 1:
                char = "R"
            elif T == "nknight" and board[r][c] == 1:
                char = "K"
            else:
                char = "_"
            board_string = board_string + char + " "
        board_string = board_string + "\n"
    return board_string
    #return "\n".join([ " ".join([ "R" if col else "_" for col in row ]) for row in board])

# Add a piece to the board at the given position, and return a new board (doesn't change original)
def add_piece(board, row, col):
    return board[0:row] + [board[row][0:col] + [1,] + board[row][col+1:]] + board[row+1:]

# Get list of successors of given board state as requirements mentioned in question 4
def successors(board):
    successor = []
    if(count_pieces(board) < N):
        count =  count_pieces(board)
        #for r in range(count, count+1):
        for r in range(0, N):
            for c in range(0, N):
                if T == "nrook" and board[r][c] != 1 and count_on_col(board, c) == 0 and count_on_row(board, r) == 0 and (r,c) not in blocks:
                    successor.append(add_piece(board, r, c))
                elif T == "nqueen" and board[r][c] != 1 and count_on_col(board, c) == 0 and count_on_diag(board, r, c) == 0 and (r,c) not in blocks:
                    successor.append(add_piece(board, r, c))
                elif T == "nknight" and board[r][c] != 1 and count_on_knight_pos(board, r, c) == 0 and (r,c) not in blocks:
                    successor.append(add_piece(board, r, c))
                else: 
                    continue
    return successor

# check if board is a goal state
def is_goal(board):
    if T == "nknight":
        return count_pieces(board) == N
    else:    
        return count_pieces(board) == N and \
            all( [ count_on_row(board, r) <= 1 for r in range(0, N) ] ) and \
            all( [ count_on_col(board, c) <= 1 for c in range(0, N) ] )

# Solve n-rooks!
def solve(initial_board):
    fringe = [initial_board]
    while len(fringe) > 0:
        successor = successors(fringe.pop()) # fringe.pop() means this is implementing DFS
        #successor = successors(fringe.pop(0)) # fringe.pop(0) means this is implementing BFS
        if successor != None :
            for s in successor:
                #print (str(printable_board(s)) + "\n")
                if is_goal(s):
                    return(s)
                fringe.append(s)
    return False

# This are inputs required to execute this program whcih are passed through command line arguments.
inputs = sys.argv 
# N is size of board, T is type of execution, n is number of block positions of board
N = input("Enter a number: ")
#N = inputs[0]
T = raw_input("Enter type (nrook/nqueen/nknight): ")
#T = inputs[1]
n = input("Enter number of block cells: ")
#n = inputs[2]

if T not in ["nrook", "nqueen", "nknight"]:
    sys.exit("Entered type is invalid...")

initial_board = [[0]*N]*N

blocks = []
for i in range (0,n):
    x = input("Enter row number of block position " + str(i) + ": ")
    y = input("Enter column number of block position " + str(i) + ": ")
    # x = inputs[(2*i) + 3]
    # y = inputs[(2*i) + 4]
    if x in range(0, N) and y in range(0, N):
        blocks.append((x,y))
    else:
        sys.exit("Entered block position is invalid...")

# The board is stored as a list-of-lists. Each inner list is a row of the board.
# A zero in a given square indicates no piece, and a 1 indicates a piece.

print ("Starting from initial board:\n" + printable_board(initial_board) + "\n\nLooking for solution...\n")
start = datetime.now()
solution = solve(initial_board)
time = datetime.now() - start
time = time.seconds*1000 + time.microseconds/1000
print (printable_board(solution) if solution else "Sorry, no solution found. :(")
print ("Time taken: "+ str(time) + " milliseconds")