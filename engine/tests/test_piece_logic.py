from engine.board_manager import BoardManager
from engine.piece_logic_engine import PieceLogicEngine

def test_knight_moves():
    board = BoardManager()
    logic = PieceLogicEngine(board)
    moves = logic.get_valid_moves("knight", 1, 4, 4)
    assert any(move for move in moves if move[0] != 1), "Knight should move across layers"
