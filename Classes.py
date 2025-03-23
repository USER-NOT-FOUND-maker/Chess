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
    



class Pawn(Piece):
    def __init__(self,Colour,File,Rank):
        super().__init__(Colour,File,Rank)
        self.Value = 1
    
    def __str__(self):
        return f"{self.Colour[0]}p"
    
    def Move(self,NewPos):
        RankChange = NewPos[1] - self.Rank
        FileChange = not (self.File == NewPos[0])

        if FileChange:
            print("invalid move, unless capturing another piece, pawns cannot move diagonally")
            return

        if self.Colour == "White" and self.Rank == 2:
            if RankChange > 2:
                print("Invalid move, pawns on their first turn can move either 1 or 2 spaces forward, not any more")
                return
            elif RankChange < 1:
                print("Invalid move, pawns on their first move must go to a new position and cant go backwards (at all).")
                return
            else:
                self.Rank = NewPos[1]
                self.Position = (self.File,self.Rank)



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
    def __init__(self,Colour,Piece,File,Rank):
        self.Colour = Colour
        self.Piece = Piece
        self.File = File
        self.Rank = Rank

    def __str__(self):
        if self.Piece == None:
            return f"[  ]"
        else:
            return f"[{self.Piece}]"
