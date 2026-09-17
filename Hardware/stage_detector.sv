import cube_defs_pkg::*;

module stage_detector(
    input logic [2:0] cpIn [0:7],
    input logic [1:0] coIn [0:7],
    input logic [3:0] epIn [0:11],
    input logic eoIn [0:11],

    output logic white_cross_solved
    output logic first_layer_done
    output logic second_layer_done
    output logic third_layer_done
    output logic cube_solved
);

always_comb begin

    //check if the white edges are in the right spot and orientaton
    if (
        epIn[UF] == UF && 
        epIn[UR] == UR && 
        epIn[UB] == UB && 
        epIn[UL] == UL &&

        eoIn[UF] == 1'b0 && 
        eoIn[UR] == 1'b0 && 
        eoIn[UB] == 1'b0 && 
        eoIn[UL] == 1'b0 
    ) 
    white_cross_solved = 1'b1;
else 
    white_cross_solved = 1'b0;

    // white cross must be solved, plus the four courners layer edges.
    if (
        white_cross_solved &&

        cpIn[URF] == URF &&
        cpIn[UFL] == UFL &&
        cpIn[ULB] == ULB &&
        cpIn[UBR] == UBR &&

        coIn[URF] == 2'd0 &&
        coIn[UFL] == 2'd0 &&
        coIn[ULB] == 2'd0 &&
        coIn[UBR] == 2'd0
    )
        first_layer_solved = 1'b1;
    else
        first_layer_solved = 1'b0;

    // first layer must be solved, plus the four middle layer edges.
    if (
        first_layer_solved &&

        epIn[FR] == FR &&
        epIn[FL] == FL &&
        epIn[BL] == BL &&
        epIn[BR] == BR &&

        eoIn[FR] == 1'b0 &&
        eoIn[FL] == 1'b0 &&
        eoIn[BL] == 1'b0 &&
        eoIn[BR] == 1'b0
    )
        second_layer_solved = 1'b1;
    else
        second_layer_solved = 1'b0;

    //second layer must be solved plus the last layer edges and corners
    if (
        second_layer_solved &&

        //last-layer edges
        epIn[DF] == DF &&
        epIn[DR] == DR &&
        epIn[DB] == DB &&
        epIn[DL] == DL &&

        eoIn[DF] == 1'b0 &&
        eoIn[DR] == 1'b0 &&
        eoIn[DB] == 1'b0 &&
        eoIn[DL] == 1'b0 &&

        //last layer corners
        cpIn[DFR] == DFR &&
        cpIn[DLF] == DLF &&
        cpIn[DBL] == DBL &&
        cpIn[DRB] == DRB &&

        coIn[DFR] == 2'd0 &&
        coIn[DLF] == 2'd0 &&
        coIn[DBL] == 2'd0 &&
        coIn[DRB] == 2'd0
    )
        cube_solved = 1'b1;
    else
        cube_solved = 1'b0;

end