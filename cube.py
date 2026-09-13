from enum import IntEnum

#enums for edges and corners assign a number to each part
#helps with iterating between parts and checks
class Edge(IntEnum):
    UR = 0
    UF = 1
    UL = 2
    UB = 3
    DR = 4
    DF = 5 
    DL = 6
    DB = 7
    FR = 8
    FL = 9
    BL = 10
    BR = 11

class Corner(IntEnum):
    URF = 0
    UFL = 1
    ULB = 2
    UBR = 3
    DFR = 4
    DLF = 5
    DBL = 6
    DRB = 7

class Move(IntEnum):
    U = 0
    U2 = 1
    U_PRIME = 2

    R = 3
    R2 = 4
    R_PRIME = 5

    F = 6
    F2 = 7
    F_PRIME = 8

    D = 9
    D2 = 10
    D_PRIME = 11

    L = 12
    L2 = 13
    L_PRIME = 14

    B = 15
    B2 = 16
    B_PRIME = 17

#define edges and corners as solved cube
SOLVED_EDGE_POSITION =         (Edge.UR, Edge.UF, Edge.UL, Edge.UB, 
                                Edge.DR, Edge.DF, Edge.DL, Edge.DB,
                                Edge.FR, Edge.FL, Edge.BL, Edge.BR)

SOLVED_EDGE_ORIENTATION =      (0, 0, 0, 0,
                                0, 0, 0, 0,
                                0, 0, 0, 0)

SOLVED_CORNER_POSITION =       (Corner.URF, Corner.UFL, Corner.ULB, Corner.UBR,
                                Corner.DFR, Corner.DLF, Corner.DBL, Corner.DRB)

SOLVED_CORNER_ORIENTATION =    (0, 0, 0, 0,
                                0, 0, 0, 0)

#Create move table to be referenced in the applyMove function.
#For each destination position, the mapping gives the source position.
#in the old cube state whose cubie moves into that destination.
#Mapping[destination] = source position in the old cube state.
#Orientation delta tells how the cubie's reference facelet changes
# relative to the reference facelet of its destination position.
U_EDGE_MAPPING =               (Edge.UB, Edge.UR, Edge.UF, Edge.UL,
                                Edge.DR, Edge.DF, Edge.DL, Edge.DB,
                                Edge.FR, Edge.FL, Edge.BL, Edge.BR)

U_EDGE_ORIENTATION =           (0, 0, 0, 0,
                                0, 0, 0, 0,
                                0, 0, 0, 0)

U_CORNER_MAPPING =             (Corner.UBR, Corner.URF, Corner.UFL, Corner.ULB,
                                Corner.DFR, Corner.DLF, Corner.DBL, Corner.DRB)

U_CORNER_ORIENTATION =         (0, 0, 0, 0,
                                0, 0, 0, 0)

R_EDGE_MAPPING =               (Edge.FR, Edge.UF, Edge.UL, Edge.UB,
                                Edge.BR, Edge.DF, Edge.DL, Edge.DB,
                                Edge.DR, Edge.FL, Edge.BL, Edge.UR)

R_EDGE_ORIENTATION =           (0, 0, 0, 0,
                                0, 0, 0, 0,
                                0, 0, 0, 0)

R_CORNER_MAPPING =             (Corner.DFR, Corner.UFL, Corner.ULB, Corner.URF,
                                Corner.DRB, Corner.DLF, Corner.DBL, Corner.UBR)

R_CORNER_ORIENTATION =         (2, 0, 0, 1,
                                1, 0, 0, 2)

F_EDGE_MAPPING =               (Edge.UR, Edge.FL, Edge.UL, Edge.UB,
                                Edge.DR, Edge.FR, Edge.DL, Edge.DB,
                                Edge.UF, Edge.DF, Edge.BL, Edge.BR)

F_EDGE_ORIENTATION =           (0, 1, 0, 0,
                                0, 1, 0, 0,
                                1, 1, 0, 0)

F_CORNER_MAPPING =             (Corner.UFL, Corner.DLF, Corner.ULB, Corner.UBR,
                                Corner.URF, Corner.DFR, Corner.DBL, Corner.DRB)

F_CORNER_ORIENTATION =         (1, 2, 0, 0,
                                2, 1, 0, 0)

D_EDGE_MAPPING =               (Edge.UR, Edge.UF, Edge.UL, Edge.UB,
                                Edge.DF, Edge.DL, Edge.DB, Edge.DR,
                                Edge.FR, Edge.FL, Edge.BL, Edge.BR)

