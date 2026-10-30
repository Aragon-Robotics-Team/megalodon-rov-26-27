# testing 
import time
import serial

pwmVal = 1500
# connect to arduino
arduino = serial.Serial("COM12", 115200)  # open serial connection to arduino

while True:
    turnOnOff = input("Turn on (Y) or off (N) or quit (Q)?")
    if (turnOnOff.upper() == "Y"):
        pwmVal = 1900
        print("Servo turned on.")
    elif (turnOnOff.upper() == "N"):
        pwmVal = 1500
        print("Servo turned off.")
    elif (turnOnOff.upper() == "Q"):
        print("Quitting...")
        break
    else:
        print("Invalid input.")
        continue

    messageToSend = (str(pwmVal) + "-").encode("ascii")
    print("message to send: {}".format(messageToSend))
    arduino.write(messageToSend)  # send to arduino
    
    time.sleep(1)