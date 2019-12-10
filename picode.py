import time 
from time import sleep
from accel import accelmag
from pth import pth
from light import light
from geiger import geiger
import datetime
import csv
from writemod import writemod
k = time.localtime()
filename = str(k[1]) +'_'+str(k[2]) +'_'+str(k[3]) +'_'+  str(k[4]) +'_'+str(k[3]) + '.csv'


fields  = ["Hour","Min","Sec","xGyro","yGyro","zGyro","xAccl","yAccel","zAccel","xMag","yMag","zMag","Lux","Humididty","Pressure","Temp","Incedences/S"]
writemod(fields,filename)

while 1:
    accelOut = accelmag()
    luxOut = light()
    pthOut = pth()

    eventCount = 456
    geigerOut = geiger()
    time.sleep(11)


    k = time.localtime()
    Hour = str(k[3])
    Min =  str(k[4])
    dataOut  = [Hour,Min]
    dataOut.extend(accelOut)
    dataOut.extend(luxOut)
    dataOut.extend(pthOut)
    dataOut.extend(geigerOut)

    writemod(dataOut,filename)
    print(dataOut)

    time.sleep(1)
