
module frequencyDivider#(parameter divider=10, parameter bitsNumber=4)(
	input   wire inputCLK,
    input   wire reset,
	output  reg  outputCLK
	);
    reg [bitsNumber-1:0] count;
    
    //Inicializacion
    initial begin count=0; outputCLK=0; end

    //Logica Secuencial
    always@(posedge inputCLK , posedge reset) begin
        if (reset == 1'b1) begin
            count <= 0;
            outputCLK <= 0;
        end else if (count == divider/2 -1) begin
            count <= count+1;
            outputCLK <= 1;
        end else if(count == divider-1) begin
            count <= 0;
            outputCLK <= 0;
        end else begin
            count <= count+1;  
        end  
    end
    
endmodule