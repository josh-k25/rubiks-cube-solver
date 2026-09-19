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

always_ff @(posedge clk) begin
    if (solve_enable) begin
        for (int i = 0; i < 4; i++) begin
            if white_edges_staged[i] !== 0 begin
                
            end
            
        end

    end


end


