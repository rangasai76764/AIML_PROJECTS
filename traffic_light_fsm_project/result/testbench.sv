`timescale 1ns/1ps

module traffic_light_tb;

    reg clk;
    reg reset;
    wire [2:0] light;

    // Instantiate the traffic light controller
    traffic_light_controller uut (
        .clk(clk),
        .reset(reset),
        .light(light)
    );

    // Clock generation
    initial clk = 0;
    always #5 clk = ~clk;

    // Test sequence
    initial begin
        $dumpfile("traffic_light.vcd");       // ✅ VCD output path fixed
        $dumpvars(0, traffic_light_tb);

        reset = 1;
        #10;
        reset = 0;

        #200;  // Run long enough to see full light cycle

        $finish;
    end
endmodule

