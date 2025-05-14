from os import system
from copy import deepcopy

Files = ["A","B","C","D","E","F","G","H"]
Ranks = [1,2,3,4,5,6,7,8]

def AddToFile(File,Add):
        return Files[Files.index(File) + Add]


def ShowAllPieces(Pieces):
        res = "\n"
        res += "["
        for i in Pieces:
                res += f"\n{repr(i)}\n"
        res += "]"
        return res

def FindKingInd(ColKing,Board):
        for i in Board:
                if type(i.Piece) == type(King("FOO","A",1)) and i.Piece.Colour == ColKing:
                        return Board.index(i)
        raise ValueError("somehow the king isnt there?")

def FindKingAllies(ColKing,Board):
        Allies = []
        for i in Board:
                if type(i.Piece) != type(None) and i.Piece.Colour == ColKing:
                        Allies.append(i.Piece)
        return Allies

def FindKingEnemies(ColKing,Board):
        Enemies = []
        for i in Board:
                if type(i.Piece) != type(None) and i.Piece.Colour != ColKing:
                        Enemies.append(i.Piece)
        return Enemies

def CopyBoards(BoardOne,BoardTwo):
        for i in BoardOne:
                BoardTwo.append(i)

def CheckIfCheckmate(ColourOfKing,Board):
        AllyPieces = FindKingAllies(ColourOfKing,Board)

        MovingIndex = 0

def ShowBoards(MainBoard,TempBoard):
        print("the Main Board looks like this")
        DisplayBoard(MainBoard)
        print("the temp board looks like this")
        DisplayBoard(TempBoard)


def IsInCheck(ColourOfKing,Board):
        EnemyPieces = FindKingEnemies(ColourOfKing,Board)
        KingIndex = FindKingInd(ColourOfKing,Board)

        
        KingIndex = IndexToNotation(KingIndex,Board)

        for i in EnemyPieces:
                if i.Move(KingIndex,Board,IsMove = False,CheckForCheck=False) == CODESUCCESS:
                        return True

        return False

# do we need these error codes? no. do we have these error codes? yes. do i want these error codes? yes. stop questioning everything i do, this is MY repositry, this is MY code and this is MY life i make MY OWN decisions and you get NO say in that

CODESUCCESS = 0
ERRCODEOBSTRUCTION = 1
ERRCODEINVALIDMOVEMENT = 2
ERRCODECHECK = 3
ERRCODESQUAREDOESNTEXIST = 4
ERRCODEFRIENDLYFIRE = 5
CHECKMATE = 6

WhiteTurn = True
MovesTaken = 0

 
# idk who needs to hear this but when "WhiteTurn" is not true, that means that its not whites turn, which means its blacks turn, try to keep up

def IndexToNotation(Index,Board):
        return f"{Board[Index].File}{Board[Index].Rank}"

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

# yes that function is insanely inefficent, time wasting, unnecasarily complex and memory inefficent, but do we really care about that?

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
        self.Position = (File,Rank) # we never use this attribute btw, i js thought its cool to have this here
    
    def FindSquareInd(self):
        for i in range(len(Board)):
            if Board[i].Piece == self:
                return i
        return
       
    def __repr__(self):
        return f"{self} at rank {self.Rank} at file {self.File} colour: {self.Colour}"


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
    
    def Move(self,NewPos,Board,CheckForCheck = True,IsMove = True):
# genuinely, i dont understand how the simplest piece in the game has the most complex implementation in code

        global AllMoves        
        

        if NewPos[0] not in Files or int(NewPos[1]) not in Ranks:
            return ERRCODESQUAREDOESNTEXIST

        if NewPos[0] == self.File and int(NewPos[1]) == int(self.Rank):
                return ERRCODEINVALIDMOVEMENT        

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
        
        if (FileChange != 0) and Board[NotationToIndex(NewPos[0],int(NewPos[1]))].Piece == None:
                return ERRCODEINVALIDMOVEMENT

 
        if RankChange > 1 or RankChange < -1:
                if RankChange > 0:
                        if Board[NotationToIndex(self.File,(self.Rank + (RankChange - 1)))].Piece:
                                return ERRCODEOBSTRUCTION
                else:
                        if Board[NotationToIndex(self.File,(self.Rank + (RankChange + 1)))].Piece: 
                                return ERRCODEOBSTRUCTION

        if Board[NotationToIndex(NewPos[0],int(NewPos[1]))].Piece != None:
                if Board[NotationToIndex(NewPos[0],int(NewPos[1]))].Piece.Colour == self.Colour:
                        return ERRCODEFRIENDLYFIRE

        if IsMove:
                Board[NotationToIndex(self.File,self.Rank)].Piece = None

                self.Rank += RankChange
                self.File = AddToFile(self.File,FileChange)

                Board[NotationToIndex(self.File,self.Rank)].Piece = self
                
        if CheckForCheck:
                if IsInCheck(self.Colour,Board):
                        if IsMove:
                                Board[NotationToIndex(self.File,self.Rank)].Piece = None
                                self.Rank -= RankChange
                                self.File = AddToFile(self.File,-FileChange)
                                Board[NotationToIndex(self.File,self.Rank)].Piece = self
                        return ERRCODECHECK    
        
        if IsMove: 
                if self.Colour == "White":
                       CheckMateCol = "Black"
                else:
                       CheckMateCol = "White"
               
                if CheckIfCheckmate(CheckMateCol,Board):
                       return CHECKMATE 
        
        return CODESUCCESS

