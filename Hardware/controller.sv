import cube_defs_pkg::*;

/*
FSM IDEA STATES (DRAFT):

RESET:
    - Reset is handled by the reset signal rather than a dedicated FSM state.
    - cube_state resets cp/co/ep/eo to the solved cube.
    - controller resets to IDLE.
    - scramble index resets to 0.

IDLE:
    - Do nothing to the cube.
    - Wait for start input.
    - On start begin applying the predefined scramble.

APPLY_MOVE:
    - Output the current logical scramble move.
    - Pulse move_start for one cycle.
    - The move sequencer takes that logical move and does it
    - immediately go to WAIT_MOVE.

WAIT_MOVE:
    - Wait for move_done from the move sequencer.
    - While waiting, do not request another move.
    - When move_done goes high:
        - If more scramble moves remain:
            - increment scramble index and return to APPLY_MOVE
        - If scramble is finished:
            - go to SOLVE

SOLVE:
    - Scramble is finished.
    - Enable the LBL solving logic.
    - Later, the LBL controller will choose move sequences based on stage/case detector signals.
    - When cube_solved goes high, go to DONE.

DONE:
    - Cube is solved.
    - Stop issuing moves.
    - Stay until reset.
*/



module controller (
    input  logic clk,
    input  logic reset,
    input  logic start,

    // From move sequencer
    input  logic move_done,

    // From stage detector
    input  logic cube_solved,

    // To move sequencer
    output moves move,
    output logic move_start,
    
    // Tells future LBL logic that scrambling is finished
    output logic solve_enable
);


    // FSM states
    typedef enum logic [2:0] {
        IDLE,
        APPLY_MOVE,
        WAIT_MOVE,
        SOLVE,
        DONE
    } state_t;

    state_t current_state;
    state_t next_state;


    logic [2:0] scramble_index;
    moves scramble_move;

    localparam int SCRAMBLE_LENGTH = 5;


    // Hard-coded scramble
    // R U F R' U2


    always_comb begin

        case (scramble_index)

            3'd0: scramble_move = R;
            3'd1: scramble_move = U;
            3'd2: scramble_move = F;
            3'd3: scramble_move = R_PRIME;
            3'd4: scramble_move = U2;

            default: scramble_move = U;
        endcase
    end



    always_ff @(posedge clk) begin

        if (reset) begin
            current_state  <= IDLE;
            scramble_index <= 3'd0;
        end

        else begin
            current_state <= next_state;
            //A logical scramble move has finished
            if (
                current_state == WAIT_MOVE &&
                move_done
            ) begin

                //Only increment if another move exists
                if (scramble_index < SCRAMBLE_LENGTH - 1)
                    scramble_index <= scramble_index + 1'b1;
            end
        end
    end



    always_comb begin

        //default
        next_state   = current_state;
        move_start   = 1'b0;
        solve_enable = 1'b0;

        //current scramble move is continuously available
        move = scramble_move;


        case (current_state)

            //do and wait for user to start
            IDLE: begin
                if (start)
                    next_state = APPLY_MOVE;
            end


            // Tell move sequencer to execute the move
            APPLY_MOVE: begin
                move_start = 1'b1;
                next_state = WAIT_MOVE;
            end


            //wait untl the moves begin
            WAIT_MOVE: begin
                if (move_done) begin
                    // last scramble move finished
                    if (scramble_index == SCRAMBLE_LENGTH - 1)
                        next_state = SOLVE;
                    //more scramble moves remain
                    else
                        next_state = APPLY_MOVE;
                end
            end


            //make solver do its thing
            SOLVE: begin
                solve_enable = 1'b1;
                if (cube_solved)
                    next_state = DONE;
            end


            //cube is solved
            DONE: begin
                next_state = DONE;
            end


            default: begin
                next_state = IDLE;
            end

        endcase

    end

endmodule