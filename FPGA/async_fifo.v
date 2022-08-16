//==========================================
// Function : Asynchronous FIFO (w/ 2 asynchronous clocks).
// Coder    : Alex Claros F.
// Date     : 15/May/2005.
// Notes    : This implementation is based on the article
//            'Asynchronous FIFO in Virtex-II FPGAs'
//            writen by Peter Alfke. This TechXclusive
//            article can be downloaded from the
//            Xilinx website. It has some minor modifications.
//=========================================

`timescale 1ns/1ps

module aFifo
  #(parameter    DATA_WIDTH    = 8,
                 ADDRESS_WIDTH = 4,
                 FIFO_DEPTH    = (1 << ADDRESS_WIDTH))
    (
        //Reading port
        output reg  [DATA_WIDTH-1:0]        Data_out,
        output reg                          Empty_out,
        input wire                          ReadEn_in,
        input wire                          RClk,
        //Writing port.
        input wire  [DATA_WIDTH-1:0]        Data_in,
        output reg                          Full_out,
        input wire                          WriteEn_in,
        input wire                          WClk,

        input wire                          Clear_in
    );

    reg   [DATA_WIDTH-1:0]              Mem [FIFO_DEPTH-1:0];
    wire  [ADDRESS_WIDTH-1:0]           pNextWordToWrite, pNextWordToRead;
    wire                                EqualAddresses;
    wire                                NextWriteAddressEn, NextReadAddressEn;
    wire                                Set_Status, Rst_Status;
    reg                                 Status;
    wire                                PresetFull, PresetEmpty;

    //  41     //Data ports logic:
    //(Uses a dual-port RAM).
    //'Data_out' logic:
    always @ (posedge RClk)
        if (ReadEn_in &  ! Empty_out)
            Data_out <= Mem[pNextWordToRead];

    //'Data_in' logic:
    always @ (posedge WClk)
        if (WriteEn_in &  ! Full_out)
            Mem[pNextWordToWrite] <= Data_in;

    //Fifo addresses support logic:
    //'Next Addresses' enable logic:
    assign NextWriteAddressEn = WriteEn_in & ~Full_out;
    assign NextReadAddressEn  = ReadEn_in  & ~Empty_out;

    //Addreses (Gray counters) logic:
    GrayCounter GrayCounter_pWr
       (.GrayCount_out(pNextWordToWrite),

        .Enable_in(NextWriteAddressEn),
        .Clear_in(Clear_in),

        .Clk(WClk)
       );

    GrayCounter GrayCounter_pRd
       (.GrayCount_out(pNextWordToRead),
        .Enable_in(NextReadAddressEn),
        .Clear_in(Clear_in),
        .Clk(RClk)
       );


    //'EqualAddresses' logic:
    assign EqualAddresses = (pNextWordToWrite == pNextWordToRead);

    //'Quadrant selectors' logic:
    assign Set_Status = (pNextWordToWrite[ADDRESS_WIDTH-2] ~^ pNextWordToRead[ADDRESS_WIDTH-1]) &
                        (pNextWordToWrite[ADDRESS_WIDTH-1] ^  pNextWordToRead[ADDRESS_WIDTH-2]);

    assign Rst_Status = (pNextWordToWrite[ADDRESS_WIDTH-2] ^  pNextWordToRead[ADDRESS_WIDTH-1]) &
                        (pNextWordToWrite[ADDRESS_WIDTH-1] ~^ pNextWordToRead[ADDRESS_WIDTH-2]);

    //'Status' latch logic:
    always @ (Set_Status, Rst_Status, Clear_in) //D Latch w/ Asynchronous Clear & Preset.
        if (Rst_Status | Clear_in)
            Status = 0;  //Going 'Empty'.
        else if (Set_Status)
            Status = 1;  //Going 'Full'.

    //'Full_out' logic for the writing port:
    assign PresetFull = Status & EqualAddresses;  //'Full' Fifo.

    always @ (posedge WClk, posedge PresetFull) //D Flip-Flop w/ Asynchronous Preset.
        if (PresetFull)
            Full_out <= 1;
        else
            Full_out <= 0;

    //'Empty_out' logic for the reading port:
    assign PresetEmpty = ~Status & EqualAddresses;  //'Empty' Fifo.

    always @ (posedge RClk, posedge PresetEmpty)  //D Flip-Flop w/ Asynchronous Preset.
        if (PresetEmpty)
            Empty_out <= 1;
        else
            Empty_out <= 0;

endmodule



//==========================================
// Function : Code Gray counter.
// Coder    : Alex Claros F.
// Date     : 15/May/2005.
//=======================================

`timescale 1ns/1ps

module GrayCounter
   #(parameter   COUNTER_WIDTH = 4)

    (output reg  [COUNTER_WIDTH-1:0]    GrayCount_out,  //'Gray' code count output.

    input wire                         Enable_in,  //Count enable.
    input wire                         Clear_in,   //Count reset.

    input wire                         Clk);

    reg    [COUNTER_WIDTH-1:0]         BinaryCount;

    always @ (posedge Clk)
        if (Clear_in) begin
            BinaryCount   <= {COUNTER_WIDTH{1'b 0}} + 1;  //Gray count begins @ '1' with
            GrayCount_out <= {COUNTER_WIDTH{1'b 0}};      // first 'Enable_in'.
        end
        else if (Enable_in) begin
            BinaryCount   <= BinaryCount + 1;
            GrayCount_out <= {BinaryCount[COUNTER_WIDTH-1],
                              BinaryCount[COUNTER_WIDTH-2:0] ^ BinaryCount[COUNTER_WIDTH-1:1]};
        end

endmodule


// In an asynchronous FIFO, one clock domain is associated with the write port, and the "head" pointer
// (the next write address) is kept in that clock domain. Similarly, the other clock domain is associated
// with the read port, and the "tail" pointer is kept there.
//
// The problem is that both clock domains need to be able to keep track of the number of words in the FIFO,
//  and the way to do this is to subtract the value of the tail pointer from the value of the head pointer,
//  modulo the size of the RAM. Therefore, each pointer is encoded as Gray code, transferred to the other
//  clock domain and converted back to binary.
//
// It doesn't matter if more than one write happens during a read clock period, or vice-versa. The point is,
// with Gray code encoding, only one bit changes between any pair of values. If one clock happens to catch
// a transition in the other clock domain, at most only one bit can be metastable, and the ambiguity is between
// two adjacent states of the counter.
//
// In other words, each side sees a monotonically increasing sequence of values from the other side, even if
// some values are skipped — and more importantly, even if metastability occurs. Therefore, it isn't possible
// for either clock domain to calculate an erroneous value for the number of words in the FIFO — it simply
// becomes a question of whether it gets the update one clock sooner or later than it otherwise might have.
//
// So, on the write side, the head pointer increments directly, increasing the depth of the FIFO, but the
// updated tail pointer coming from the other side may be delayed. This can only cause the write side to
// overestimate the number of words in the FIFO, and therefore, the FIFO will never overflow.
//
// Similarly, on the read side, the tail pointer increments directly, decreasing the depth of the FIFO, but
// the updated head pointer may be delayed. This can only cause the read side to underestimate the number
// of words in the FIFO, and as a result, it will never underflow.
//
// In fact, you can put any number of synchronizing stages in the path of the Gray code transfers, and the
// only effect this will have is to increase the latency through the FIFO. This is even a configurable parameter
// in the Xilinx dual-clock FIFO generator.