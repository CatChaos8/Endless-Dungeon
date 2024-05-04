import serial
import pyautogui

# Connect to Arduino via serial port
ser = serial.Serial('COM3', 9600)  # Adjust COM port accordingly

while True:
    # Read data from Arduino
    data = ser.readline().decode().strip()
    
    # Simulate key press
    pyautogui.typewrite(data)
