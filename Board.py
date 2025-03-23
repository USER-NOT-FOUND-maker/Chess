from Classes import *

def ConstructPieces(Colour):
    if Colour == "White":
        RankOne = 1
        RankTwo = 2
    else:
        RankOne = 7
        RankTwo = 8

    Pawns = [Pawn(Colour,Files[i],RankTwo) for i in range(8)]

    Rooks = [Rook(Colour,Files[0],RankOne),Rook(Colour,Files[7],RankOne)]

    Bishops = [Bishop(Colour,Files[2],RankOne),Bishop(Colour,Files[6],RankOne)]

    Knights= [Knight(Colour,Files[3],RankOne),Knight(Colour,Files[5],RankOne)]

    Queens =[Queen(Colour,Files[4],RankOne)]

    king = King(Colour,Files[5],RankOne)

    Pieces = []

    for i in range(8):
        Pieces.append(Pawns[i])
    
    for i in range(2):
        Pieces.append(Rooks[i])
    
    for i in range(2):
        Pieces.append(Bishops[i])
    
    for i in range(2):
        Pieces.append(Knights[i])
    
    Pieces.append(Queens[0])
    Pieces.append(king)

    return Pieces


WhitePieces,BlackPieces = ConstructPieces("White"),ConstructPieces("Black")

Pieces = []

for i in range(16):
    Pieces.append(WhitePieces[i])

for i in range(16):
    Pieces.append(BlackPieces[i])

def ConstructBoard():
    Board = []
    Dark = False
    for i in range(8):
        for j in range(8):
            if Dark:
                Board.append(Square("Black",None,Files[i],j+1))
            else:
                Board.append(Square("White",None,Files[i],j+1))

            Dark = not Dark
        Dark = not Dark
    return Board

def FillBoard(Board):
    for i in range(8,16):
        Colour = Board[i].Colour
        Board[i] = Square(Colour,Pawn("White",Files[i-8],2),Files[i-8],2)
 
    for i in range(48,56):
        Colour = Board[i].Colour
        Board[i] = Square(Colour,Pawn("Black",Files[i-48],2),Files[i-48],2)

    for i in range(8):
        Colour = Board[i].Colour

        if i == 0 or i == 7:
            Board[i] = Square(Colour,Rook("White",Files[i],1),Files[i],1)
        elif i == 1 or i == 6:
            Board[i] = Square(Colour,Knight("White",Files[i],1),Files[i],1)
        elif i == 2 or i == 5:
            Board[i] = Square(Colour,Bishop("White",Files[i],1),Files[i],1)
        elif i == 3:
            Board[i] = Square(Colour,Queen("White",Files[i],1),Files[i],1)
        else:
            Board[i] = Square(Colour,King("White",Files[i],1),Files[i],1)

    for i in range(56,64):
            Colour = Board[i].Colour

            if i == 56 or i == 63:
                Board[i] = Square(Colour,Rook("Black",Files[i-56],1),Files[i-56],8)
            elif i == 57 or i == 62:
                Board[i] = Square(Colour,Knight("Black",Files[i-56],1),Files[i-56],8)
            elif i == 58 or i == 61:
                Board[i] = Square(Colour,Bishop("Black",Files[i-56],1),Files[i-56],8)
            elif i == 59:
                Board[i] = Square(Colour,Queen("Black",Files[i-56],1),Files[i-56],8)
            else:
                Board[i] = Square(Colour,King("Black",Files[i-56],1),Files[i-56],8)

    return Board


Board = ConstructBoard()
Board = FillBoard(Board)

def DisplayBoard(Board):
    for i in range(len(Board)):
        if i % 8 != 0 and i != 0:
            print(Board[i],end="")
        else:
            print()
            print(Board[i],end="")

    print()

DisplayBoard(Board)
