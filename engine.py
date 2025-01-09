'''
Board State:
    - Player to Move (White = 0 and Black = 1)
    - Data Structure: Player - Pieces; Piece - Value, Coordinate, Moves
        * coordinate to pieces
        * use bitboard when you can
    - Every move:
        * update all possible moves after move !!!
        * update every player eval after move (needs top)
    - General Things to Consider: Check/Checkmate, En Passant, Forced Draw

    Pieces of Engine Functionality:
    - Piece Values (i.e. Pawn ~ 1, Bishop ~ 3, Rook ~ 5)
    - Increase/Decrease Piece Value to promote natural moves (center pieces are better than edge pieces)
    - Have pieces mapped as Bit-Boards ~ [0/1] * 64
    - Minimax of Board (CPP / Rust)

    Brainstorm:
    - Give each piece a unique value: [1, 32] -> This lets us represent board as bitboard
    - Piece Index: Piece object
'''