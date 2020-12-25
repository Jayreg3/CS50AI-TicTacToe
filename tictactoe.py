"""
Tic Tac Toe Player
"""

import math
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
    is_x_turn = 0
    for row in board:
        for column in row:
            if column == 'X':
                is_x_turn += 1
            elif column == 'O':
                is_x_turn -= 1
            else:
                continue
    return 'X' if is_x_turn == 0 else 'O'


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i, row in enumerate(board):
        for j, column in enumerate(row):
            if column == None:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    current_player = player(board)
    resulting_board = copy.deepcopy(board)
    if resulting_board[action[0]][action[1]] is not None:
        try:
            raise Exception
        except Exception as err:
            if not err.args:
                err.args=('',)
            err.args += ("Action not valid. The spot already has a mark. Try another action",)
            raise
    resulting_board[action[0]][action[1]] = current_player
    return resulting_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    tally = {'Xtop_left_diagonal':0, 'Xtop_right_diagonal':0, 'Otop_left_diagonal':0, 'Otop_right_diagonal':0}
    top_left_diagonal = ((0,0), (1,1), (2,2))
    top_right_diagonal = ((2,0), (1,1), (0,2))

    for i,row in enumerate(board):
        for j,column in enumerate(row):
            if column == None:
                continue
            else:
                player = column
                col_key = str(player) + 'column' + str(j)
                row_key = str(player) + 'row' + str(i)
                top_left_key = str(player) + 'top_left_diagonal'
                top_right_key = str(player) + 'top_right_diagonal'
                tally[col_key] = 1 if col_key not in tally else (tally[col_key] + 1)
                tally[row_key] = 1 if row_key not in tally else (tally[row_key] + 1)
                if (i,j) in top_left_diagonal:
                    tally[top_left_key] += 1
                if (i,j) in top_right_diagonal:
                    tally[top_right_key] += 1
                if 3 in [tally[col_key], tally[row_key], tally[top_left_key], tally[top_right_key]]:
                    return player
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is None and len(actions(board)) > 0:
        return False
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise. Only called on terminal boards.
    """
    if winner(board) == 'X':
        return 1
    elif winner(board) == 'O':
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) is True:
        return None
    best_action = {'action': False, 'value': False}

    if player(board) == 'X':
        for action in actions(board):
            action_value = max_value(result(board, action), 1)
            if action_value > best_action['value'] or best_action['value'] is None:
                best_action['action'] = action
                best_action['value'] = action_value
            print(best_action)
    else:
        for action in actions(board):
            action_value = min_value(result(board, action), 1)
            if action_value < best_action['value'] or best_action['value'] is None:
                best_action['action'] = action
                best_action['value'] = action_value
            print(best_action)
    return best_action['action']


def max_value(board, num_of_turns):
    if terminal(board):
        return utility(board) / num_of_turns
    value = float('-inf')
    for action in actions(board):
        value = max(value, min_value(result(board, action), num_of_turns + 1))
        print('running max_value with board = ', board, ' value is ', value)
    return value


def min_value(board, num_of_turns):
    if terminal(board):
        return utility(board) / num_of_turns
    value = float('inf')
    for action in actions(board):
        value = min(value, max_value(result(board, action), num_of_turns + 1))
        print('running max_value with board = ', board, ' value is ', value)
    return value

