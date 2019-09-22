import RPi.GPIO as GPIO
import time

usleep = lambda x: time.sleep(x/1000000.0)
pingpio = 24
maxcycles = 1000

class DHT():
        def read(self):
            if(self.expectPulse(0)==0):
                return "Timeout waiting for start signal low pulse."
            if(self.expectPulse(1)==0):
                return "Timeout waiting for start signal high pulse."
            i=0
            cycles = []
            while (i<80):
              cycles.append(self.expectPulse(0))
              cycles.append(self.expectPulse(1))
              i=i+2
            i=0
            st='0'
            while (i<40):
                lowCycles  = cycles[2*i]
                highCycles = cycles[2*i+1]
                if(((lowCycles == 0) or (highCycles == 0)) and i != 39):
                    #print "error waiting for pulse "+ str(i)+ " L "+str(lowCycles)+ " H "+str(highCycles)
                    return '-'
                if(lowCycles>highCycles):
                    st=st+'0'
                else:
                    st=st+'1'
                i=i+1
            if(len(st)==41):
                return st[:40]
            else:
                return '-'


        def expectPulse(self,level):
            count=0;
            while(GPIO.input(pingpio)==level):
                if(count>=maxcycles):
                    return 0
                count=count+1;
		#usleep(1);
            return count

if __name__ == "__main__":
        dht = DHT()
        while(1):
            try:
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(pingpio, GPIO.OUT)
                GPIO.output(pingpio, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(pingpio, GPIO.LOW)
                usleep(1000)
                GPIO.output(pingpio, GPIO.HIGH)
                usleep(20)
                GPIO.output(pingpio, GPIO.LOW)
                GPIO.setup(pingpio, GPIO.IN)
                usleep(5)
                res =  dht.read()
                if(res!='-'):
                    hum = int(res[:16], 2)
                    t = int(res[17:32], 2)
                    crc = int(res[33:40], 2)
                    crc1 = int(res[:8], 2)
                    crc2 = int(res[9:16], 2)
                    crc3 = int(res[17:24], 2)
                    crc4 = int(res[25:32], 2)
                    hum = float(hum)
                    t = float(t)
                    if((crc1+crc2+crc3+crc4) ==crc ):
                        print "Humidity: "+str(hum/10)
                        print "Temp:"+str(t/10)
                time.sleep(2)
            except:
                time.sleep(2)
