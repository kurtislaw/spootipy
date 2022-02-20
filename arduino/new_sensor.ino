#include "NewPing.h"

#define TRIGGER_PIN  13  // Arduino pin tied to trigger pin on ping sensor.
#define ECHO_PIN     12  // Arduino pin tied to echo pin on ping sensor.
#define MAX_DISTANCE 500 // Maximum distance we want to ping for (in centimeters). Maximum sensor distance is rated at 400-500cm.

NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE); // NewPing setup of pins and maximum distance.

unsigned int pingSpeed = 1000; // How frequently are we going to send out a ping (in milliseconds). 50ms would be 20 times a second.
unsigned long pingTimer;     // Holds the next ping time.

void setup() {
  Serial.begin(9600); // Open serial monitor at 115200 baud to see ping results.
  pingTimer = millis(); // Start now.
}

void loop() {
  if (millis() >= pingTimer) {   // pingSpeed milliseconds since last ping, do another ping.
    pingTimer += pingSpeed;      // Set the next ping time.
    sonar.ping_timer(echoCheck); // Send out the ping, calls "echoCheck" function every 24uS where you can check the ping status.x
//    delay(500);
  }
  // Do other stuff here, really. Think of it as multi-tasking.
}

void echoCheck() { // Timer2 interrupt calls this function every 24uS where you can check the ping status.
  // Don't do anything here!
  if (sonar.check_timer()) { // This is how you check to see if the ping was received.
    Serial.println(sonar.ping_result / US_ROUNDTRIP_CM); 
  }
  // Don't do anything here!
}
