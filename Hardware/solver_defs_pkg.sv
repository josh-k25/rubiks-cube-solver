package solver_defs_pkg;

typedef enum logic [4:0] {

    //first-layer corner insertion
    SEQ_INSERT_URF,
    SEQ_INSERT_UFL,
    SEQ_INSERT_ULB,
    SEQ_INSERT_UBR,

    //first-layer corner ejection
    SEQ_EJECT_URF,
    SEQ_EJECT_UFL,
    SEQ_EJECT_ULB,
    SEQ_EJECT_UBR,

    //second-layer sequences
    //these are ejection sequences
    SEQ_SECOND_FL_1,
    SEQ_SECOND_FR_1,
    SEQ_SECOND_BL_1,
    SEQ_SECOND_BR_1,

    //these are solving ones
    SEQ_SECOND_FL_0,
    SEQ_SECOND_FR_0,
    SEQ_SECOND_BL_0,
    SEQ_SECOND_BR_0,

    //yellow cross
    SEQ_YELLOW_CROSS,
    SEQ_YELLOW_CROSS_D,
    SEQ_YELLOW_CROSS_D_PRIME,
    SEQ_YELLOW_CROSS_D2,

    //yellow edge permutation
    SEQ_YELLOW_EDGE_DF_DR,
    SEQ_YELLOW_EDGE_DR_DB,
    SEQ_YELLOW_EDGE_DB_DL,
    SEQ_YELLOW_EDGE_DF_DL,

    // Yellow corner positioning
    SEQ_POSITION_DFR,
    SEQ_POSITION_DLF,
    SEQ_POSITION_DBL,
    SEQ_POSITION_DRB,

    //yellow corner orientation
    SEQ_TWIST_CORNER

} sequence_id_t;

import cube_defs_pkg::*;
import solver_defs_pkg::*;

