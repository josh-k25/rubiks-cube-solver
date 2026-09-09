from cube import cubeState, Move, Edge, Corner

def checkWhiteCrossSolved(self):
    if self.edgePosition[0] == Edge.UR and self.edgeOrientation[0] == 0 and self.edgePosition[1] == Edge.UF and self.edgeOrientation[1] == 0 and self.edgePosition[2] == Edge.UL and self.edgeOrientation[2] == 0 and self.edgePosition[3] == Edge.UB and self.edgeOrientation[3] == 0:
        return True
    else:
        return False

def solveWhiteCross(selfj, moves):
    pass
#1. is UX already solved? if yes, next edge. if no, next step
#2. where is the UX position?
#3. what is the orientation?
#4. what situation is the cubie in?
#5. perform set algo to solve (not sure how to do this)?