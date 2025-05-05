try:
        AllMoves = []

        from GetMove import *
        from initialise import * 


        while True:
            ExecuteMove()
                
            AllMoves.append(Board)
except KeyboardInterrupt:
        print("\n\nexiting game\n\n")
