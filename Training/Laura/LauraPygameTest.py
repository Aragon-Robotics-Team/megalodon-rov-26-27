import lauraTest
import pygame
import serial
from time import sleep

pygame.init()       # Initialize Pygame modules
pygame.joystick.init()  # Initialize joystick module, sets up joystick subsystem

# connect to arduino
arduino = serial.Serial("COM3", 9600)  # open serial connection to arduino

# main loop
loop = True
while loop:
    message = []        # new message list for each loop iteration

    for event in pygame.event.get():        # pygame.event.get() returns a list
                                            # of all events (quit, button pressed, etc)
        # stop looping if window is closed
        if event.type == pygame.QUIT:       # an event triggered when user closes window
            loop = False
        
    # detect number of JOYSTICKS connected
    joystickNum = pygame.joystick.get_count()
    print(joystickNum)

    # loop through every joystick
    for i in range(joystickNum):
        joystick = pygame.joystick.Joystick(i)  # create Joystick object
        joystick.init()  # initialize the joystick object so we can read its values
        print("Joystick name {}: {}".format(i, joystick.get_name()))

        # get AXIS values for joystick
        axes = joystick.get_numaxes()       # returns number of axes on joystick variable with each
                                            # with each axis corresponding to a stick or trigger
        for j in range(axes):       # print axis values
            message.append(joystick.get_axis(j))
            print("Axis {} value: {}".format(j, joystick.get_axis(j)))

        # get BUTTON values for joystick
        buttons = joystick.get_numbuttons()
        for j in range(buttons):    # print button values
            message.append(joystick.get_button(j))
            print("Button {} value: {}".format(j, joystick.get_button(j)))

    # gotten from testing with xbox controller
    Lx = message[0]
    print("Lx: {}".format(Lx))
    Ly = message[1]*-1
    print("Ly: {}".format(Ly))
    Rx = message[3]
    print("Rx: {}".format(Rx))
    A = message[6]  # orange button
    print("A: {}".format(A))
    B = message[7]  # button behind orange button
    print("B: {}".format(B))

    # convert to arduino format to prepare to send
    messageToSend = lauraTest.convertForArduino(Ly, 1, Lx, 0.5, Rx, A, B)
    messageToSend = messageToSend.encode("ascii")
    print("message to send: {}".format(messageToSend))
    arduino.write(messageToSend)  # send to arduino

    received = arduino.readline().decode("ascii")  # read a line from arduino
    print("Received from Arduino: {}".format(received))

    sleep(0.5)  # add delay to avoid spamming output

pygame.quit()  # stops pygame cleanly
arduino.close()  # close serial connection to arduino