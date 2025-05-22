"""
Tic Tac Toe Player
"""
import copy
import math

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
    # set counters for X and O occurences
    x_s = 0
    o_s = 0
    # Count occurences to determine which player is next
    for list in board:
        x_s += list.count("X")
        o_s += list.count("O")
    # if there are more Xs than Os, O is next elses it's always Xs turn
    if x_s > o_s:
        return O
    return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for indx_row, list in enumerate(board):
        for indx_col, item in enumerate(list):
            if item == None:
                moves.add((indx_row,indx_col))
    return moves



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_state = copy.deepcopy(board)
    current_player = player(new_state)
    if action not in actions(board):
        raise ValueError('invalid Action')
    for indx_row, list in enumerate(new_state):
        for indx_col, item in enumerate(list):
            if indx_row == action[0] and indx_col == action[1]:
                new_state[indx_row][indx_col] = current_player
    return new_state


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check if any rows have the same symbol in each cell that is not none
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]

    # check if any cols have the symbol thats not none
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]
    # checking diagonals maually since there are only two
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    # if no winner return none
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    counter = 0
    for list in board:
        for item in list:
            if item == None:
                counter += 1

    won = winner(board)
    if won is not None or counter == 0:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    won = winner(board)
    if won == "X":
        return 1
    if won == "O":
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # decide if a move needs to be made and how's turn it is
    if terminal(board):
        return None

    if player(board) == O:
        best_score = float('inf')
        best_move = None
        for move in actions(board):
            new_score = maxi(result(board,move))
            if new_score < best_score:
                best_score = new_score
                best_move = move
        return best_move

    best_score = float('-inf') # player X
    best_move = None
    for move in actions(board):
        new_score = mini(result(board,move))
        if new_score > best_score:
            best_score = new_score
            best_move = move
    return best_move


def mini(board): # player = O
    """
    Returns optimal move for O player
    """
    if terminal(board):
        return utility(board)
    best_move = float('inf')
    for move in actions(board):
        best_move = min(best_move,maxi(result(board,move)))
    return best_move


def maxi(board): # player = X
    """
    Returns optimal move for X player
    """
    if terminal(board):
        return utility(board)
    best_move = float('-inf')
    for move in actions(board):
        best_move = max(best_move,mini(result(board,move)))
    return best_move

