import serial
import time as t
import numpy as np
import matplotlib.pyplot as plt
value=130
arraySize=600
serialPort=serial.Serial()
serialPort.baudrate=9600
serialPort.port="COM3"
print(serialPort)
serialPort.open()
dataRead=False
data=[]
dataOut=np.zeros(arraySize)
arrayIndex=range(arraySize)

while (dataRead==False):
     serialPort.write(bytes([value]))
     t.sleep(0.1)
     inByte = serialPort.in_waiting
     #This loop reads in data from the array until byteCount reaches the array size (arraySize)
     byteCount=0
     while ((inByte>0)&(byteCount<arraySize)):
          #dataByte=serialPort.read()
          dataByte1=serialPort.read()
          dataByte2=serialPort.read()
          dataOut[byteCount] = ord(dataByte1)*4+(ord(dataByte2)>>6)          
          byteCount=byteCount+1
          #data=data+[dataByte]
     if (byteCount==arraySize):
          dataRead=True
serialPort.close()
#Transform unicode encoding into integers
#for i in arrayIndex:
    # dataOut[i]=ord(data[i])
#Plot your analog output!
f1=plt.figure()
plt.plot(arrayIndex, dataOut, 'o')
plt.xlabel("array index")
plt.ylabel("10-bit rounded voltage reading")
print('mean:', np.mean(dataOut))

np.savetxt('2candles_10bit_363_23.csv', dataOut, delimiter=",")