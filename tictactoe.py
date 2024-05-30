"""
Tic Tac Toe Player
"""

import math
import random
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = 0
    count_o = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                count_x += 1
            if board[i][j] == O:
                count_o += 1


    if count_x > count_o:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_set = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action_set.add((i , j))

    return action_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """ 
    turn = player(board)

    if action not in actions(board):
        raise Exception("Not valid")
    
    row, col = action
    newboard = copy.deepcopy(board)

    newboard[row][col] = player(board)
    
    return newboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] != EMPTY and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]

    for j in range(3):
        if board[0][j] != EMPTY and board[0][j] == board[1][j] == board[2][j]:
            return board[0][j]

    if board[0][0] != EMPTY and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    elif board[2][0] != EMPTY and board[2][0] == board[1][1] == board[0][2]:
        return board[2][0]
    else:
        return None
    
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    return False 

    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif board == initial_state():
        return (random.randint(0,2),random.randint(0,2))

    turn = player(board)
    if turn == X:
        best_score = float("-inf")
        best_action = None
        for action in actions(board):
            new_board = result(board, action)
            new_score = min_value(new_board)
            if new_score > best_score:
                best_score = new_score
                best_action = action
    elif turn == O:
        best_score = float("inf")
        best_action = None
        for action in actions(board):
            new_board = result(board, action)
            new_score = max_value(new_board)
            if new_score < best_score:
                best_score = new_score
                best_action = action

    return best_action

def max_value(board):
    if terminal(board):
        return utility(board)
    v = float("-inf")
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = float("inf")
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v