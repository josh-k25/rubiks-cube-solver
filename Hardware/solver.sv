import cube_defs_pkg::*;
import solver_defs_pkg::*;


module solver(
    input logic clk,
    input logic solve_enable,
    input logic move_start,
    input logic [2:0] cpIn [0:7],
    input logic [1:0] coIn [0:7],
    input logic [3:0] epIn [0:11],
    input logic eoIn [0:11],
    input logic white_cross_solved
    input logic first_layer_done
    input logic second_layer_done
    input logic third_layer_done
    input logic cube_solved

    output logic white_edges_staged [0:3]

    output logic move
);

logic [1:0] target_index;
logic white_edges_staging_done;

always_ff @(posedge clk) begin

    if (reset) begin
        target_index              <= 2'd0;
        white_edges_staging_done  <= 1'b0;
    end

    else if (solve_enable) begin

        // Current white edge is already staged
        if (white_edges_staged[target_index]) begin

            // Move on to the next white edge
            if (target_index < 2'd3) begin
                target_index <= target_index + 1'b1;
            end

            // All four white edges have been staged
            else begin
                white_edges_staging_done <= 1'b1;
            end

        end

        // If the current edge is not staged,
        // keep target_index the same.
        // Solver logic will use its position/orientation
        // to determine which move to perform.

    end

end
always_comb begin

    case (target_index)

        2'd0: target_edge = UF;
        2'd1: target_edge = UR;
        2'd2: target_edge = UB;
        2'd3: target_edge = UL;

        default: target_edge = UF;

    endcase

end

endmodule
