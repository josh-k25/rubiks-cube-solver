package cube_defs_pkg;

//all edges as enums for readability
typedef enum logic [3:0]{
    UR = 4'd0,
    UF = 4'd1,
    UL = 4'd2,
    UB = 4'd3,
    DR = 4'd4,
    DF = 4'd5,
    DL = 4'd6,
    DB = 4'd7,
    FR = 4'd8,
    FL = 4'd9,
    BL = 4'd10,
    BR = 4'd11
} edge;

//all corners as enums for readability
typedef enum logic [2:0]{
    URF = 3'd0,
    UFL = 3'd1,
    ULB = 3'd2,
    UBR = 3'd3,
    DFR = 3'd4,
    DLF = 3'd5,
    DBL = 3'd6,
    DRB = 3'd7
} corner;

typedef enum logic [4:0]{
    U,
    U2,
    U_PRIME,

    R,
    R2,
    R_PRIME,

    F,
    F2,
    F_PRIME,

    D,
    D2,
    D_PRIME,

    L,
    L2,
    L_PRIME,

    B,
    B2,
    B_PRIME
} moves;

endpackage