class Board:
    def __init__(self):
        '''
        self.state:
        - White's Move = 1
        - Black's Move = 2
        - White's Win = -1
        - Black's Win = -2
        - Draw = 0
        '''
        # 0 ~ White's Move, 1 ~ Black's Move
        self.state = 0 # White's Moves 
        self.evaluation = 0

        self.black = Player()
        self.white = Player()

        self.pieces = {} # piece id: Piece Object

        # 64 integer long bit board, 0 represents empty square
        # Default: black on top, white on bottom
        self.board = [
             1,  2,  3,  4,  5,  6,  7,  8,
             9, 10, 11, 12, 13, 14, 15, 16,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
             0,  0,  0,  0,  0,  0,  0,  0,
            17, 18, 19, 20, 21, 22, 23, 24,
            25, 26, 27, 28, 29, 30, 31, 32
        ]

        # Setup Board
        for i, n in enumerate(self.board):
            # r, c = i // 8, i % 8
            curr_piece = Piece(i, n)
            if 1 <= n <= 16:
                self.pieces[n] = curr_piece
                self.black.pieces[i] = curr_piece
            if 17 <= n <= 32:
                self.pieces[n] = curr_piece
                self.white.pieces[i] = curr_piece
    
    def get_white_pieces(self) -> None:
        for coordinate, piece in self.white.items():
            r, c = coordinate // 8, coordinate % 8
            print("{piece.type} @ ({r}, {c})")
        
    def get_black_pieces(self) -> None:
        for coordinate, piece in self.black.items():
            r, c = coordinate // 8, coordinate % 8
            print("{piece.type} @ ({r}, {c})")
    
    def print_board(self) -> None:
        for coordinate, id in enumerate(self.board):
            if id == 0:
                print('O', end =" ")
            else:
                curr_piece = self.pieces[id]
                print(curr_piece.appearance, end =" ")
            
            if (coordinate + 1) % 8 == 0:
                print()


PAWNS = {9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24}
ROOKS = {1, 8, 25, 32}
KNIGHTS = {2, 7, 26, 31}
BISHOPS = {3, 6, 27, 30}
QUEENS = {4, 28}
KINGS = {5, 29}

class Player:
    def __init__(self):
        self.pieces = {} # Bit Board Location: Piece Objects


class Piece:
    '''
    Pawn	1 point
    Knight	3 points
    Bishop	3 points
    Rook	5 points
    Queen	9 points
    '''
    def __init__(self, coordinate, id):
        self.coordinate = coordinate
        self.id = id
        self.value = -1
        self.type = None
        self.appearance = None
        # 0 ~ Black, 1 ~ White
        self.player = 0 if id > 16 else 1

        if id in PAWNS:
            self.value = 1
            self.type = 'pawn'
            self.appearance = '♟' if self.player == 0 else '♙'
        elif id in KNIGHTS:
            self.value = 3
            self.type = 'knight'
            self.appearance = '♞' if self.player == 0 else '♘'
        elif id in BISHOPS:
            self.value = 3
            self.type = 'bishop'
            self.appearance = '♝' if self.player == 0 else '♗'
        elif id in ROOKS:
            self.value = 5
            self.type = 'rook'
            self.appearance = '♜' if self.player == 0 else '♖'
        elif id in QUEENS:
            self.value = 9
            self.type = 'queen'
            self.appearance = '♛' if self.player == 0 else '♕'
        else: # King
            self.value = float('inf') 
            self.type = 'king'
            self.appearance = '♚' if self.player == 0 else '♔'



def main():
    board = Board()
    board.print_board()


if __name__=="__main__":
    main()