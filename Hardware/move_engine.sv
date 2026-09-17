import cube_defs_pkg::*;

module move_engine(
    input logic clk, 
    //move input will come from 
    input move move,

    input logic [2:0] cpIn [0:7],
    input logic [1:0] coIn [0:7],
    input logic [3:0] epIn [0:11],
    input logic eoIn [0:11],

    output logic [2:0] cp [0:7],
    output logic [1:0] co [0:7],
    output logic [3:0] ep [0:11],
    output logic eo [0:11]
);

always_comb begin

    for (int i = 0; i < 12; i++) begin
        edgeMapping[i]          = i;
        edgeOrientationDelta[i] = 1'b0;
    end

    for (int i = 0; i < 8; i++) begin
        cornerMapping[i]          = i;
        cornerOrientationDelta[i] = 2'd0;
    end

    // u move mapping
    U: begin
            edgeMapping[UR] = UB;
            edgeMapping[UF] = UR;
            edgeMapping[UL] = UF;
            edgeMapping[UB] = UL;

            edgeMapping[DR] = DR;
            edgeMapping[DF] = DF;
            edgeMapping[DL] = DL;
            edgeMapping[DB] = DB;

            edgeMapping[FR] = FR;
            edgeMapping[FL] = FL;
            edgeMapping[BL] = BL;
            edgeMapping[BR] = BR;


            cornerMapping[URF] = UBR;
            cornerMapping[UFL] = URF;
            cornerMapping[ULB] = UFL;
            cornerMapping[UBR] = ULB;

            cornerMapping[DFR] = DFR;
            cornerMapping[DLF] = DLF;
            cornerMapping[DBL] = DBL;
            cornerMapping[DRB] = DRB;
        end


        //r move
        R: begin
            edgeMapping[UR] = FR;
            edgeMapping[UF] = UF;
            edgeMapping[UL] = UL;
            edgeMapping[UB] = UB;

            edgeMapping[DR] = BR;
            edgeMapping[DF] = DF;
            edgeMapping[DL] = DL;
            edgeMapping[DB] = DB;

            edgeMapping[FR] = DR;
            edgeMapping[FL] = FL;
            edgeMapping[BL] = BL;
            edgeMapping[BR] = UR;


            cornerMapping[URF] = DFR;
            cornerMapping[UFL] = UFL;
            cornerMapping[ULB] = ULB;
            cornerMapping[UBR] = URF;

            cornerMapping[DFR] = DRB;
            cornerMapping[DLF] = DLF;
            cornerMapping[DBL] = DBL;
            cornerMapping[DRB] = UBR;


            cornerOrientationDelta[URF] = 2'd2;
            cornerOrientationDelta[UFL] = 2'd0;
            cornerOrientationDelta[ULB] = 2'd0;
            cornerOrientationDelta[UBR] = 2'd1;

            cornerOrientationDelta[DFR] = 2'd1;
            cornerOrientationDelta[DLF] = 2'd0;
            cornerOrientationDelta[DBL] = 2'd0;
            cornerOrientationDelta[DRB] = 2'd2;
        end


        //f move
        F: begin
            edgeMapping[UR] = UR;
            edgeMapping[UF] = FL;
            edgeMapping[UL] = UL;
            edgeMapping[UB] = UB;

            edgeMapping[DR] = DR;
            edgeMapping[DF] = FR;
            edgeMapping[DL] = DL;
            edgeMapping[DB] = DB;

            edgeMapping[FR] = UF;
            edgeMapping[FL] = DF;
            edgeMapping[BL] = BL;
            edgeMapping[BR] = BR;


            edgeOrientationDelta[UF] = 1'b1;
            edgeOrientationDelta[DF] = 1'b1;
            edgeOrientationDelta[FR] = 1'b1;
            edgeOrientationDelta[FL] = 1'b1;


            cornerMapping[URF] = UFL;
            cornerMapping[UFL] = DLF;
            cornerMapping[ULB] = ULB;
            cornerMapping[UBR] = UBR;

            cornerMapping[DFR] = URF;
            cornerMapping[DLF] = DFR;
            cornerMapping[DBL] = DBL;
            cornerMapping[DRB] = DRB;


            cornerOrientationDelta[URF] = 2'd1;
            cornerOrientationDelta[UFL] = 2'd2;
            cornerOrientationDelta[ULB] = 2'd0;
            cornerOrientationDelta[UBR] = 2'd0;

            cornerOrientationDelta[DFR] = 2'd2;
            cornerOrientationDelta[DLF] = 2'd1;
            cornerOrientationDelta[DBL] = 2'd0;
            cornerOrientationDelta[DRB] = 2'd0;
        end


        //d move
        D: begin
            edgeMapping[UR] = UR;
            edgeMapping[UF] = UF;
            edgeMapping[UL] = UL;
            edgeMapping[UB] = UB;

            edgeMapping[DR] = DF;
            edgeMapping[DF] = DL;
            edgeMapping[DL] = DB;
            edgeMapping[DB] = DR;

            edgeMapping[FR] = FR;
            edgeMapping[FL] = FL;
            edgeMapping[BL] = BL;
            edgeMapping[BR] = BR;


            cornerMapping[URF] = URF;
            cornerMapping[UFL] = UFL;
            cornerMapping[ULB] = ULB;
            cornerMapping[UBR] = UBR;

            cornerMapping[DFR] = DLF;
            cornerMapping[DLF] = DBL;
            cornerMapping[DBL] = DRB;
            cornerMapping[DRB] = DFR;
        end


        //l move
        L: begin
            edgeMapping[UR] = UR;
            edgeMapping[UF] = UF;
            edgeMapping[UL] = BL;
            edgeMapping[UB] = UB;

            edgeMapping[DR] = DR;
            edgeMapping[DF] = DF;
            edgeMapping[DL] = FL;
            edgeMapping[DB] = DB;

            edgeMapping[FR] = FR;
            edgeMapping[FL] = UL;
            edgeMapping[BL] = DL;
            edgeMapping[BR] = BR;


            cornerMapping[URF] = URF;
            cornerMapping[UFL] = ULB;
            cornerMapping[ULB] = DBL;
            cornerMapping[UBR] = UBR;

            cornerMapping[DFR] = DFR;
            cornerMapping[DLF] = UFL;
            cornerMapping[DBL] = DLF;
            cornerMapping[DRB] = DRB;


            cornerOrientationDelta[URF] = 2'd0;
            cornerOrientationDelta[UFL] = 2'd1;
            cornerOrientationDelta[ULB] = 2'd2;
            cornerOrientationDelta[UBR] = 2'd0;

            cornerOrientationDelta[DFR] = 2'd0;
            cornerOrientationDelta[DLF] = 2'd2;
            cornerOrientationDelta[DBL] = 2'd1;
            cornerOrientationDelta[DRB] = 2'd0;
        end


        //b move
        B: begin
            edgeMapping[UR] = UR;
            edgeMapping[UF] = UF;
            edgeMapping[UL] = UL;
            edgeMapping[UB] = BR;

            edgeMapping[DR] = DR;
            edgeMapping[DF] = DF;
            edgeMapping[DL] = DL;
            edgeMapping[DB] = BL;

            edgeMapping[FR] = FR;
            edgeMapping[FL] = FL;
            edgeMapping[BL] = UB;
            edgeMapping[BR] = DB;


            edgeOrientationDelta[UB] = 1'b1;
            edgeOrientationDelta[DB] = 1'b1;
            edgeOrientationDelta[BL] = 1'b1;
            edgeOrientationDelta[BR] = 1'b1;


            cornerMapping[URF] = URF;
            cornerMapping[UFL] = UFL;
            cornerMapping[ULB] = UBR;
            cornerMapping[UBR] = DRB;

            cornerMapping[DFR] = DFR;
            cornerMapping[DLF] = DLF;
            cornerMapping[DBL] = ULB;
            cornerMapping[DRB] = DBL;


            cornerOrientationDelta[URF] = 2'd0;
            cornerOrientationDelta[UFL] = 2'd0;
            cornerOrientationDelta[ULB] = 2'd1;
            cornerOrientationDelta[UBR] = 2'd2;

            cornerOrientationDelta[DFR] = 2'd0;
            cornerOrientationDelta[DLF] = 2'd0;
            cornerOrientationDelta[DBL] = 2'd2;
            cornerOrientationDelta[DRB] = 2'd1;
        end


        default: begin
        end

    endcase
end

//apply the moves
always_comb begin
    //edge gets positin of new edges based on move
    for (int i = 0; i < 12; i++) begin
        ep[i] = epIn[edgeMapping[i]];
        // xor works the same as modulo 2
        eo[i] = eoIn[edgeMapping[i]] ^ edgeOrientationDelta[i];
    end

    //corners get position of new corner based on move
    for (int i = 0; i < 8; i++) begin

        cp[i] = cpIn[cornerMapping[i]];

        //modulo 3 representation for the corner orientations
        if ((coIn[cornerMapping[i]] + cornerOrientationDelta[i]) >= 3)
            co[i] = coIn[cornerMapping[i]] + cornerOrientationDelta[i] - 3;
        else
            co[i] = coIn[cornerMapping[i]] + cornerOrientationDelta[i];
    end
end


