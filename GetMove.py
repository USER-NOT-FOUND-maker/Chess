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

def GetSquare(prompt = "\nenter a chess square: ",FailedPrompt = "\ninvalid square, try again: "):
    Square = input(prompt)

    while not ValidateSquare(Square):
        Square = input(FailedPrompt)

    return Square.upper()

def IsValidMovingPieceSquare(MovingPieceSquare,CorrectColour):
    
    PieceOnSquare = Board[NotationToIndex(MovingPieceSquare[0],MovingPieceSquare[1])].Piece != None
    if not PieceOnSquare:
        return False
    # need an early return because if we dont and there is no piece on that square we get an error when checking if the piece is the correct colour
    PieceIsCorrectColour = Board[NotationToIndex(MovingPieceSquare[0],int(MovingPieceSquare[1]))].Piece.Colour == CorrectColour
    return PieceIsCorrectColour

def GetMove():
    global WhiteTurn

    if WhiteTurn:
        CorrectColour = "White"
    else:
        CorrectColour = "Black"

    MovingPieceSquare = GetSquare(prompt = "\nenter the square of the piece that is moving: ") 
   
    while not IsValidMovingPieceSquare(MovingPieceSquare,CorrectColour):
        MovingPieceSquare = GetSquare(prompt = "\ninvalid square for some reason, enter another moving piece square: ")

    ResultSquare = GetSquare(prompt = "enter the square that the piece is moving to: ")

    return MovingPieceSquare,ResultSquare

"""
for the function "ExecuteMove" we need to know this

CODESUCCESS = 0                                                                                                                                                                                                                                 ERRCODEOBSTRUCTION = 1                                                                                                                                                                                                                          ERRCODEINVALIDMOVEMENT = 2                                                                                                                                                                                                                      ERRCODECHECK = 3                                                                                                                                                                                                                                ERRCODESQUAREDOESNTEXIST = 4
"""

def ExecuteMove():
    global WhiteTurn
    global MovesTaken

    MovingPieceSquare,ResultSquare = GetMove()
    TempBoard = Board

    MovingPiece = Board[NotationToIndex(MovingPieceSquare[0],int(MovingPieceSquare[1]))].Piece

    ResultingCode = MovingPiece.Move(ResultSquare,Board)
    
    
    if ResultingCode == CODESUCCESS:
    #    system("clear")
        DisplayBoard(Board)
        WhiteTurn = not WhiteTurn
        if WhiteTurn:
            CorrectColour = "White"
        else:
            CorrectColour = "Black"

        MovesTaken += 1


            
    elif ResultingCode == ERRCODEOBSTRUCTION:
   #     system("clear")
        print("\npiece could not move because there was another piece in its way\n")
        DisplayBoard(Board)
            
    elif ResultingCode == ERRCODEINVALIDMOVEMENT:
  #      system("clear")
        print("\npiece could not move because it did not follow the rules of how it moves\n")
        DisplayBoard(Board)
            
    elif ResultingCode == ERRCODECHECK:
 #       system("clear")
        print("\npiece could not move because it caused a check on its own king\n")
        DisplayBoard(Board)
    
    elif ResultingCode == ERRCODESQUAREDOESNTEXIST:
#        system("clear")
        print("\npiece could not move because the given square does not exist\n")
        DisplayBoard(Board)
    elif ResultingCode == ERRCODEFRIENDLYFIRE:
        print("\npiece could not move because it tried to take one of its own pieces\n")
        DisplayBoard(Board)            


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
        

