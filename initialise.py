from os import system

CODESUCCESS = 0
ERRCODEOBSTRUCTION = 1
ERRCODEINVALIDMOVEMENT = 2
ERRCODECHECK = 3
ERRCODESQUAREDOESNTEXIST = 4

Files = ["A","B","C","D","E","F","G","H"]
Ranks = [1,2,3,4,5,6,7,8]
WhiteTurn = True
MovesTaken = 0

# idk who needs to hear this but when "WhiteTurn" is not true, that means that its not whites turn, which means its blacks turn, try to keep up

def NotationToIndex(File,Rank):
    Rank = int(Rank)

    RankIndex = {
                1: [i for i in range(0, 8)],
                2: [i for i in range(8, 16)],
                3: [i for i in range(16, 24)],
                4: [i for i in range(24, 32)],
                5: [i for i in range(32, 40)],
                6: [i for i in range(40, 48)],
                7: [i for i in range(48, 56)],
                8: [i for i in range(56, 64)]
                }

    FileIndex = {
            "A": [i for i in range(0, 56+1, 8)],
            "B": [i for i in range(1, 57+1, 8)],
            "C": [i for i in range(2, 58+1, 8)],
            "D": [i for i in range(3, 59+1, 8)],
            "E": [i for i in range(4, 60+1, 8)],
            "F": [i for i in range(5, 61+1, 8)],
            "G": [i for i in range(6, 62+1, 8)],
            "H": [i for i in range(7, 63+1, 8)]
            }

    PossibleIndexes = RankIndex[Rank]

    for i in PossibleIndexes:
        if i in FileIndex[File]:
            return i

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

    def GetAllowedRankChanges(self):
        if self.Colour == "Black" and self.PawnHasntMoved():
            return [-1,-2]
        elif self.Colour == "Black" and (not self.PawnHasntMoved()):
            return [-1]

        elif self.Colour == "White" and (not self.PawnHasntMoved()):
            return [1]
        else:
            return [1,2]

    def __str__(self):
        return f"{self.Colour[0]}p"
    
    def Move(self,NewPos,Board):
        global AllMoves        

        if NewPos[0] not in Files or int(NewPos[1]) not in Ranks:
            return ERRCODESQUAREDOESNTEXIST

        AllowedRankChanges = self.GetAllowedRankChanges()       

        FileChange = Files.index(NewPos[0]) - Files.index(self.File)
        RankChange = int(NewPos[1]) - self.Rank
        
        if (RankChange not in AllowedRankChanges) or (FileChange not in (1,0,-1)):
                return ERRCODEINVALIDMOVEMENT

        
        if (FileChange != 0) and Board[NotationToIndex(NewPos[0],int(NewPos[1]))].Piece == None:
                """
                if self.Colour == "White" and (Board[NotationToIndex(NewPos[0],int(NewPos[1])-1)].Piece != None) and self.Rank == 5:
                        FirstMoveCheck = AllMoves[len(AllMoves)-2][NotationToIndex(NewPos[0],int(NewPos[1])-1)].Piece == None

                        if not FirstMoveCheck:
                                return ERRCODEINVALIDMOVEMENT

                        Board[NotationToIndex(NewPos[0],int(NewPos[1])-1)].Piece = None
                elif self.Colour == "Black" and (Board[NotationToIndex(NewPos[0],int(NewPos[1])+1)].Piece != None) and self.Rank == 4:
                        FirstMoveCheck = AllMoves[len(AllMoves)-2][NotationToIndex(NewPos[0],int(NewPos[1])+1)].Piece == None

                        if not FirstMoveCheck:
                                return ERRCODEINVALIDMOVEMENT

                        Board[NotationToIndex(NewPos[0],int(NewPos[1])+1)].Piece = None
                """
                return ERRCODEINVALIDMOVEMENT
        
 
        if RankChange > 1 or RankChange < -1:
                if RankChange > 0:
                        if Board[NotationToIndex(self.File,(self.Rank + (RankChange - 1)))].Piece:
                                return ERRCODEOBSTRUCTION
                else:
                        if Board[NotationToIndex(self.File,(self.Rank + (RankChange + 1)))].Piece: 
                                return ERRCODEOBSTRUCTION




        Board[NotationToIndex(self.File,self.Rank)].Piece = None

        self.Rank += RankChange
        self.File = Files[Files.index(self.File) + FileChange]
        
        Board[NotationToIndex(self.File,self.Rank)].Piece = self
        
        return CODESUCCESS

