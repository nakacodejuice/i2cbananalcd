#include <wiringPi.h> 
#include <pcf8574.h> 
#include <stdio.h>
#include "LiquidCrystal.h"

int main() 
{ 
        int i; 
        pcf8574Setup(100,0x27);                                  
        for(i=0;i<8;i++) pinMode(100+i,OUTPUT);                                                                                                
        while(1)                                                 
        { 
                i = 0; 
                for(i=0;i<=8;i++)                                             
                { 
                        printf("Current LED = %d\n",100+i);                      
                        digitalWrite((100+i),HIGH);                       
                        delay(500);                                       
                        digitalWrite((100+i),0);                         
                        delay(500);                                       
                } 
        } 
   
}
