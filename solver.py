from cube import cubeState, Move, Edge, Corner

def checkWhiteCrossSolved(self):
    if self.edgePosition[Edge.UR] == Edge.UR and self.edgeOrientation[0] == 0 and self.edgePosition[Edge.UF] == Edge.UF and self.edgeOrientation[1] == 0 and self.edgePosition[Edge.UL] == Edge.UL and self.edgeOrientation[2] == 0 and self.edgePosition[Edge.UB] == Edge.UB and self.edgeOrientation[3] == 0:
        return True
    else:
        return False

def solveWhiteCross(self, moves):
    pass
#1. is UX already solved? if yes, next edge. if no, next step
#2. perform set algo to solve (not sure how to do this)?
#3. 

    #Case for when edge 


def solveEdge(self, edge):

    # target D-layer position and insertion move for each white edge
    EDGE_SOLVE_DATA = {
        Edge.UF: (Edge.DF, Move.F2),
        Edge.UR: (Edge.DR, Move.R2),
        Edge.UB: (Edge.DB, Move.B2),
        Edge.UL: (Edge.DL, Move.L2)
    }

    targetPosition, insertMove = EDGE_SOLVE_DATA[edge]

    # Keep rotating D until the target edge is underneath
    # the position where it belongs
    while True:

        position, orientation = self.getEdgeData(edge)

        if position == targetPosition and orientation == 0:
            break

        self = self.applyMove(Move.D)

    # Insert the edge into the U-layer cross
    self = self.applyMove(insertMove)

    return self

def stageEdge(self, edge):

    WHITE_EDGES = (
        Edge.UF,
        Edge.UR,
        Edge.UB,
        Edge.UL
    )

    D_POSITIONS = (
        Edge.DF,
        Edge.DR,
        Edge.DB,
        Edge.DL
    )

    MIDDLE_STAGE_DATA = {
        # position, orientation : (required D slot, move)

        (Edge.FR, 0): (Edge.DR, Move.R_PRIME),
        (Edge.FL, 0): (Edge.DL, Move.L),
        (Edge.BR, 0): (Edge.DR, Move.R),
        (Edge.BL, 0): (Edge.DL, Move.L_PRIME),

        (Edge.FR, 1): (Edge.DF, Move.F),
        (Edge.FL, 1): (Edge.DF, Move.F_PRIME),
        (Edge.BR, 1): (Edge.DB, Move.B_PRIME),
        (Edge.BL, 1): (Edge.DB, Move.B)
    }

    while True:

        position, orientation = self.getEdgeData(edge)

        #already staged
        if position in D_POSITIONS and orientation == 0:
            return self

        #middle layer

        if position in (Edge.FR, Edge.FL, Edge.BR, Edge.BL):

            requiredDPosition, move = MIDDLE_STAGE_DATA[
                (position, orientation)
            ]

            #protect white edges that are already staged.
            while (
                self.edgePosition[requiredDPosition] in WHITE_EDGES
                and
                self.edgeOrientation[requiredDPosition] == 0
            ):
                self = self.applyMove(Move.D)

            self = self.applyMove(move)
            continue

        #d layer but flipped

        if position in D_POSITIONS and orientation == 1:

            #rotate target until it reaches DF.
            while position != Edge.DF:
                self = self.applyMove(Move.D)
                position, orientation = self.getEdgeData(edge)

            self = self.applyMove(Move.F)
            # Re-check as a middle-layer case
            continue

        # U layer

        if position in (Edge.UF, Edge.UR, Edge.UB, Edge.UL):

            #Rotate target to UF first.
            while position != Edge.UF:
                self = self.applyMove(Move.U)
                position, orientation = self.getEdgeData(edge)

            # Make sure DF does not contain an already staged edge.
            while (
                self.edgePosition[Edge.DF] in WHITE_EDGES
                and
                self.edgeOrientation[Edge.DF] == 0
            ):
                self = self.applyMove(Move.D)

            if orientation == 0:
                # UF,0 -> DF,0
                self = self.applyMove(Move.F2)

            else:
                # UF,1 -> FR,0
                self = self.applyMove(Move.F)

            # Re-check resulting state
            continue