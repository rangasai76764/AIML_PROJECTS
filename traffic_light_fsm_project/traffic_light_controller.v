`timescale 1ns/1ps

module traffic_light_controller(
    input clk,
    input reset,
    output reg [2:0] light
);

    typedef enum reg [1:0] {
        RED    = 2'b00,
        GREEN  = 2'b01,
        YELLOW = 2'b10
    } state_t;

    state_t current_state, next_state;
    reg [3:0] counter;

    always @(posedge clk or posedge reset) begin
        if (reset) begin
            current_state <= RED;
            counter <= 0;
        end else begin
            if (counter == 4 || (current_state == YELLOW && counter == 2)) begin
                current_state <= next_state;
                counter <= 0;
            end else begin
                counter <= counter + 1;
            end
        end
    end

    always @(*) begin
        case (current_state)
            RED: begin
                light = 3'b100;  // Red ON
                next_state = GREEN;
            end
            GREEN: begin
                light = 3'b001;  // Green ON
                next_state = YELLOW;
            end
            YELLOW: begin
                light = 3'b010;  // Yellow ON
                next_state = RED;
            end
            default: begin
                light = 3'b100;
                next_state = RED;
            end
        endcase
    end
endmodule