module solver_sequence_rom (

    input  sequence_id_t sequence_id,
    input  logic [3:0] step_index,

    output moves move,
    output logic [3:0] sequence_length,
    output logic valid_step

);

    localparam int NUM_SEQUENCES       = 29;
    localparam int MAX_SEQUENCE_LENGTH = 8;


    /*
    SEQUENCE ROM

    sequence_rom[sequence_id][step_index]

    U is used only as padding for sequences shorter than 8 moves 
    since the arrays all have to be the same length
    and the actual number of moves executed is limited by the sequence length rom arrays
    */

    localparam moves sequence_rom
        [0:NUM_SEQUENCES-1]
        [0:MAX_SEQUENCE_LENGTH-1] = '{

        // FIRST LAYER CORNER INSERTION

        // SEQ_INSERT_URF
        // R' D' R D
        '{
            R_PRIME, D_PRIME, R, D,
            U, U, U, U
        },

        // SEQ_INSERT_UFL
        // L D L' D'
        '{
            L, D, L_PRIME, D_PRIME,
            U, U, U, U
        },

        // SEQ_INSERT_ULB
        // L' D' L D
        '{
            L_PRIME, D_PRIME, L, D,
            U, U, U, U
        },

        // SEQ_INSERT_UBR
        // R D R' D'
        '{
            R, D, R_PRIME, D_PRIME,
            U, U, U, U
        },


        // FIRST LAYER CORNER EJECTION
        // SEQ_EJECT_URF
        // R' D' R
        '{
            R_PRIME, D_PRIME, R,
            U, U, U, U, U
        },

        // SEQ_EJECT_UFL
        // L D L'
        '{
            L, D, L_PRIME,
            U, U, U, U, U
        },

        // SEQ_EJECT_ULB
        // L' D' L
        '{
            L_PRIME, D_PRIME, L,
            U, U, U, U, U
        },

        // SEQ_EJECT_UBR
        // R D R'
        '{
            R, D, R_PRIME,
            U, U, U, U, U
        },


        // SECOND LAYER

        // SEQ_SECOND_FL_1
        // D L D' L' D' F' D F
        '{
            D, L, D_PRIME, L_PRIME,
            D_PRIME, F_PRIME, D, F
        },

        // SEQ_SECOND_FR_1
        // D' R' D R D F D' F'
        '{
            D_PRIME, R_PRIME, D, R,
            D, F, D_PRIME, F_PRIME
        },

        // SEQ_SECOND_BL_1
        // D' L' D L D B D' B'
        '{
            D_PRIME, L_PRIME, D, L,
            D, B, D_PRIME, B_PRIME
        },

        // SEQ_SECOND_BR_1
        // D R D' R' D' B' D B
        '{
            D, R, D_PRIME, R_PRIME,
            D_PRIME, B_PRIME, D, B
        },

        // SEQ_SECOND_FL_0
        // F' D' F D L D L' D'
        '{
            F_PRIME, D_PRIME, F, D,
            L, D, L_PRIME, D_PRIME
        },

        // SEQ_SECOND_FR_0
        // F D F' D' R' D' R D
        '{
            F, D, F_PRIME, D_PRIME,
            R_PRIME, D_PRIME, R, D
        },

        // SEQ_SECOND_BL_0
        // B D B' D' L' D' L D
        '{
            B, D, B_PRIME, D_PRIME,
            L_PRIME, D_PRIME, L, D
        },

        // SEQ_SECOND_BR_0
        // B' D' B D R D R' D'
        '{
            B_PRIME, D_PRIME, B, D,
            R, D, R_PRIME, D_PRIME
        },


        // YELLOW CROSS

        // SEQ_YELLOW_CROSS
        // F' R' D' R D F
        '{
            F_PRIME, R_PRIME, D_PRIME, R,
            D, F, U, U
        },

        // SEQ_YELLOW_CROSS_D
        // D F' R' D' R D F
        '{
            D, F_PRIME, R_PRIME, D_PRIME,
            R, D, F, U
        },

        // SEQ_YELLOW_CROSS_D_PRIME
        // D' F' R' D' R D F
        '{
            D_PRIME, F_PRIME, R_PRIME, D_PRIME,
            R, D, F, U
        },

        // SEQ_YELLOW_CROSS_D2
        // D2 F' R' D' R D F
        '{
            D2, F_PRIME, R_PRIME, D_PRIME,
            R, D, F, U
        },


        // YELLOW EDGE PERMUTATION

        // SEQ_YELLOW_EDGE_DF_DR
        // F' D' F D' F' D2 F D'
        '{
            F_PRIME, D_PRIME, F, D_PRIME,
            F_PRIME, D2, F, D_PRIME
        },

        // SEQ_YELLOW_EDGE_DR_DB
        // R' D' R D' R' D2 R D'
        '{
            R_PRIME, D_PRIME, R, D_PRIME,
            R_PRIME, D2, R, D_PRIME
        },

        // SEQ_YELLOW_EDGE_DB_DL
        // B' D' B D' B' D2 B D'
        '{
            B_PRIME, D_PRIME, B, D_PRIME,
            B_PRIME, D2, B, D_PRIME
        },

        // SEQ_YELLOW_EDGE_DF_DL
        // L' D' L D' L' D2 L D'
        '{
            L_PRIME, D_PRIME, L, D_PRIME,
            L_PRIME, D2, L, D_PRIME
        },


        // YELLOW CORNER POSITIONING

        // SEQ_POSITION_DFR
        // D' R' D L D' R D L'
        '{
            D_PRIME, R_PRIME, D, L,
            D_PRIME, R, D, L_PRIME
        },

        // SEQ_POSITION_DLF
        // D' F' D B D' F D B'
        '{
            D_PRIME, F_PRIME, D, B,
            D_PRIME, F, D, B_PRIME
        },

        // SEQ_POSITION_DBL
        // D' L' D R D' L D R'
        '{
            D_PRIME, L_PRIME, D, R,
            D_PRIME, L, D, R_PRIME
        },

        // SEQ_POSITION_DRB
        // D' B' D F D' B D F'
        '{
            D_PRIME, B_PRIME, D, F,
            D_PRIME, B, D, F_PRIME
        },

        // YELLOW CORNER ORIENTATION

        // SEQ_TWIST_CORNER
        // R U R' U'
        '{
            R, U, R_PRIME, U_PRIME,
            U, U, U, U
        }
    };


    // LENGTH ROM

    localparam logic [3:0] sequence_lengths
        [0:NUM_SEQUENCES-1] = '{

        // Corner insertions
        4'd4,
        4'd4,
        4'd4,
        4'd4,

        // Corner ejections
        4'd3,
        4'd3,
        4'd3,
        4'd3,

        // Second layer
        4'd8,
        4'd8,
        4'd8,
        4'd8,
        4'd8,
        4'd8,
        4'd8,
        4'd8,

        // Yellow cross
        4'd6,
        4'd7,
        4'd7,
        4'd7,

        // Yellow edge permutation
        4'd8,
        4'd8,
        4'd8,
        4'd8,

        // Yellow corner positioning
        4'd8,
        4'd8,
        4'd8,
        4'd8,

        // Yellow corner orientation
        4'd4
    };


    // rom read logic
    always_comb begin

        // defaults
        move            = U;
        sequence_length = 4'd0;
        valid_step      = 1'b0;

        // make sure sequence ID is valid
        if (sequence_id < NUM_SEQUENCES) begin

            sequence_length = sequence_lengths[sequence_id];

            // only read an actual move when inside the sequence
            if (step_index < sequence_lengths[sequence_id]) begin

                move = sequence_rom[sequence_id][step_index];

                valid_step = 1'b1;

            end

        end

    end

endmodule

endpackage