class Knight(Piece):
    def __init__(self,Colour,File,Rank):
        super().__init__(Colour,File,Rank)
        self.Value = 3
    
    def __str__(self):
        return f"{self.Colour[0]}N"

    def Move(self,NewPos,Board):
        if NewPos[0] not in Files or int(NewPos[1]) not in Ranks:
                return ERRCODESQUAREDOESNTEXIST
        
        RankChange = int(NewPos[1]) - self.Rank
        FileChange = Files.index(NewPos[0]) - Files.index(self.File)

        if (RankChange not in (1,2,-1,-2) or FileChange not in (1,2,-1,-2)) or (abs(RankChange) == abs(FileChange)):
                return ERRCODEINVALIDMOVEMENT

        
        Board[NotationToIndex(self.File,self.Rank)].Piece = None

        self.Rank += RankChange
        self.File = Files[Files.index(self.File) + FileChange]
        
        Board[NotationToIndex(self.File,self.Rank)].Piece = self

        return CODESUCCESS
class Bishop(Piece):
    def __init__(self,Colour,File,Rank):
        super().__init__(Colour,File,Rank)
        self.Value = 3
    
    def __str__(self):
        return f"{self.Colour[0]}B"

    def Move(self,NewPos,Board):
        pass

class Rook(Piece):
    def __init__(self,Colour,File,Rank):
        super().__init__(Colour,File,Rank)
        self.Value = 5
    
    def __str__(self):
        return f"{self.Colour[0]}R"

    def Move(self,NewPos,Board):
        pass


class Queen(Piece):
    def __init__(self,Colour,File,Rank):
        super().__init__(Colour,File,Rank)
        self.Value = 9

    def __str__(self):
        return f"{self.Colour[0]}Q"

    def Move(self,NewPos,Board):
        pass


class King(Piece):
    def __init__(self,Colour,File,Rank):
        super().__init__(Colour,File,Rank)
        self.Value = 0
    
    def __str__(self):
        return f"{self.Colour[0]}K"

    def Move(self,NewPos,Board):
        pass


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

def ConstructBoard():
    Board = []
    for i in range(1,9):
        Board.append(Square(None,"A",i))
    for i in range(1,9):
        Board.append(Square(None,"B",i))
    for i in range(1,9):
        Board.append(Square(None,"C",i))
    for i in range(1,9):
        Board.append(Square(None,"D",i))
    for i in range(1,9):
        Board.append(Square(None,"E",i))
    for i in range(1,9):
        Board.append(Square(None,"F",i))
    for i in range(1,9):
        Board.append(Square(None,"G",i))
    for i in range(1,9):
        Board.append(Square(None,"H",i))

    return Board

def FillBoard(Board):
    # White pieces
    Board[0].Piece = Rook("White", "A", 1)
    Board[1].Piece = Knight("White", "B", 1)
    Board[2].Piece = Bishop("White", "C", 1)
    Board[3].Piece = Queen("White", "D", 1)
    Board[4].Piece = King("White", "E", 1)
    Board[5].Piece = Bishop("White", "F", 1)
    Board[6].Piece = Knight("White", "G", 1)
    Board[7].Piece = Rook("White", "H", 1)

    Board[8].Piece = Pawn("White", "A", 2)
    Board[9].Piece = Pawn("White", "B", 2)
    Board[10].Piece = Pawn("White", "C", 2)
    Board[11].Piece = Pawn("White", "D", 2)
    Board[12].Piece = Pawn("White", "E", 2)
    Board[13].Piece = Pawn("White", "F", 2)
    Board[14].Piece = Pawn("White", "G", 2)
    Board[15].Piece = Pawn("White", "H", 2)

    # Black pieces
    Board[56].Piece = Rook("Black", "A", 8)
    Board[57].Piece = Knight("Black", "B", 8)
    Board[58].Piece = Bishop("Black", "C", 8)
    Board[59].Piece = Queen("Black", "D", 8)
    Board[60].Piece = King("Black", "E", 8)
    Board[61].Piece = Bishop("Black", "F", 8)
    Board[62].Piece = Knight("Black", "G", 8)
    Board[63].Piece = Rook("Black", "H", 8)

    Board[48].Piece = Pawn("Black", "A", 7)
    Board[49].Piece = Pawn("Black", "B", 7)
    Board[50].Piece = Pawn("Black", "C", 7)
    Board[51].Piece = Pawn("Black", "D", 7)
    Board[52].Piece = Pawn("Black", "E", 7)
    Board[53].Piece = Pawn("Black", "F", 7)
    Board[54].Piece = Pawn("Black", "G", 7)
    Board[55].Piece = Pawn("Black", "H", 7)

    return Board


Board = FillBoard(ConstructBoard())

def DisplayBoard(Board):
    for i in range(len(Board)):
        if i % 8 != 0 and i != 0:
            print(Board[i],end="")
        else:
            print()
            print(Board[i],end="")

    print()

DisplayBoard(Board)
