from initialise import *

def ValidateSquare(Square):
    if len(Square) != 2:
        return False
    
    CorrectFile = Square[0].upper() in Files

    try:
        num = Square[1]

        num = int(num)

        if num != int(Square[1]):
            RankIsNum = False
        else:    
            RankIsNum = True

    except ValueError:
        RankIsNum = False

    if RankIsNum:
        CorrectRank = int(Square[1]) in Ranks
    else:
        CorrectRank = False

    return CorrectRank and RankIsNum and CorrectFile

def GetSquare(prompt = "enter a chess square: ",FailedPrompt = "invalid square, try again: "):
    Square = input(prompt)

    while not ValidateSquare(Square):
        Square = input(FailedPrompt)

    return Square.upper()

def GetMove():
    MovingPieceSquare = GetSquare(prompt = "enter the square of the piece that is moving: ")

    while Board[NotationToIndex(MovingPieceSquare[0],MovingPieceSquare[1])].Piece == None:
        print(f"{MovingPieceSquare} does not have a piece on it, pick another square")
        MovingPieceSquare = GetSquare(prompt = "enter the square of the piece that is moving: ")
    
    ResultSquare = GetSquare(prompt = "enter the square that the piece is moving to: ")

    return MovingPieceSquare,ResultSquare

while True:
    print(GetMove)

"""

attributes we need in Notation class
- captured (boolean)
- new position (string of length 2)
- moving piece (string of length 1 unless its a pawn)
- length of the notation class itself (necause why not)
- check (boolean)
- castle (boolean)
- the moving piece
"""


"""
NotationSigns = ["a","b","c","d","e","f","g","h","1","2","3","4","5","6","7","8","R","B","N","K","Q","+","#","x","=","O-O-O","O-O"]

PieceNotations = 
{
    "K": "King",
    "Q": "Queen",
    "B": "Bishop",
    "N":"Knight",
    "R":"Rook"
}

class Notation:
    def __init__(self,Notation):
        if "x" in Notation or "X" in Notation:
            self.Capture = True
        else:
            self.Capture = False

        if "=" in Notation or "#" in Notation:
            self.Check = True
        else:
            self.Check = False

        
        if "O-O-O" in Notation  or Notation = "O-O" in Notation:
            self.Castle = True
        else:
            self.Castle = False

        if self.Castle and self.Capture:
            print("Can not castle and capture at the same time")
            del self
            return

        if "#" in Notation and "+" in Notation:
            print("if a move is checkmate, you must only include a # in the notation, but if its just check, you must only include a + in the notation, if it isnt a check or a checkmate, you dont include a + or a #")
            del self
            return

        self.Length = len(str(Notation))
"""
        

