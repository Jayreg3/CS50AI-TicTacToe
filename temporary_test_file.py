from tictactoe import initial_state, player, actions, result, winner, terminal, utility, minimax
#import math

print('initial state = ', initial_state())
board = initial_state()
# board[0][0] = 'X'
# board[0][1] = 'O'
# board[1][0] = 'X'
# print('board = ', board)
# print('player = ', player(board))
# player = player(board)
# print('actions = ', actions(board))
# print('result = ', result(board, (2,0), player))
print('winner: ', winner(board))
print('terminal?: ', terminal(board))
# print('utility: ', utility(board))
# print('minimax: ', minimax(board))
#print(-math.inf < 0)
# print(float('-inf') < 0)