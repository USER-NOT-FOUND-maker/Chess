Files = ["A","B","C","D","E","F","G","H"]
Ranks = [1,2,3,4,5,6,7,8]

class InvalidPieceInitialiser(ValueError):
    def __init__(self,message):
        self.Message = message
        super().__init__()



class Piece:
    def __init__(self,Colour,File,Rank):
        if File not in Files:
            raise InvalidPieceInitialiser("Entered file is not valid")
        if Rank not in Ranks:
            raise InvalidPieceInitialiser("Entered rank is not valid")
        
        self.File = File
        self.Rank = Rank
        self.Colour = Colour
        self.Position = (File,Rank)
    
    def FindSquareInd(self):
        for i in range(len(Board)):
            if Board[i].Piece == self:
                return i
        return


class Pawn(Piece):
    def __init__(self,Colour,File,Rank):
        super().__init__(Colour,File,Rank)
        self.Value = 1
    
    def PawnHasntMoved(self):
        return (self.Colour == "White" and self.Rank == 2) or (self.Colour == "Black" and self.Rank == 7)

    def __str__(self):
        return f"{self.Colour[0]}p"
    
    def Move(self,NewPos):

        if self.File != NewPos[0].upper():
            print("\nPawns must move straight forward unless capturing\n")
            DisplayBoard(Board)
            return
        
        if self.PawnHasntMoved():
            if self.Colour == "Black":
                AllowedRankChanges = (-1,-2)
            else:
                AllowedRankChanges = (1,2)
        else:
            if self.Colour == "Black":
                AllowedRankChanges = (-1)
            else:
                AllowedRankChanges = (1)

        if (int(NewPos[1]) - self.Rank) not in AllowedRankChanges:
            print("Pawn is not allowed to move up that many ranks.")
            return

        PieceSquareInd = self.FindSquareInd()

        def GetNewSquareInd(self,NewPos):
            RankChange = int(NewPos[1]) - self.Rank
            NewRank = self.Rank + RankChange

            for i in range(len(Board)):
                print(f"Pawn rank = {self.Rank} Pawn File = {self.File} current square rank = {Board[i].Rank} current square file = {Board[i].File} New Rank = {NewRank}")
                if Board[i].Rank == NewRank and Board[i].File == self.File:
                    return i


        NewSquareInd = GetNewSquareInd(self,NewPos)

        print(NewSquareInd)

        self.Rank = int(NewPos[1]) - self.Rank

        Board[PieceSquareInd].Piece = None
        Board[NewSquareInd].Piece = self
        
        

class Knight(Piece):
    def __init__(self,Colour,File,Rank):
        super().__init__(Colour,File,Rank)
        self.Value = 3
    
    def __str__(self):
        return f"{self.Colour[0]}N"



class Bishop(Piece):
    def __init__(self,Colour,File,Rank):
        super().__init__(Colour,File,Rank)
        self.Value = 3
    
    def __str__(self):
        return f"{self.Colour[0]}B"



class Rook(Piece):
    def __init__(self,Colour,File,Rank):
        super().__init__(Colour,File,Rank)
        self.Value = 5
    
    def __str__(self):
        return f"{self.Colour[0]}R"



class Queen(Piece):
    def __init__(self,Colour,File,Rank):
        super().__init__(Colour,File,Rank)
        self.Value = 9

    def __str__(self):
        return f"{self.Colour[0]}Q"



class King(Piece):
    def __init__(self,Colour,File,Rank):
        super().__init__(Colour,File,Rank)
        self.Value = 0
    
    def __str__(self):
        return f"{self.Colour[0]}K"



class Square:
    def __init__(self,Piece,File,Rank):
        self.Piece = Piece
        self.File = File
        self.Rank = Rank

    def __str__(self):
        if self.Piece == None:
            return f"[  ]"
        else:
            return f"[{self.Piece}]"

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
    for i in range(8):
        for j in range(1,9):
            Board.append(Square(None,Files[i],j))

    return Board

def FillBoard(Board):
    for i in range(8,16):
        Board[i] = Square(Pawn("White",Files[i-8],2),Files[i-8],2)
 
    for i in range(48,56):
        Board[i] = Square(Pawn("Black",Files[i-48],2),Files[i-48],2)

    for i in range(8):

        if i == 0 or i == 7:
            Board[i] = Square(Rook("White",Files[i],1),Files[i],1)
        elif i == 1 or i == 6:
            Board[i] = Square(Knight("White",Files[i],1),Files[i],1)
        elif i == 2 or i == 5:
            Board[i] = Square(Bishop("White",Files[i],1),Files[i],1)
        elif i == 3:
            Board[i] = Square(Queen("White",Files[i],1),Files[i],1)
        else:
            Board[i] = Square(King("White",Files[i],1),Files[i],1)

    for i in range(56,64):

            if i == 56 or i == 63:
                Board[i] = Square(Rook("Black",Files[i-56],1),Files[i-56],8)
            elif i == 57 or i == 62:
                Board[i] = Square(Knight("Black",Files[i-56],1),Files[i-56],8)
            elif i == 58 or i == 61:
                Board[i] = Square(Bishop("Black",Files[i-56],1),Files[i-56],8)
            elif i == 59:
                Board[i] = Square(Queen("Black",Files[i-56],1),Files[i-56],8)
            else:
                Board[i] = Square(King("Black",Files[i-56],1),Files[i-56],8)

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
"""
ExamplePawn = Board[8].Piece
ExamplePawn.Move("A3")

DisplayBoard(Board)
"""

for i in Board:
    print(f"file,rank = {i.File} {i.Rank}")
