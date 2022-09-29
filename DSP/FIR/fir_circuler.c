#include "fir_circular.h"

//define the variable in the stack memory, including declaration. The value of this
//FIR_FILTER_IMPULSE_RESPONSE array is based on a design (the value represent the behaviour of the filter)
static float FIR_FILTER_IMPULSE_RESPONSE[FIR_FILTER_LENGTH]={0.4,0.3,0.2,0.1,0.05};

//function to initialise the circular buffer value
void FIRFilter_init(FIRFilter *fir){ //use pointer to FIRFilter variable so that we do not need to copy the memory value (more efficient)
    //clear the buffer of the filter
    for(int i=0;i<FIR_FILTER_LENGTH;i++){
        fir->buff[i]=0.0f;
    }

    //Reset the buffer index
    fir->buffIndex=0;

    //clear filter output
    fir->out=0.0f; //'f' to make is as a float
}

//function to calculate (process) the filter output
float FIRFilter_calc(FIRFilter *fir, float inputVal){

    float out=0.0f;

    /*Implementing CIRCULAR BUFER*/
    //Store the latest sample=inputVal into the circular buffer
    fir->buff[fir->buffIndex]=inputVal;

    //Increase the buffer index. retrun to zero if it reach the end of the index (circular buffer)
    fir->buffIndex++;
    uint8_t sumIndex=fir->buffIndex;
    if(fir->buffIndex==FIR_FILTER_LENGTH){
        fir->buffIndex=0;
    }

    //Compute the filtered sample with convolution
    fir->out=0.0f;
    for(int i=0;i<FIR_FILTER_LENGTH;i++){
        //decrese sum index and warp it if necessary
        if(sumIndex>0){
            sumIndex--;
        }
        else{
            sumIndex=FIR_FILTER_LENGTH-1;
        }
        //The convolution process: Multyply the impulse response with the SHIFTED input sample and add it to the output
        fir->out=fir->out+fir->buff[sumIndex]*FIR_FILTER_IMPULSE_RESPONSE[i];
    }

    //return the filtered data
    return out;

}
