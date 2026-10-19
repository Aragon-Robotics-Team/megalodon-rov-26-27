def Scale_PWM(joystick):
    return (joystick)*400
def mathfunct(ly, lx, rx, A, B):
    horizontal_frontleft = 1500
    horizontal_frontright = 1500
    horizontal_backleft = 1500
    horizontal_backright = 1500
    # Forward/Backward Movement
    horizontal_frontleft += Scale_PWM(ly)
    horizontal_frontright += Scale_PWM(ly)
    horizontal_backleft += Scale_PWM(ly)
    horizontal_backright += Scale_PWM(ly)

    horizontal_frontleft -= Scale_PWM(lx)
    horizontal_frontright -= Scale_PWM(lx)
    horizontal_backleft -= Scale_PWM(lx)
    horizontal_backright -= Scale_PWM(lx)

    horizontal_frontleft += Scale_PWM(rx)
    horizontal_frontright -= Scale_PWM(rx) 
    horizontal_backleft  += Scale_PWM(rx)
    horizontal_backright -= Scale_PWM(rx)

    vertical_frontleft = 1500
    vertical_frontright = 1500
    vertical_backleft = 1500
    vertical_backright = 1500

    if A==1:
        vertical_frontleft = 1900
        vertical_frontright = 1900
        vertical_backleft = 1900
        vertical_backright = 1900
    if B==1:
        vertical_frontleft = 1100
        vertical_frontright = 1100
        vertical_backleft = 1100
        vertical_backright = 1100

    #Joystick Movement
    if -0.1 <= ly <= 0.1:
        ly = 0
    if -0.1 <= lx <= 0.1:
        lx = 0
    if -0.1 <= rx <= 0.1:
        rx = 0
    if horizontal_frontleft > 1900:
        horizontal_frontleft = 1900
    if horizontal_frontright > 1900:
        horizontal_frontright = 1900
    if horizontal_backleft > 1900:
        horizontal_backleft = 1900
    if horizontal_backright > 1900:
        horizontal_backright = 1900
    if vertical_frontleft > 1900:
        vertical_frontleft = 1900
    if vertical_frontright > 1900:
        vertical_frontright = 1900
    if vertical_backleft > 1900:
        vertical_backleft = 1900
    if vertical_backright > 1900:
        vertical_backright = 1900
    if horizontal_frontleft < 1100:
        horizontal_frontleft = 1100
    if horizontal_frontright < 1100:
        horizontal_frontright = 1100
    if horizontal_backleft < 1100:
        horizontal_backleft = 1100
    if horizontal_backright < 1100:
        horizontal_backright = 1100
    if vertical_frontleft < 1100:
        vertical_frontleft = 1100
    if vertical_frontright < 1100:
        vertical_frontright = 1100
    if vertical_backleft < 1100:
        vertical_backleft = 1100
    if vertical_backright < 1100:
        vertical_backright = 1100
    print(horizontal_frontleft, horizontal_frontright, horizontal_backleft, horizontal_backright)
    print(vertical_frontleft, vertical_frontright, vertical_backleft, vertical_backright)
#mathfunct(0, 0, 1, 0, 0)





