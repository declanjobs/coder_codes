#ifndef FIR_FILTER_H
#define FIR_FILTER_H

#include <stdint.h>

#define FIR_FILTER_LENGTH 5

//Defining the struct to represent the circular buffer
typedef struct{
    float buff[FIR_FILTER_LENGTH]; //for circular buffer array
    uint8_t buffIndex; //Tracking the index of the circular buffer
    float out; //the output value of the circular buffer
} FIRFilter;

//functions prototype
void FIRFilter_init(FIRFilter *fir);
float FIRFilter_calc(FIRFilter *fir, float inputVal);

#endif