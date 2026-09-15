from cube import cubeState, Move, Edge, Corner

def checkWhiteCrossSolved(self):
    if self.edgePosition[Edge.UR] == Edge.UR and self.edgeOrientation[0] == 0 and self.edgePosition[Edge.UF] == Edge.UF and self.edgeOrientation[1] == 0 and self.edgePosition[Edge.UL] == Edge.UL and self.edgeOrientation[2] == 0 and self.edgePosition[Edge.UB] == Edge.UB and self.edgeOrientation[3] == 0:
        return True
    else:
        return False

def solveWhiteCross(self):
    
    #    is it already solved?
    #    yes → next corner
    #    no
    #    ↓
    #   stageCorner(corner)
    #    ↓
    #   target is somewhere on D
    #    ↓
    #   rotate D until target is
    #   underneath its destination
    #    ↓
    #   perform appropriate insertion
    #    ↓
    #   check isCornerSolved()
    #    ↓
    #   repeat if necessary

    WHITE_EDGES = (
        Edge.UF,
        Edge.UR,
        Edge.UB,
        Edge.UL
    )

    # If the whole cross is already solved, do nothing
    if checkWhiteCrossSolved(self):
        return self

    # First, stage every white edge onto the D layer
    # with orientation 0
    for edge in WHITE_EDGES:
        self = stageEdge(self, edge)

    # Then insert each staged edge into its solved U position
    for edge in WHITE_EDGES:
        self = solveFirstLayerEdge(self, edge)

    return self

def solveFirstLayerEdge(self, edge):

    # target D-layer position and insertion move for each white edge to solve
    FIRST_EDGE_SOLVE_DATA = {
        Edge.UF: (Edge.DF, Move.F2),
        Edge.UR: (Edge.DR, Move.R2),
        Edge.UB: (Edge.DB, Move.B2),
        Edge.UL: (Edge.DL, Move.L2)
    }

    targetPosition, solveMove = FIRST_EDGE_SOLVE_DATA[edge]

    # While true is an infinite loop; use break to leave the loop
    # Keep rotating D until the target edge is underneath
    # the position where it belongs
    while True:

        position, orientation = self.getEdgeData(edge)

        if position == targetPosition and orientation == 0:
            break

        # loop D until it hits the right target position
        self = self.applyMove(Move.D)

    # Insert the edge into the U-layer cross
    self = self.applyMove(solveMove)

    return self

#get edge to D layer so that it can be solved
def stageEdge(self, edge):

#dictionaries to reference the white edges and target (D) positions
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

    #reference table on what to do when the edge piece is in the middle of the rubix cube
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
            #if there already is a white edge piece there do D to move it and then apply the setup move
            while (
                self.edgePosition[requiredDPosition] in WHITE_EDGES and
                self.edgeOrientation[requiredDPosition] == 0
            ):
                self = self.applyMove(Move.D)

            self = self.applyMove(move)
            continue

        #D layer but orientation is wrong
        #either edge piece starts there or its from the middle layer
        if position in D_POSITIONS and orientation == 1:

            #rotate target until it reaches DF.
            while position != Edge.DF:
                self = self.applyMove(Move.D)
                position, orientation = self.getEdgeData(edge)

            self = self.applyMove(Move.F)
            #it is sent back to middle layer but with correct for solving orientation
            continue

        # U layer

        if position in (Edge.UF, Edge.UR, Edge.UB, Edge.UL):

            #Rotate target to UF first.
            while position != Edge.UF:
                self = self.applyMove(Move.U)
                position, orientation = self.getEdgeData(edge)

            #make sure DF does not contain an already staged edge.
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

def solveFirstLayerCorner(self, corner):

    WHITE_CORNERS = (
        Corner.URF,
        Corner.UFL,
        Corner.ULB,
        Corner.UBR
    )

    CORNER_TARGET_POSITION = {
        Corner.URF: Corner.DFR,
        Corner.UFL: Corner.DLF,
        Corner.ULB: Corner.DBL,
        Corner.UBR: Corner.DRB
    }

    CORNER_INSERTION_MOVES = {
    Corner.URF: (
        Move.R_PRIME,
        Move.D_PRIME,
        Move.R,
        Move.D
    ),

    Corner.UFL: (
        Move.L,
        Move.D,
        Move.L_PRIME,
        Move.D_PRIME
    ),

    Corner.ULB: (
        Move.L_PRIME,
        Move.D_PRIME,
        Move.L,
        Move.D
    ),

    Corner.UBR: (
        Move.R,
        Move.D,
        Move.R_PRIME,
        Move.D_PRIME
    )
}

    if self.isCornerSolved(corner):
        return self

    position, _ = self.getCornerData(corner)

    # rotate D until the target corner is underneath
    # the U-layer position where it belongs
    while position != CORNER_TARGET_POSITION[corner]:
        self = self.applyMove(Move.D)
        position, _ = self.getCornerData(corner)

    insertionMoves = CORNER_INSERTION_MOVES[corner]

    # repeat the sexy move😏 until both
    # position and orientation are correct
    while not self.isCornerSolved(corner):
        self = self.applyMoves(insertionMoves)

    return self

