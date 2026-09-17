module move_engine(
    input logic clk, 
    //move input will come from 
    input logic move,

    input logic [2:0] cpIn [0:7],
    input logic [1:0] coIn [0:7],
    input logic [3:0] epIn [0:11],
    input logic eoIn [0:11],

    output logic [2:0] cp [0:7],
    output logic [1:0] co [0:7],
    output logic [3:0] ep [0:11],
    output logic eo [0:11]
);