class Knight(Piece):
    def __init__(self,Colour,File,Rank):
        super().__init__(Colour,File,Rank)
        self.Value = 3
    
    def __str__(self):
        return f"{self.Colour[0]}N"

    def Move(self,NewPos,Board,CheckForCheck = True,IsMove = True):
        if NewPos[0] not in Files or int(NewPos[1]) not in Ranks:
                return ERRCODESQUAREDOESNTEXIST
        
        RankChange = int(NewPos[1]) - self.Rank
        FileChange = Files.index(NewPos[0]) - Files.index(self.File)

        if (RankChange not in (1,2,-1,-2) or FileChange not in (1,2,-1,-2)) or (abs(RankChange) == abs(FileChange)):
                return ERRCODEINVALIDMOVEMENT
        
        if Board[NotationToIndex(NewPos[0],int(NewPos[1]))].Piece != None:
                if Board[NotationToIndex(NewPos[0],int(NewPos[1]))].Piece.Colour == self.Colour:
                        return ERRCODEFRIENDLYFIRE
        
#        print(IsCheck(self.Colour,Board))

        if IsMove:
                Board[NotationToIndex(self.File,self.Rank)].Piece = None

                self.Rank += RankChange
                self.File = Files[Files.index(self.File) + FileChange]
                 
                Board[NotationToIndex(self.File,self.Rank)].Piece = self
                

        if CheckForCheck:
                if IsInCheck(self.Colour,Board):
                        if IsMove:
                                Board[NotationToIndex(self.File,self.Rank)].Piece = None
                                self.Rank -= RankChange
                                self.File = Files[Files.index(self.File) - FileChange]
                                Board[NotationToIndex(self.File,self.Rank)].Piece = self
                        return ERRCODECHECK
        
        if IsMove:      
                if self.Colour == "White":
                       CheckMateCol = "Black"
                else:
                       CheckMateCol = "White"
         
                if CheckIfCheckmate(CheckMateCol,Board):
                       return CHECKMATE
 
        return CODESUCCESS

class Bishop(Piece):
    def __init__(self,Colour,File,Rank):
        super().__init__(Colour,File,Rank)
        self.Value = 3
    
    def __str__(self):
        return f"{self.Colour[0]}B"

    def Move(self,NewPos,Board,CheckForCheck = True,IsMove = True):
        if (NewPos[0] not in Files) or (int(NewPos[1]) not in Ranks):
                return ERRCODESQUAREDOESNTEXIST

        if NewPos[0] == self.File and int(NewPos[1]) == int(self.Rank):
                return ERRCODEINVALIDMOVEMENT        

        FileChange = Files.index(NewPos[0]) - Files.index(self.File)
        RankChange = int(NewPos[1]) - self.Rank

        if abs(FileChange) != abs(RankChange):
                return ERRCODEINVALIDMOVEMENT


        if RankChange > 0:
                AddToRank = 1
                TempRank = self.Rank + 1
        else:
                AddToRank = -1
                TempRank = self.Rank - 1

        if FileChange > 0:
                AddToFile = 1
                TempFile = Files[Files.index(self.File) + 1]
        else:
                AddToFile = -1
                TempFile = Files[Files.index(self.File) - 1]
        
       

        for i in range(abs(RankChange)-1): # incase you cant tell already, we can switch RankChange for FileChange and it makes no difference .
                if Board[NotationToIndex(TempFile,TempRank)].Piece != None:
                        return ERRCODEOBSTRUCTION
                TempRank += AddToRank
                TempFile = Files[Files.index(TempFile) + AddToFile]

        if Board[NotationToIndex(NewPos[0],int(NewPos[1]))].Piece != None:
                if Board[NotationToIndex(NewPos[0],int(NewPos[1]))].Piece.Colour == self.Colour:
                        return ERRCODEFRIENDLYFIRE


        TempBoard = [i for i in Board]
        
        if IsMove:
                Board[NotationToIndex(self.File,self.Rank)].Piece = None

                self.Rank += RankChange
                self.File = Files[Files.index(self.File) + FileChange]
                
                
                Board[NotationToIndex(self.File,self.Rank)].Piece = self


        if CheckForCheck:
                if IsInCheck(self.Colour,Board):
                        if IsMove:
                                Board[NotationToIndex(self.File,self.Rank)].Piece = None
                                self.Rank -= RankChange
                                self.File = Files[Files.index(self.File) - FileChange]
                                Board[NotationToIndex(self.File,self.Rank)].Piece = self
                        return ERRCODECHECK
        
        if IsMove:
                if self.Colour == "White":
                       CheckMateCol = "Black"
                else:
                       CheckMateCol = "White"
               
         
                if CheckIfCheckmate(CheckMateCol,Board):
                       return CHECKMATE
                 
        return CODESUCCESS
                         
