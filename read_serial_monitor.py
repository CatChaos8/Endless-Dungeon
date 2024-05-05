import serial
import pyautogui

# Connect to Arduino
ser = serial.Serial('COM3', 9600)  

while True:
    # Read data from Serial Monitor
    data = ser.readline().decode().strip()
    
    # Press Key
    pyautogui.typewrite(data)
