// Pin assignments for buttons
const int buttonPins[] = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13};
const int numButtons = sizeof(buttonPins) / sizeof(buttonPins[0]);

// Pin assignments for potentiometers
const int potPins[] = {A0, A1, A2, A3, A4, A5};
const int numPots = sizeof(potPins) / sizeof(potPins[0]);

float analog_logic_tracker[6][2] = {};

 
// Array to store the button states
bool buttonStates[numButtons];

void setup() {
  // Initialize the serial communication
  Serial.begin(115200);

  // Set button pins as inputs and enable internal pull-up resistors
  for (int i = 0; i < numButtons; i++) {
    pinMode(buttonPins[i], INPUT_PULLUP);
  }
}

void loop() {
  // Read button states
  for (int i = 0; i < numButtons; i++) {
    buttonStates[i] = !digitalRead(buttonPins[i]);
  }

  // Read potentiometer values
  for (int i = 0; i < numPots; i++) {
    int potValue = analogRead(potPins[i]);
    analog_logic_tracker[i][0] = i;   
    analog_logic_tracker[i][1] = potValue; 

    switch (potPins[i]) {
      case A0:
        if (potValue == 0){
            Serial.println("Left Analog CLICKED");
          }
        break;
      case A1:
         if (potValue > 650) {
              // Code to handle the condition when the reading is greater than 650 on A5
              Serial.println("Left Analog DOWN ");
            }
             if(potValue < 100){
              Serial.println("Left Analog UP ");
            }
        break;
      case A2:
        if (potValue > 650) {
              // Code to handle the condition when the reading is greater than 650 on A5
              Serial.println("Left Analog RIGHT ");
            }
             if(potValue < 100){
              Serial.println("Left Analog LEFT ");
            }
        break;
      case A3:
        // Code for processing analog pin A3
        if (potValue > 650) {
          Serial.println("Right Analog DOWN ");
        }
        if(potValue < 100){
          Serial.println("Right Analog UP ");
        }
        break;
      case A4:
        if (potValue > 650) {
          // Code to handle the condition when the reading is greater than 650 on A5
          Serial.println("Right Analog RIGHT ");
        }
         if(potValue < 100){
          Serial.println("Right Analog LEFT ");
        }
        break;
        case A5:
          if (potValue == 0){
            Serial.println("Right Analog CLICKED");
          }

        break;
      default:
        // Handle any other cases (shouldn't be needed in this context)
        break;
    }
  }
      
  

  // Print button states
  for (int i = 0; i < numButtons; i++) {
    //Serial.print("Button ");
    //Serial.print(i);
    //Serial.print(": ");
    //Serial.println(buttonStates[i]);
  }

  // Delay to avoid reading too frequently
  delay(100);
}
