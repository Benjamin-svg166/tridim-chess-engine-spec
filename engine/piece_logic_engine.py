# engine/piece_logic_engine.py

class PieceLogicEngine:
    """
    Encodes movement rules for all pieces across layers.
    Includes vertical transitions, layer-specific constraints,
    and special moves like Layered Castling and Floating En Passant.
    """

    def __init__(self, board_manager):
        self.board = board_manager

    def get_valid_moves(self, piece, layer, row, col):
        """
        Returns a list of valid moves for a given piece at a position.
        Each move is a tuple: (target_layer, target_row, target_col)
        """
        if piece is None:
            return []

        method_name = f"_moves_for_{piece.lower()}"
        if hasattr(self, method_name):
            return getattr(self, method_name)(layer, row, col)
        else:
            return []

    def _moves_for_knight(self, layer, row, col):
        """
        Knight moves in L-shapes across layers.
        """
        deltas = [
            (2, 1, 0), (1, 2, 0), (-1, 2, 0), (-2, 1, 0),
            (-2, -1, 0), (-1, -2, 0), (1, -2, 0), (2, -1, 0),
            (1, 0, 2), (-1, 0, 2), (1, 0, -2), (-1, 0, -2),
            (0, 1, 2), (0, -1, 2), (0, 1, -2), (0, -1, -2),
            (2, 0, 1), (-2, 0, 1), (2, 0, -1), (-2, 0, -1),
            (0, 2, 1), (0, -2, 1), (0, 2, -1), (0, -2, -1)
        ]
        moves = []
        for dl, dr, dc in deltas:
            nl, nr, nc = layer + dl, row + dr, col + dc
            if self.board.is_valid_position(nl, nr, nc):
                moves.append((nl, nr, nc))
        return moves

    # Placeholder methods for other pieces
    def _moves_for_rook(self, layer, row, col):
        return []

    def _moves_for_bishop(self, layer, row, col):
        return []

    def _moves_for_queen(self, layer, row, col):
        return []

    def _moves_for_king(self, layer, row, col):
        return []

    def _moves_for_pawn(self, layer, row, col):
        return []
