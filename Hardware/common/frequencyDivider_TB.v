// ============================================================================
// TESTBENCH FOR frequencyDivider
// ============================================================================
`timescale 1ns / 100ps
module SD_SPI_TB ();
    reg clk;
    reg reset;


    frequencyDivider #(.divider(2),.bitsNumber(2)) uut(
	    .inputCLK(clk),
        .reset(reset)
	);


    initial begin
        clk=0;
        reset=0;
        #50
        reset=1;
        #1
        reset=0;
    end

    always clk = #0.5 ~clk;

    initial begin: TEST_CASE
        $dumpfile("verilogTestBench.vcd");
        $dumpvars(-1, uut);
        #80000 $finish;
    end

endmodule
