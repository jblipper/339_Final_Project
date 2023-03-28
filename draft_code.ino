int outputPin = 3;
int input0 = A0;
int readings[500]; //The array that will hold our readings
int timeBase=50; //Time between analog readings (for stability)
int readingPtr; //The array pointer that points to the current reading
void setup()
{
pinMode(outputPin, OUTPUT);
pinMode(input0, INPUT);
Serial.begin(9600);
}
void loop()
{
if(Serial.available() > 0)
{
int out=Serial.read();
analogWrite(outputPin, out);
//Make analog readings with delay timeBase
for(readingPtr = 0; readingPtr < 500; readingPtr++)
{
readings[readingPtr] = analogRead(input0);
delayMicroseconds(timeBase);
}
//Write array values to serial port. Note that we round our 10-bit measurements to 8-bit.
for(readingPtr = 0; readingPtr < 500; readingPtr++)
{
Serial.write(highByte(readings[readingPtr]<<6)); //shift bits left six times and use only top eight
}
}
}
