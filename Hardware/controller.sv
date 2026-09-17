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


module controller(
    input logic clk
    input logic reset,
    input logic start,
)