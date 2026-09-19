import cube_defs_pkg::*;

module cube_status (

    input logic [2:0] cpIn [0:7],
    input logic [1:0] coIn [0:7],
    input logic [3:0] epIn [0:11],
    input logic eoIn [0:11],

    input edge target_edge,

    //use an array of width 8 or 12 for all the corner or edge permutations,
    //with 1 meaning solved and 0 being not solved
    output logic cpSolved [0:7],
    output logic coSolved [0:7],
    output logic cSolved  [0:7],

    output logic epSolved [0:11],
    output logic eoSolved [0:11],
    output logic eSolved [0:11],

    //first layer signals
    output logic white_edges_staged [0:3]

    output edge  target_edge_position,
);


localparam edge WHITE_EDGES [0:3] = '{
    UF,
    UR,
    UB,
    UL
};


always_comb begin

    // CORNER STATUS
    for (int i = 0; i < 8; i++) begin

        if (cpIn[i] == i)
            cpSolved[i] = 1'b1;
        else
            cpSolved[i] = 1'b0;

    end


    //keep in mind this all happens in parallel for hardware compared to sequentially in software
    for (int i = 0; i < 8; i++) begin

        if (coIn[i] == 0)
            coSolved[i] = 1'b1;
        else
            coSolved[i] = 1'b0;

    end


    for (int i = 0; i < 8; i++) begin

        cSolved[i] = cpSolved[i] && coSolved[i];

    end


    //edge status
    for (int i = 0; i < 12; i++) begin
        if (epIn[i] == i)
            epSolved[i] = 1'b1;
        else
            epSolved[i] = 1'b0;
    end

    for (int i = 0; i < 12; i++) begin
        if (eoIn[i] == 0)
            eoSolved[i] = 1'b1;
        else
            eoSolved[i] = 1'b0;
    end

    for (int i = 0; i < 12; i++) begin
        eSolved[i] = epSolved[i] && eoSolved[i];
    end


    //white edge staged

    // check white edges
    for (int i = 0; i < 4; i++) begin
        // assume this white edge is not staged
        white_edges_staged[i] = 1'b0;
        // Search the D layer positions
        for (int j = 4; j < 8; j++) begin
            if (
                epIn[j] == WHITE_EDGES[i] &&
                eoIn[j] == 1'b0
            ) begin
                white_edges_staged[i] = 1'b1;
            end
        end
    end

    // defaults
    target_edge_position    = UR;
    target_edge_orientation = 1'b0;
    target_edge_found       = 1'b0;

    //search every edge position for the target cubie
    for (int i = 0; i < 12; i++) begin

        if (epIn[i] == target_edge) begin

            //' is a SystemVerilog typecast
            target_edge_position = edge'(i);
            target_edge_orientation = eoIn[i];
            target_edge_found = 1'b1;

        end

    end

end

endmodule