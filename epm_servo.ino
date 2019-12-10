
#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int data[3];    // variable to store the servo position
int i = 0;
int inPin1 = A3;
int inPin2 = A2;
int motor1 = 7;
int motor2 = 8;
bool prev_state = false;
bool expand = false;
bool contract = false;
void setup() {
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  pinMode(inPin1, INPUT);
  pinMode(inPin2, INPUT);
  pinMode(motor1, OUTPUT);
  pinMode(motor2, OUTPUT);
  Serial.begin(9600);
  
}

void loop() {

  if (analogRead(A2) > 600 && analogRead(A3) < 200) // epm high jetson 27-A2 22-A3
  {
    if (expand == false)
    {
      Serial.println("going down");
    digitalWrite(motor1, HIGH);
    digitalWrite(motor2, LOW);
    Serial.println("start");
    delay(1000);
    Serial.println("end");
    digitalWrite(motor1, LOW);
    expand = true;
    }
    myservo.writeMicroseconds(2000);
    delay(100);
  }
  else if (analogRead(A3) > 600 && analogRead(A2) < 200) // epm low
  {
    myservo.writeMicroseconds(1000);
    delay(100);
  }
  else
  {
    myservo.writeMicroseconds(1500); // epm neutral
    delay(100);
    delay(1000);
    if (expand == true)
    {
      Serial.println("going up");
    digitalWrite(motor1, LOW);
    digitalWrite(motor2, HIGH);
    Serial.println("start");
    delay(1000);
    Serial.println("end");
    digitalWrite(motor2, LOW);
    expand = false;
    }
    
  }
}
