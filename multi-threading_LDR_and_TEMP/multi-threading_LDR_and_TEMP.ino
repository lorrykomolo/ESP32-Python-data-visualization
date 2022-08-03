/* Sensors */
const byte LDR = A2; //Light Dependant Resistor
const byte tempSensor = A4; //LM34 temp sensor

/* Two "independant" timed events */
const long eventTime_1_LDR = 1000; //in ms
const long eventTime_2_temp = 5000; //in ms

/* When did they start the race? */
unsigned long previousTime_1 = 0;
unsigned long previousTime_2 = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {

  /* Updates frequently */
  unsigned long currentTime = millis();

  /* This is my event_1 */
  if ( currentTime - previousTime_1 >= eventTime_1_LDR) {
    Serial.print("LDR: ");
    Serial.println( analogRead(LDR) );
    
    /* Update the timing for the next event*/
    previousTime_1 = currentTime;
  }

    /* This is my event_2 */
  if ( currentTime - previousTime_2 >= eventTime_2_temp) {

    Serial.print("Temp: ");
    Serial.println( analogRead(tempSensor) );

    /* Update the timing for the next event*/
    previousTime_2 = currentTime;
  }

}
