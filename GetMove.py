from initialise import *


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