D_EDGE_ORIENTATION =           (0, 0, 0, 0,
                                0, 0, 0, 0,
                                0, 0, 0, 0)

D_CORNER_MAPPING =             (Corner.URF, Corner.UFL, Corner.ULB, Corner.UBR,
                                Corner.DLF, Corner.DBL, Corner.DRB, Corner.DFR)

D_CORNER_ORIENTATION =         (0, 0, 0, 0,
                                0, 0, 0, 0)

L_EDGE_MAPPING =               (Edge.UR, Edge.UF, Edge.BL, Edge.UB,
                                Edge.DR, Edge.DF, Edge.FL, Edge.DB,
                                Edge.FR, Edge.UL, Edge.DL, Edge.BR)

L_EDGE_ORIENTATION =           (0, 0, 0, 0,
                                0, 0, 0, 0,
                                0, 0, 0, 0)

L_CORNER_MAPPING =             (Corner.URF, Corner.ULB, Corner.DBL, Corner.UBR,
                                Corner.DFR, Corner.UFL, Corner.DLF, Corner.DRB)

L_CORNER_ORIENTATION =         (0, 1, 2, 0,
                                0, 2, 1, 0)


B_EDGE_MAPPING =               (Edge.UR, Edge.UF, Edge.UL, Edge.BR,
                                Edge.DR, Edge.DF, Edge.DL, Edge.BL,
                                Edge.FR, Edge.FL, Edge.UB, Edge.DB)

B_EDGE_ORIENTATION =           (0, 0, 0, 1,
                                0, 0, 0, 1,
                                0, 0, 1, 1)

B_CORNER_MAPPING =             (Corner.URF, Corner.UFL, Corner.UBR, Corner.DRB,
                                Corner.DFR, Corner.DLF, Corner.ULB, Corner.DBL)

B_CORNER_ORIENTATION =         (0, 0, 1, 2,
                                0, 0, 2, 1)

#lookup table to be referenced in the apply move function
BASE_MOVE_TABLE = {
    Move.U:    (U_EDGE_MAPPING,
                U_EDGE_ORIENTATION,
                U_CORNER_MAPPING,
                U_CORNER_ORIENTATION),

    Move.R:   (R_EDGE_MAPPING,
            R_EDGE_ORIENTATION,
            R_CORNER_MAPPING,
            R_CORNER_ORIENTATION),


    Move.F:   (F_EDGE_MAPPING,
            F_EDGE_ORIENTATION,
            F_CORNER_MAPPING,
            F_CORNER_ORIENTATION),

    Move.D:   (D_EDGE_MAPPING,
            D_EDGE_ORIENTATION,
            D_CORNER_MAPPING,
            D_CORNER_ORIENTATION),

    Move.L:    (L_EDGE_MAPPING,
                L_EDGE_ORIENTATION,
                L_CORNER_MAPPING,
                L_CORNER_ORIENTATION),

    Move.B:   (B_EDGE_MAPPING,
            B_EDGE_ORIENTATION,
            B_CORNER_MAPPING,
            B_CORNER_ORIENTATION),
}

#Dictionary for all the moves (base moves, how many times to use that move)
MOVE_DEFINITIONS = {
    Move.U:       (Move.U, 1),
    Move.U2:      (Move.U, 2),
    Move.U_PRIME: (Move.U, 3),

    Move.R:       (Move.R, 1),
    Move.R2:      (Move.R, 2),
    Move.R_PRIME: (Move.R, 3),

    Move.F:       (Move.F, 1),
    Move.F2:      (Move.F, 2),
    Move.F_PRIME: (Move.F, 3),

    Move.D:       (Move.D, 1),
    Move.D2:      (Move.D, 2),
    Move.D_PRIME: (Move.D, 3),

    Move.L:       (Move.L, 1),
    Move.L2:      (Move.L, 2),
    Move.L_PRIME: (Move.L, 3),

    Move.B:       (Move.B, 1),
    Move.B2:      (Move.B, 2),
    Move.B_PRIME: (Move.B, 3)
}