def stageCorner(self, corner):

    WHITE_CORNERS = (
        Corner.URF,
        Corner.UFL,
        Corner.ULB,
        Corner.UBR
    )

    D_CORNERS = (
        Corner.DFR,
        Corner.DLF,
        Corner.DBL,
        Corner.DRB
    )

    #Set moves for when a corner is in the wrong corner and needs to be ejected to the D layer
    CORNER_EJECTION_MOVES = {
            Corner.URF: (Move.R_PRIME, Move.D_PRIME, Move.R),
            Corner.UFL: (Move.L, Move.D, Move.L_PRIME),
            Corner.ULB: (Move.L_PRIME, Move.D_PRIME, Move.L),
            Corner.UBR: (Move.R, Move.D, Move.R_PRIME)
        }

    while True:

            position, _ = self.getCornerData(corner)

            #if corner is solved move on
            if self.isCornerSolved(corner):
                return self

            #if corner is staged move on
            if position in D_CORNERS:
                return self
    
            #position in U corner but no the right one
            if position in WHITE_CORNERS:
                ejectionmoves  = CORNER_EJECTION_MOVES[position]

                self = self.applyMoves(ejectionmoves)

            continue

def solveWhiteCorners(self):

    WHITE_CORNERS = (
        Corner.URF,
        Corner.UFL,
        Corner.ULB,
        Corner.UBR
    )

    for corner in WHITE_CORNERS:

        if self.isCornerSolved(corner):
            continue

        self = stageCorner(self, corner)
        self = solveFirstLayerCorner(self, corner)

    return self

def solveFirstLayer(self):

    newState = solveWhiteCross(self)

    newState = solveWhiteCorners(newState)

    return newState

def solveSecondLayer(self):

    #define middle edges (cubies that need to be solved for second layer)
    MIDDLE_EDGES = (
        Edge.FL,
        Edge.FR,
        Edge.BR,
        Edge.BL
    )

    #current middle-layer position : ejection sequence
    SECOND_EDGE_EJECTION_MOVES = {
        Edge.FL: (Move.D, Move.L, Move.D_PRIME, Move.L_PRIME, Move.D_PRIME, Move.F_PRIME, Move.D, Move.F),

        Edge.FR: (Move.D_PRIME, Move.R_PRIME, Move.D, Move.R, Move.D, Move.F, Move.D_PRIME, Move.F_PRIME),

        Edge.BL: (Move.D_PRIME, Move.L_PRIME, Move.D, Move.L, Move.D, Move.B, Move.D_PRIME, Move.B_PRIME),

        Edge.BR: (Move.D, Move.R, Move.D_PRIME, Move.R_PRIME, Move.D_PRIME, Move.B_PRIME, Move.D, Move.B)
    }

    #solve data depending on cubie orientation
    #get depending on cubie being solved and its orientation, use specific target cubie location and set moves
    SECOND_EDGE_SOLVE_DATA = {
    (Edge.FL, 1): (Edge.DF, (Move.D, Move.L, Move.D_PRIME, Move.L_PRIME, Move.D_PRIME, Move.F_PRIME, Move.D, Move.F)),
    (Edge.FL, 0): (Edge.DB, (Move.F_PRIME, Move.D_PRIME, Move.F, Move.D, Move.L, Move.D, Move.L_PRIME, Move.D_PRIME)),

    (Edge.FR, 1): (Edge.DF, (Move.D_PRIME, Move.R_PRIME, Move.D, Move.R, Move.D, Move.F, Move.D_PRIME, Move.F_PRIME)),
    (Edge.FR, 0): (Edge.DB, (Move.F, Move.D, Move.F_PRIME, Move.D_PRIME, Move.R_PRIME, Move.D_PRIME, Move.R, Move.D)),

    (Edge.BL, 1): (Edge.DB, (Move.D_PRIME, Move.L_PRIME, Move.D, Move.L, Move.D, Move.B, Move.D_PRIME, Move.B_PRIME)),
    (Edge.BL, 0): (Edge.DF, (Move.B, Move.D, Move.B_PRIME, Move.D_PRIME, Move.L_PRIME, Move.D_PRIME, Move.L, Move.D)),

    (Edge.BR, 1): (Edge.DB, (Move.D, Move.R, Move.D_PRIME, Move.R_PRIME, Move.D_PRIME, Move.B_PRIME, Move.D, Move.B)),
    (Edge.BR, 0): (Edge.DF, (Move.B_PRIME, Move.D_PRIME, Move.B, Move.D, Move.R, Move.D, Move.R_PRIME, Move.D_PRIME))
}
    for edge in MIDDLE_EDGES:

        #if its alreadt solved move on
        if self.isEdgeSolved(edge):
            continue

        position, orientation = self.getEdgeData(edge)

        #if cubie in edge position that is not correct eject it into the D layer
        if position in (Edge.FL, Edge.FR, Edge.BL, Edge.BR):
            ejectionMoves = SECOND_EDGE_EJECTION_MOVES[position]
            self = self.applyMoves(ejectionMoves)
            position, orientation = self.getEdgeData(edge)

        assert position in (Edge.DF, Edge.DR, Edge.DL, Edge.DB)

        position, orientation = self.getEdgeData(edge)
        targetPosition, moves = SECOND_EDGE_SOLVE_DATA[(edge, orientation)]

        # orientation should be fixed here
        while position != targetPosition:
            self = self.applyMove(Move.D)
            position, orientation = self.getEdgeData(edge)

        self = self.applyMoves(moves)

        position, orientation = self.getEdgeData(edge)

    return self

