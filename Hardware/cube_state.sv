import cube_defs_pkg::*;

module cube_state(
    input logic clk,
    input logic reset,
    input logic cpIn,
    input logic load,

    //corner permutation 3 bits for 8 corners  
    input logic [2:0] cpIn [0:7],
    //corner orientation 2 bits for 8 corners
    input logic [1:0] coIn [0:7],
    //edge permutation  4 bits for 12 edges
    input logic [3:0] epIn [0:11],
    // edge orientation 2 bits for 12 edges
    input logic eoIn [0:11],

    output logic [2:0] cp [0:7],
    output logic [1:0] co [0:7],
    output logic [3:0] ep [0:11],
    output logic eo [0:11]
);

always_ff @(posedge clk or reset) begin
    if (reset) begin
        ep[UR] <= UR;
        ep[UF] <= UF;
        ep[UL] <= UL;
        ep[UB] <= UB;
        ep[DR] <= DR;
        ep[DF] <= DF;
        ep[DL] <= DL;
        ep[DB] <= DB;
        ep[FR] <= FR;
        ep[FL] <= FL;
        ep[BL] <= BL;
        ep[BR] <= BR;

        cp[URF] <= URF;
        cp[UFL] <= UFL;
        cp[ULB] <= ULB;
        cp[UBR] <= UBR;
        cp[DFR] <= DFR;
        cp[DLF] <= DLF;
        cp[DBL] <= DBL;
        cp[DRB] <= DRB;

        for (int i = 0; i < 12; i++)
            eo[i] <= 1'b0;

        for (int i = 0; i < 8; i++)
            co[i] <= 2'd0;
    end
    
    else if (load) begin
    cp <= cpIn;
    co <= coIn;
    ep <= epIn;
    eo <= eoIn;
    end
end