class cubeState:
    def __init__(self):
        self.edgePosition = list(SOLVED_EDGE_POSITION) 

        self.edgeOrientation = list(SOLVED_EDGE_ORIENTATION)

        self.cornerPosition = list(SOLVED_CORNER_POSITION)

        self.cornerOrientation = list(SOLVED_CORNER_ORIENTATION)


    def applyMove(currentState, move):
    # select mapping/delta tables based on move

        baseMove, turns = MOVE_DEFINITIONS[move]

        edgeMapping, edgeOrientation, cornerMapping, cornerOrientation = BASE_MOVE_TABLE[baseMove]

        for i in range(turns):

            newState = cubeState()

            for destination in range(12):
                source = edgeMapping[destination]

                newState.edgePosition[destination] = currentState.edgePosition[source]

                newState.edgeOrientation[destination] = (currentState.edgeOrientation[source] + edgeOrientation[destination]) % 2

            for destination in range(8):
                source = cornerMapping[destination]
        
                newState.cornerPosition[destination] = currentState.cornerPosition[source]
        
                newState.cornerOrientation[destination] = (currentState.cornerOrientation[source] + cornerOrientation[destination]) % 3

            currentState = newState

        return newState

    def applyMoves(self, moves):
        currentState = self

        for move in moves:
            currentState = currentState.applyMove(move)

        return currentState

    def identityTest(self, move):
        cube = cubeState()

        #save the original solved state
        originalEdgePosition = cube.edgePosition.copy()
        originalEdgeOrientation = cube.edgeOrientation.copy()
        originalCornerPosition = cube.cornerPosition.copy()
        originalCornerOrientation = cube.cornerOrientation.copy()

        #four quarter-turns should equal the identity
        for i in range(4):
            cube = cube.applyMove(move)

        assert cube.edgePosition == originalEdgePosition
        assert cube.edgeOrientation == originalEdgeOrientation
        assert cube.cornerPosition == originalCornerPosition
        assert cube.cornerOrientation == originalCornerOrientation

        print(f"{move.name}^4 identity test passed")

    #checking for edge being solved is the first step in solving white cross
    #Argument will be Edge.XX so no need to have Edge. in method
    def isEdgeSolved(self, edge):
        if self.edgePosition[edge] == edge and self.edgeOrientation[edge] == 0:
            return True
        else:
            return False

    def getEdgeData(self, edge):
        #get the position of the cubie
        position = self.edgePosition.index(edge)

        #use cubie as a reference to check what orientation it is 
        return (position,self.edgeOrientation[position])

    def isCornerSolved(self, corner):
        if self.cornerPosition[corner] == corner and self.cornerOrientation[corner] == 0:
            return True
        else:
            return False

    def getCornerData(self, corner):

        position = self.cornerPosition.index(corner)

        return (position, self.cornerOrientation[position])

    def isFirstLayerSolved(self):

        if (
            self.isEdgeSolved(Edge.UR)
            and self.isEdgeSolved(Edge.UF)
            and self.isEdgeSolved(Edge.UL)
            and self.isEdgeSolved(Edge.UB)
            and self.isCornerSolved(Corner.URF)
            and self.isCornerSolved(Corner.UFL)
            and self.isCornerSolved(Corner.ULB)
            and self.isCornerSolved(Corner.UBR)
        ):
            return True

        else:
            return False

    #going to check for first and second layer. not only the second as the name might imply
    def isSecondLayerSolved(self):
        if (
            self.isEdgeSolved(Edge.UR)
            and self.isEdgeSolved(Edge.UF)
            and self.isEdgeSolved(Edge.UL)
            and self.isEdgeSolved(Edge.UB)
            and self.isCornerSolved(Corner.URF)
            and self.isCornerSolved(Corner.UFL)
            and self.isCornerSolved(Corner.ULB)
            and self.isCornerSolved(Corner.UBR)
            and self.isEdgeSolved(Edge.FR)
            and self.isEdgeSolved(Edge.FL)
            and self.isEdgeSolved(Edge.BL)
            and self.isEdgeSolved(Edge.BR)
        ):
            return True

        else:
            return False

    def printState(self):

        print("EDGES")
        print("-----")

        for position in Edge:
            cubie = self.edgePosition[position]
            orientation = self.edgeOrientation[position]

            print(
                f"{position.name}: "
                f"{cubie.name}, orientation {orientation}"
            )

        print()

        print("CORNERS")
        print("-------")

        for position in Corner:
            cubie = self.cornerPosition[position]
            orientation = self.cornerOrientation[position]

            print(
                f"{position.name}: "
                f"{cubie.name}, orientation {orientation}"
            )