def solveThirdLayer(self):

    self = solveYellowCross(self)

    self = solveYellowCrossEdges(self)

    self = positionYellowCorners(self)

    self = orientYellowCorners(self)

    return self
    

def solveYellowCross(self):

    yellowDotMoves = (
        Move.F_PRIME,
        Move.R_PRIME,
        Move.D_PRIME,
        Move.R,
        Move.D,
        Move.F
        )

    YELLOW_LINE_MOVES = {

        # Line already in required orientation: DL + DR
        (Edge.DL, Edge.DR): (
            Move.F_PRIME,
            Move.R_PRIME,
            Move.D_PRIME,
            Move.R,
            Move.D,
            Move.F
        ),

        # Rotate DF + DB line into DL + DR first
        (Edge.DF, Edge.DB): (
            Move.D,
            Move.F_PRIME,
            Move.R_PRIME,
            Move.D_PRIME,
            Move.R,
            Move.D,
            Move.F
        )
    }

    YELLOW_L_MOVES = {

        # L already in required orientation: DR + DF
        (Edge.DR, Edge.DF): (
            Move.F_PRIME,
            Move.R_PRIME,
            Move.D_PRIME,
            Move.R,
            Move.D,
            Move.F
        ),

        # Rotate DB + DR into DR + DF
        (Edge.DB, Edge.DR): (
            Move.D_PRIME,
            Move.F_PRIME,
            Move.R_PRIME,
            Move.D_PRIME,
            Move.R,
            Move.D,
            Move.F
        ),

        # Rotate DL + DB into DR + DF
        (Edge.DL, Edge.DB): (
            Move.D2,
            Move.F_PRIME,
            Move.R_PRIME,
            Move.D_PRIME,
            Move.R,
            Move.D,
            Move.F
        ),

        # Rotate DF + DL into DR + DF
        (Edge.DF, Edge.DL): (
            Move.D,
            Move.F_PRIME,
            Move.R_PRIME,
            Move.D_PRIME,
            Move.R,
            Move.D,
            Move.F
        )
    }

    while not self.yellowCrossSolved():

        lineEdges = self.yellowLineEdges()

        #if yellow line was detected it will return edges and corresponding moves will executee
        if lineEdges is not None:
            moves = YELLOW_LINE_MOVES[lineEdges]
            self = self.applyMoves(moves)
            continue

        lEdges = self.yellowLEdges()

        #if yellow l was detected it will return edges and corresponding moves will executee
        if lEdges is not None:
            moves = YELLOW_L_MOVES[lEdges]
            self = self.applyMoves(moves)
            continue

        # no cross, line, or L -> dot
        self = self.applyMoves(yellowDotMoves)

    return self