class Rook(Piece):
    def __init__(self,Colour,File,Rank):
        super().__init__(Colour,File,Rank)
        self.Value = 5
    
    def __str__(self):
        return f"{self.Colour[0]}R"

    def Move(self,NewPos,Board,CheckForCheck = True,IsMove = True):
        if NewPos[0] not in Files or int(NewPos[1]) not in Ranks:
                return ERRCODESQUAREDOESNTEXIST
        
        FileChange = Files.index(NewPos[0]) - Files.index(self.File)
        RankChange = int(NewPos[1]) - self.Rank

        if FileChange != 0 and RankChange != 0:
                return ERRCODEINVALIDMOVEMENT

        if FileChange == 0:
                Vertical = True
        else:
                Vertical = False

        if Vertical:

                if RankChange > 0:
                        AddToRank = 1
                        TempRank = self.Rank + 1
                else:
                        AddToRank = -1 
                        TempRank = self.Rank - 1

                for i in range(abs(RankChange) - 1):
                        if Board[NotationToIndex(self.File,TempRank)].Piece != None:
                                return ERRCODEOBSTRUCTION
                        TempRank += AddToRank
        else:
                if FileChange > 0:
                        AddToFile = 1
                        TempFile = Files[Files.index(self.File) + 1]
                else:
                        AddToFile = -1
                        TempFile = Files[Files.index(self.File) - 1]

                for i in range(abs(FileChange) - 1):
                        if Board[NotationToIndex(TempFile,self.Rank)].Piece != None:
                                return ERRCODEOBSTRUCTION

                        TempFile = Files[Files.index(TempFile) + AddToFile]

 
        if Board[NotationToIndex(NewPos[0],int(NewPos[1]))].Piece != None:
                if Board[NotationToIndex(NewPos[0],int(NewPos[1]))].Piece.Colour == self.Colour:
                        return ERRCODEFRIENDLYFIRE


        TempBoard = [i for i in Board]

        if IsMove:
                Board[NotationToIndex(self.File,self.Rank)].Piece = None

                self.Rank += RankChange
                self.File = Files[Files.index(self.File) + FileChange]
                
                
                Board[NotationToIndex(self.File,self.Rank)].Piece = self
                        

        if CheckForCheck:
                if IsInCheck(self.Colour,TempBoard):
                        if IsMove: 
                                Board[NotationToIndex(self.File,self.Rank)].Piece = None
                                self.Rank -= RankChange
                                self.File = Files[Files.index(self.File) - FileChange]
                                Board[NotationToIndex(self.File,self.Rank)].Piece = self
                        return ERRCODECHECK

        if IsMove:
                if self.Colour == "White":
                       CheckMateCol = "Black"
                else:
                       CheckMateCol = "White"
         
                if CheckIfCheckmate(CheckMateCol,Board):
                       return CHECKMATE 

        return CODESUCCESS

class Queen(Piece):
    def __init__(self,Colour,File,Rank):
        super().__init__(Colour,File,Rank)
        self.Value = 9

    def __str__(self):
        return f"{self.Colour[0]}Q"

    def Move(self,NewPos,Board,CheckForCheck = True,IsMove = True):
        if NewPos[0] not in Files or int(NewPos[1]) not in Ranks:
                return ERRCODESQUAREDOESNTEXIST

        RankChange = int(NewPos[1]) - self.Rank
        FileChange = Files.index(NewPos[0]) - Files.index(self.File)
        
        if abs(RankChange) == abs(FileChange):
                MoveLike = "Bishop"
        elif (RankChange == 0 and FileChange != 0) or (RankChange != 0 and FileChange == 0):
                MoveLike = "Rook"
        else:
                return ERRCODEINVALIDMOVEMENT


        TempBoard = deepcopy(Board)


        if MoveLike == "Rook":
                TempBoard[NotationToIndex(self.File,self.Rank)].Piece = Rook(self.Colour,self.File,self.Rank)
        else:
                TempBoard[NotationToIndex(self.File,self.Rank)].Piece = Bishop(self.Colour,self.File,self.Rank)

        Res = TempBoard[NotationToIndex(self.File,self.Rank)].Piece.Move(NewPos,TempBoard,IsMove = False)
        
        if IsMove and Res in (CODESUCCESS,CHECKMATE):
                Board[NotationToIndex(self.File,self.Rank)].Piece = None
                self.Rank += RankChange
                self.File = Files[Files.index(self.File) + FileChange]
                Board[NotationToIndex(self.File,self.Rank)].Piece = self
                return Res
        else:
                return Res

