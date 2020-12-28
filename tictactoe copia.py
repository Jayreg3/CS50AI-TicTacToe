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

    # Subtracts the number of Os from the number of Xs (X always starts first)
    x_minus_o = 0
    for row in board:
        for column in row:
            if column == 'X':
                x_minus_o += 1
            elif column == 'O':
                x_minus_o -= 1
            else:
                continue
    # Same number of X and O means X's turn
    return X if x_minus_o == 0 else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i, row in enumerate(board):
        for j, column in enumerate(row):
            if column == None:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Deep copy the current board to not manipulate the input board
    resulting_board = copy.deepcopy(board)
    # Raise an exception if the intended spot is already taken or out of the board
    if resulting_board[action[0]][action[1]] is not None or action[0] not in range(0,3) or action[1] not in range(0,3):
        # More complex way to raise exception
        # try:
        #     raise Exception
        # except Exception as err:
        #     if not err.args:
        #         err.args=('',)
        #     err.args += ("Action not valid. The spot already has a mark or is out of the board. Try another action",)
        #     raise

        # Simpler way to raise exception
        raise Exception("Action not valid. The spot already has a mark or is out of the board. Try another action")
    # If the move is legal, sets the current player's mark at the corresponding cell
    current_player = player(board)
    resulting_board[action[0]][action[1]] = current_player
    return resulting_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Creates a dict to tally each player's number in a row by row, column, or diagonal
    tally = {'Xtop_left_diagonal':0, 'Xtop_right_diagonal':0, 'Otop_left_diagonal':0, 'Otop_right_diagonal':0}
    # Define what is considered a diagonal
    top_left_diagonal = ((0,0), (1,1), (2,2))
    top_right_diagonal = ((2,0), (1,1), (0,2))

    # Loops through board, adding to the player's tally for each corresponding row, column, and diagonal
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
                # Report a winner as soon as any tally reaches 3
                if 3 in [tally[col_key], tally[row_key], tally[top_left_key], tally[top_right_key]]:
                    return player
    # Return None if no winner is found; game is in progress or tied
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Less optimal solution that calls the actions function which loops through the board twice
    # if winner(board) is None and len(actions(board)) > 0:
    #     return False
    # else:
    #     return True

    # More optimal solution that loops through the board once
    # Returns true (game over) if there is a winner or there are no empty spots
    if winner(board) is not None or not any(spot == EMPTY for spot in [col for row in board for col in row]):
        return True
    else:
        return False


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

    # Small optimization: if no move has been made, start in the middle
    if board == initial_state():
        return (1,1)

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

