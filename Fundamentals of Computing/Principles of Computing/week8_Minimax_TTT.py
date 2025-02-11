"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    # initiate the case
    output = (-1, (-1, -1))
    
    # check current situations
    if board.check_win() is not None:
        return SCORES[board.check_win()], (-1, -1)
    
    # DFS
    else:
        for empty in board.get_empty_squares():
            copy_board = board.clone()
            copy_board.move(empty[0], empty[1], player)
            score, _ = mm_move(copy_board, provided.switch_player(player))
            if score * SCORES[player] == 1:
                return score, empty
            elif score * SCORES[player] > output[0]:
                output = [score, empty]
            elif output[0] == -1:
                output = [output[0], empty]
        return output[0] * SCORES[player], output[1]

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

#provided.play_game(move_wrapper, 1, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
