import pygame
from serial import Serial
import math_func
from time import sleep

FACTOR = 1.004288867 # depth sent by sensor to actual depth
OFFSET = 0.161498

# CHANGE PORT ACCORDINGLY
# /dev/cu.usbmodem21301 for Mac
arduino = Serial('COM13', 9600)

pygame.init()
pygame.joystick.init()
clock = pygame.time.Clock()

# message contains axis/button values
message = [] 
# [0] = LX
# [1] = LY
# [2] = LT
# [3] = RX
# [4] = RY
# [5] = RT
# [6] = A
# [7] = B
# [8] = X
# [9] = Y
# [10] = LB
# [11] = RB
# [12] = LJ
# [13] = RJ

loop = True

# this make code work instant
sleep(3)

# ---------- MAIN PROGRAM LOOP ---------- #

while loop:
    message = [] #clearing the contents of the list with each loop iteration
    
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quit")
            loop = False

    # Get count of interactables.
    joystick_count = pygame.joystick.get_count()

    # For each interactable:
    for index in range(joystick_count):
        joystick = pygame.joystick.Joystick(index)
        joystick.init()        

        # get joystick axis values
        axes = joystick.get_numaxes()
        for index in range(axes):
            axis = joystick.get_axis(index)
            message.append(joystick.get_axis(index))

        # get joystick button values
        buttons = joystick.get_numbuttons()
        for index in range(buttons):
            button = joystick.get_button(index)
            message.append(button)

        # taking the values list
        Lx = message[0]
        Ly = message[1]
        Rx = message[3]
        A = message[5]
        B = message[6]
        C = message[8]
        D = message[7]

        throttle_y = message[2]
        throttle_x = message[4]

        # construct string, send to arduino, received info back
        messageToSend = (math_func.makeString(Lx, Ly, Rx, A, B, C, D, throttle_y, throttle_x, 180)).encode("ascii")
        # messageToSend = b"1500-1500=1500+1500*1500,1500]1500/1500.0!\r\n"
        # print(messageToSend)
        arduino.write(messageToSend) 
        print(messageToSend)
        received = arduino.readline().decode("ascii")
        # PWMs, depth = received.split(";")
        print(received)
        # print(depth)
        # print((float(depth) * FACTOR) + OFFSET)

        # sleep(0.03)
            
# ---------- END MAIN PROGRAM LOOP ---------- #

# quit pygame after user exists
pygame.quit()

# ---------- ARDUINO CODE ---------- #

# //global variables for thruster pwms
# String br = "";
# String fl = "";
# String bl = "";
# String fr = "";
# String v1 = "";
# String v2 = "";

# void setup() {
# Serial.begin(9600); // set the baud rate
# delay(2000);
# Serial.println("Arduino is ready!");
# } 

# void loop() {

#   br = Serial.readStringUntil(',').toInt();
#   fl = Serial.readStringUntil(',').toInt();
#   bl = Serial.readStringUntil(',').toInt();
#   fr = Serial.readStringUntil(',').toInt();
#   v1 = Serial.readStringUntil(',').toInt();
#   v2 = Serial.readStringUntil(',').toInt();

#   Serial.println(br + ", " + fl + ", " + bl + ", " + fr + ", " + v1 + ", " + v2);

# }