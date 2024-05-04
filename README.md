This is a roguelike game where you kill things. To attack you have to answer a question correctly. At the end of every battle you get an item that upgrades your stats(Attack, DoT, HP, Heal Amount, & more!)
Requirements: Pygame!

Joystick: https://www.tinkercad.com/things/6ztUTHf9cy5-daring-rottis/editel











Arduino code: 

#include <Key.h>;
#include <Keypad.h>;

int buzzer = 13;
int buzzer_value = 1;

const byte ROWS = 4;
const byte COLS = 4;
const byte PassLength = 4;
char currentPassword[PassLength] = {'0', '0', '0', '0'};

char buttons[ROWS][COLS] = {
  {'1','W','0','1'},
  {'A',' ','D','2'},
  {'7','S','0','3'},
  {'*','0','#','4'},
};

byte rowPins[ROWS] = {5, 4, 3, 2};
byte colPins[COLS] = {6, 7, 8, 12};

Keypad keypad = Keypad(makeKeymap(buttons), rowPins, colPins, ROWS, COLS);

void setup() {

 Serial.begin(9600); 
  
}

void loop() {

char key = keypad.getKey();
  
  if (key == '*'){
  Serial.println('*');
    if (buzzer_value == 0){
      buzzer_value = 1;}
    else{
      buzzer_value = 0;}
   
      }
 
    else if (key != NO_KEY) {
    Serial.println(key);
      if (buzzer_value == 1){
              tone(buzzer, 450);
        delay(100);
        noTone(buzzer);
}

  
}
  delay(100);
}