class King(Piece):
    def __init__(self,Colour,File,Rank):
        super().__init__(Colour,File,Rank)
        self.Value = 0
    
    def __str__(self):
        return f"{self.Colour[0]}K"

    def Move(self,NewPos,Board,CheckForCheck = True,IsMove = True):
        
        print(f"made a call to {self}, moving to {NewPos}")

        if NewPos[0] not in Files or int(NewPos[1]) not in Ranks:
                return ERRCODESQUAREDOESNTEXIST

        RankChange = int(NewPos[1]) - self.Rank
        FileChange = Files.index(NewPos[0]) - Files.index(self.File)

        AcceptedChanges = (1,0,-1)

        if RankChange not in AcceptedChanges or FileChange not in AcceptedChanges:
                print(f"got an invalid movement trying to move {self} to {NewPos}, self.Rank = {self.Rank}, self.File = {self.File}, rankchange is {RankChange}, filechange is {FileChange}")
                return ERRCODEINVALIDMOVEMENT

       
        if Board[NotationToIndex(NewPos[0],int(NewPos[1]))].Piece != None:
                if Board[NotationToIndex(NewPos[0],int(NewPos[1]))].Piece.Colour == self.Colour:
                        return ERRCODEFRIENDLYFIRE
 

        TempBoard = [i for i in Board]

        if IsMove:
                Board[NotationToIndex(self.File,self.Rank)].Piece = None

                self.Rank += RankChange
                self.File = Files[Files.index(self.File) + FileChange]
                
                Board[NotationToIndex(self.File,self.Rank)].Piece = self
                        

        if CheckForCheck: 
                if IsInCheck(self.Colour,TempBoard):
                        if IsMove:
                                Board[NotationToIndex(self.File,self.Rank)].Piece = None
                                self.Rank -= RankChange
                                self.File = Files[Files.index(self.File) - FileChange]
                                Board[NotationToIndex(self.File,self.Rank)].Piece = self
                        return ERRCODECHECK

        if IsMove:
                if self.Colour == "White":
                       CheckMateCol = "Black"
                else:
                      CheckMateCol = "White"
         
                if CheckIfCheckmate(CheckMateCol,Board):
                       return CHECKMATE
 
        return CODESUCCESS 


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
    for i in range(8):
        Board.append(Square(None,Files[i],1))
    for i in range(8):
        Board.append(Square(None,Files[i],2))
    for i in range(8):
        Board.append(Square(None,Files[i],3))
    for i in range(8):
        Board.append(Square(None,Files[i],4))
    for i in range(8):
        Board.append(Square(None,Files[i],5))
    for i in range(8):
        Board.append(Square(None,Files[i],6))
    for i in range(8):
        Board.append(Square(None,Files[i],7))
    for i in range(8):
        Board.append(Square(None,Files[i],8))

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
    print("     ",end = "")
    for i in range(8):
        print(Files[i], end = " "*3)
    for i in range(len(Board)):
        if i % 8 != 0 and i != 0:
            print(f"{Board[i]}",end="")
        else:
            print()
            print(f"{(i // 8)+1} ",end = " ")
            print(f"{Board[i]}",end="")

    print()

# DisplayBoard(Board)
"""
for i in range(64):
        print(f"{i} = {IndexToNotation(i,Board)}")
"""

CheckmateBoard = ConstructBoard()

CheckmateBoard[8].Piece = King("White","A",2)
CheckmateBoard[1].Piece = Queen("Black","B",1)
CheckmateBoard[2].Piece = Rook("Black","C",1)
CheckmateBoard[63].Piece = King("Black","H",8)


print("this is what CheckmateBoard looks like")
DisplayBoard(CheckmateBoard)

print(f"calling 'CheckIfCheckmate' function (passing 'White' in for the colour) on CheckmateBoard returns {CheckIfCheckmate('White',CheckmateBoard)}")
