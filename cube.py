from enum import IntEnum

#enums for edges and corners (help with converting to hardware later)
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

#define edges and corners as solved cube
edgePosition =     [Edge.UR, Edge.UF, Edge.UL, Edge.UB, 
                    Edge.DR, Edge.DF, Edge.DL, Edge.DB,
                    Edge.FR, Edge.FL, Edge.BL, Edge.BR]

edgeOrientation =  [0, 0, 0, 0,
                    0, 0, 0, 0,
                    0, 0, 0, 0]

cornerPosition =   [Corner.URF, Corner.UFL, Corner.ULB, Corner.UBR,
                    Corner.DFR, Corner.DLF, Corner.DBL, Corner.DRB]

cornerOrientation = [0, 0, 0, 0,
                    0, 0, 0, 0]