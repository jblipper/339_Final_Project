import serial
import time as t
import numpy as np
import matplotlib.pyplot as plt
value=130
arraySize=600
serialPort=serial.Serial()
serialPort.baudrate=9600
serialPort.port="COM5"
print(serialPort)
serialPort.open()
dataRead=False
data=[]
while (dataRead==False):
     serialPort.write(bytes([value]))
     t.sleep(0.1)
     inByte = serialPort.in_waiting
     #This loop reads in data from the array until byteCount reaches the array size (arraySize)
     byteCount=0
     while ((inByte>0)&(byteCount<arraySize)):
          dataByte=serialPort.read()
          byteCount=byteCount+1
          data=data+[dataByte]
     if (byteCount==arraySize):
          dataRead=True
serialPort.close()
dataOut=np.zeros(arraySize)
arrayIndex=range(arraySize)
#Transform unicode encoding into integers
for i in arrayIndex:
     dataOut[i]=ord(data[i])
#Plot your analog output!
f1=plt.figure()
plt.plot(arrayIndex, dataOut, 'o')
plt.xlabel("array index")
plt.ylabel("8-bit rounded voltage reading")
print('mean:', np.mean(dataOut))