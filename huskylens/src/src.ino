#include "HUSKYLENS.h"

HUSKYLENS huskylens;

void setup() {
    Serial.begin(9600);
    Wire.begin();
    
    while (!huskylens.begin(Wire)) {
        Serial.println("HuskyLens not detected!");
        delay(1000);
    }
    
    huskylens.writeAlgorithm(ALGORITHM_OBJECT_RECOGNITION);
    Serial.println("HuskyLens ready in Object Recognition mode");
}

void loop() {
    if (huskylens.request()) {
        HUSKYLENSResult result = huskylens.read();
        
        if (result.command == COMMAND_RETURN_BLOCK) {
            Serial.print("Object ID: ");
            Serial.print(result.ID);
            Serial.print(", X: ");
            Serial.print(result.xCenter);
            Serial.print(", Y: ");
            Serial.print(result.yCenter);
            Serial.print(", Width: ");
            Serial.print(result.width);
            Serial.print(", Height: ");
            Serial.println(result.height);
        }
    }
    delay(100);
}