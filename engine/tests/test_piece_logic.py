from engine.board_manager import BoardManager
from engine.piece_logic_engine import PieceLogicEngine

def test_knight_moves():
    board = BoardManager()
    logic = PieceLogicEngine(board)
    moves = logic.get_valid_moves("knight", 1, 4, 4)
    assert any(move for move in moves if move[0] != 1), "Knight should move across layers"  
    def _moves_for_rook(self, layer, row, col):
        """
        Rook moves linearly across rows, columns, and vertical layers.
        """
        moves = []
        for i in range(self.board.rows):
            if i != row and self.board.is_valid_position(layer, i, col):
                moves.append((layer, i, col))
        for j in range(self.board.cols):
            if j != col and self.board.is_valid_position(layer, row, j):
                moves.append((layer, row, j))
        for l in range(self.board.layers):
            if l != layer and self.board.is_valid_position(l, row, col):
                moves.append((l, row, col))
        return moves

    def _moves_for_bishop(self, layer, row, col):
        """
        Bishop moves diagonally across layers.
        """
        moves = []
        for delta in range(1, max(self.board.rows, self.board.cols)):
            for dl in [-1, 1]:
                for dr in [-1, 1]:
                    for dc in [-1, 1]:
                        nl = layer + dl * delta
                        nr = row + dr * delta
                        nc = col + dc * delta
                        if self.board.is_valid_position(nl, nr, nc):
                            moves.append((nl, nr, nc))
        return moves

    def _moves_for_queen(self, layer, row, col):
        """
        Queen combines rook and bishop logic across all layers.
        """
        return self._moves_for_rook(layer, row, col) + self._moves_for_bishop(layer, row, col)

    def _moves_for_king(self, layer, row, col):
        """
        King moves one square in any direction, including vertical.
        """
        moves = []
        for dl in [-1, 0, 1]:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dl == dr == dc == 0:
                        continue
                    nl, nr, nc = layer + dl, row + dr, col + dc
                    if self.board.is_valid_position(nl, nr, nc):
                        moves.append((nl, nr, nc))
        return moves

    def _moves_for_pawn(self, layer, row, col):
        """
        Pawn advances forward on its layer; can ascend/descend under specific conditions.
        This is a simplified version — you can expand with Floating En Passant and promotion logic.
        """
        moves = []
        forward = 1  # Assume white moves "up"; adjust for color later
        if self.board.is_valid_position(layer, row + forward, col):
            moves.append((layer, row + forward, col))
        # Optional vertical move
        for dl in [-1, 1]:
            if self.board.is_valid_position(layer + dl, row + forward, col):
                moves.append((layer + dl, row + forward, col))
        return moves
def test_rook_moves():
    board = BoardManager()
    logic = PieceLogicEngine(board)
    moves = logic.get_valid_moves("rook", 1, 4, 4)
    assert any(move[0] != 1 for move in moves), "Rook should move vertically"

def test_bishop_moves():
    board = BoardManager()
    logic = PieceLogicEngine(board)
    moves = logic.get_valid_moves("bishop", 1, 4, 4)
    assert any(move[0] != 1 for move in moves), "Bishop should move diagonally across layers"
