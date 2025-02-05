"""
Tic Tac Toe Player
"""
import copy

X = "X"
O = "O"
EMPTY = None

class InvalidActionException(Exception):
    pass


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
    i = 0
    for row in board:
        for entry in row:
            if entry == X:
                i += 1
            elif entry == O:
                i -= 1

    if i == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available = set()
    for i in range(3):
        for j in range(3):
            if not board[i][j]:
                available.add((i, j))
    return available


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] is not EMPTY:
        raise InvalidActionException("Invalid Move")
    if any(x < 0 or x > 2 for x in action):
        raise InvalidActionException("Invalid Move")

    new = copy.deepcopy(board)  # Creates an independent copy
    new[action[0]][action[1]] = player(board)
    return new


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if all(x == X for x in row):
            return X
        if all(x == O for x in row):
            return O

    for i in range(3):
        if all(x == X for x in [board[0][i], board[1][i], board[2][i]]):
            return X
        if all(x == O for x in [board[0][i], board[1][i], board[2][i]]):
            return O

    if all(x == X for x in [board[0][0], board[1][1], board[2][2]]):
        return X
    if all(x == X for x in [board[0][2], board[1][1], board[2][0]]):
        return X
    if all(x == O for x in [board[0][0], board[1][1], board[2][2]]):
        return O
    if all(x == O for x in [board[0][2], board[1][1], board[2][0]]):
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    for row in board:
        if any(x == None for x in row):
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


def maxi(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    action = None
    act = list(actions(board))
    for i in range(len(act)):
        minim, _ = mini(result(board, act[i]))
        if minim > v:
            v = minim
            action = act[i]
    return v, action


def mini(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    action = None
    act = list(actions(board))
    for i in range(len(act)):
        maxim, _ = maxi(result(board, act[i]))
        if maxim < v:
            v = maxim
            action = act[i]
    return v, action


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    p = player(board)
    if p == X:
        _, action = maxi(board)
    else:
        _, action = mini(board)

    if action:
        return action
    return None