def solveYellowCrossEdges(self):

    YELLOW_EDGES = (
        Edge.DF,
        Edge.DR,
        Edge.DB,
        Edge.DL
    )

    #the two listed edges are already solved. the algorithm preserves those two and swaps the other two.
    YELLOW_EDGE_PERMUTATION_MOVES = {

        # DF + DR solved
        (Edge.DF, Edge.DR): (
            Move.F_PRIME,
            Move.D_PRIME,
            Move.F,
            Move.D_PRIME,
            Move.F_PRIME,
            Move.D2,
            Move.F,
            Move.D_PRIME
        ),

        # DR + DB solved
        (Edge.DR, Edge.DB): (
            Move.R_PRIME,
            Move.D_PRIME,
            Move.R,
            Move.D_PRIME,
            Move.R_PRIME,
            Move.D2,
            Move.R,
            Move.D_PRIME
        ),

        # DB + DL solved
        (Edge.DB, Edge.DL): (
            Move.B_PRIME,
            Move.D_PRIME,
            Move.B,
            Move.D_PRIME,
            Move.B_PRIME,
            Move.D2,
            Move.B,
            Move.D_PRIME
        ),

        # DL + DF solved
        (Edge.DF, Edge.DL): (
            Move.L_PRIME,
            Move.D_PRIME,
            Move.L,
            Move.D_PRIME,
            Move.L_PRIME,
            Move.D2,
            Move.L,
            Move.D_PRIME
        )
    }

    # used when the only matched pair is opposit
    oppositePairMoves = YELLOW_EDGE_PERMUTATION_MOVES[
        (Edge.DF, Edge.DR)
    ]

    while True:

        foundOppositePair = False

        #check all 4 possible D-layer alignments
        for _ in range(4):

            solvedEdges = []

            for edge in YELLOW_EDGES:
                if self.isEdgeSolved(edge):
                    solvedEdges.append(edge)

            #all four yellow-cross edges are permuted correctly
            if len(solvedEdges) == 4:
                return self

            #two edges match
            if len(solvedEdges) == 2:

                solvedPair = tuple(solvedEdges)

                # adjacent pair
                # use the algorithm for that exact pair
                if solvedPair in YELLOW_EDGE_PERMUTATION_MOVES:

                    moves = YELLOW_EDGE_PERMUTATION_MOVES[solvedPair]

                    self = self.applyMoves(moves)

                    # cube changed, so restart detection
                    break

                # the two solved edges are opposite
                else:
                    foundOppositePair = True

            # try another D-layer alignment
            self = self.applyMove(Move.D)

        else:
            # checked all four D rotations without finding an adjacent solved pair. This means we encountered the opposite-pair case.
            if foundOppositePair:
                self = self.applyMoves(oppositePairMoves)
                continue

            raise AssertionError("No valid yellow-edge permutation case found")

def positionYellowCorners(self):

    YELLOW_CORNERS = (
        Corner.DFR,
        Corner.DLF,
        Corner.DBL,
        Corner.DRB
    )

    CORNER_POSITION_MOVES = {

        Corner.DFR: (
            Move.D_PRIME,
            Move.R_PRIME,
            Move.D,
            Move.L,
            Move.D_PRIME,
            Move.R,
            Move.D,
            Move.L_PRIME
        ),

        Corner.DLF: (
            Move.D_PRIME,
            Move.F_PRIME,
            Move.D,
            Move.B,
            Move.D_PRIME,
            Move.F,
            Move.D,
            Move.B_PRIME
        ),

        Corner.DBL: (
            Move.D_PRIME,
            Move.L_PRIME,
            Move.D,
            Move.R,
            Move.D_PRIME,
            Move.L,
            Move.D,
            Move.R_PRIME
        ),

        Corner.DRB: (
            Move.D_PRIME,
            Move.B_PRIME,
            Move.D,
            Move.F,
            Move.D_PRIME,
            Move.B,
            Move.D,
            Move.F_PRIME
        )
    }

    while True:

        positionedCorners = []

        # only check position since rientation does not matter yet.
        for corner in YELLOW_CORNERS:
            if self.cornerPosition[corner] == corner:
                positionedCorners.append(corner)

        # all four corners are in their correct locations
        if len(positionedCorners) == 4:
            return self

        #one corner is correctly positioned. keep it fixed and cycle the other three.
        if len(positionedCorners) == 1:
            fixedCorner = positionedCorners[0]

            moves = CORNER_POSITION_MOVES[fixedCorner]

            self = self.applyMoves(moves)

            # re check the new state
            continue

        #apply any of the moves if none of them are positioned correctly
        if len(positionedCorners) == 0:
            self = self.applyMoves(
                CORNER_POSITION_MOVES[Corner.DFR]
            )

            continue

        # After yellow-edge permutation is complete,
        # 2 or 3 correctly positioned corners should
        # not be a valid case.
        raise AssertionError(
            f"Unexpected number of positioned yellow corners: "
            f"{len(positionedCorners)}"
        )

def orientYellowCorners(self):

    CORNER_TWIST_MOVES = (
        Move.R,
        Move.U,
        Move.R_PRIME,
        Move.U_PRIME
    )

    #process all four yellow corners
    for _ in range(4):

        # Remember which physical corner is currently
        # in the working DFR position
        targetCorner = self.cornerPosition[Corner.DFR]

        # Keep applying the trigger until that same
        # corner returns to DFR with orientation 0
        while not (
            self.cornerPosition[Corner.DFR] == targetCorner
            and self.cornerOrientation[Corner.DFR] == 0
        ):

            self = self.applyMoves(CORNER_TWIST_MOVES)

        # Bring the next yellow corner to DFR
        self = self.applyMove(Move.D)

    return self