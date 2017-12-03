int outputpin = A0;  //initializes/defines the output pin of the LM35 temperature sensor
                    //this sets the ground pin to LOW and the input voltage pin to high
void setup()
{
Serial.begin(9600);
}

void loop() //main loop
{
int analogValue = analogRead(outputpin);
float millivolts = (analogValue/1024.0) * 3300; //3300 is the voltage provided by NodeMCU
float celsius = millivolts/10;
Serial.print("in DegreeC=   ");
Serial.println(celsius);
delay(1000);
}
