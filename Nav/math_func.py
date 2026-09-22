def PWM(joyVal): #converting a double to a PWM value
    Limit = 400 #with 400 the max is 1900 and the min is 1100 PWM
    joyVal = joyVal*Limit
    return joyVal

def makeString(Lx, Ly, Rx, A, B, C, D, throttle_y, throttle_x, pwm_limit=400, percent_horiz=100, percent_vert=100):
    #Lx-Double/float, Ly-Double/float, Rx-Double/float, A-Boolean, B-Boolean, "Sensitive Mode" - Boolean
    vtr = vtl = vbr = vbl = fr = fl = br = bl = 1500
    servo = 0
    sendStr = "" #constructed string to be sent to the arduino
    capMovement = 400 * (percent_horiz/100)
    capPivot = 400 * (percent_horiz/100)
    Vstrength = 400 * (percent_vert/100)

    # accounting for inverted axis
    Ly = Ly * (1)  
    Lx = Lx * (-1)
    Rx = Rx * (1)
    throttle_y = throttle_y * (-1)
    throttle_x = throttle_x * (-1)
    
    #deadband 0.1 deviation
    if(Lx < 0.1 and Lx > -0.1):
        Lx = 0
    if(Ly < 0.1 and Ly > -0.1):
        Ly = 0
    if(throttle_x < 0.1 and throttle_x > -0.1):
        throttle_x = 0
    if(throttle_y < 0.1 and throttle_y > -0.1):
        throttle_y = 0



    #LINEAR MODE
    # Front and Back Calculations
    br += PWM(Ly) * (capMovement/400) 
    bl += PWM(Ly) * (capMovement/400)
    fr += PWM(Ly) * (capMovement/400)
    fl += PWM(Ly) * (capMovement/400)
    

    #Crabbing Calculations 
    br += PWM(Lx)  * (capMovement/400)
    bl += -PWM(Lx) * (capMovement/400)
    fr += -PWM(Lx) * (capMovement/400)
    fl += PWM(Lx)  * (capMovement/400)
    

    #Pivoting CALCULATIONS 
    br += PWM(Rx) * (capPivot/400)
    bl += -PWM(Rx)  * (capPivot/400)
    fr += PWM(Rx) * (capPivot/400)
    fl += -PWM(Rx)  * (capPivot/400)

    # 1501 = PID ON
    vtr = vtl = vbr = vbl = 1501

    #up-down movement
    if(A): #if A is pressed
        vtr += Vstrength
        vtl += Vstrength * 0.9
        vbr += Vstrength
        vbl += Vstrength
        #v1 and v2 go up
    if(B): #if B is pressed
        vtr -= Vstrength
        vtl -= Vstrength * 0.9
        vbr -= Vstrength
        vbl -= Vstrength
        #v1 and v2 go down

    # pivot back and front
    vtr -= throttle_y * Vstrength
    vtl -= throttle_y * Vstrength
    vbr += throttle_y * Vstrength
    vbl += throttle_y * Vstrength

    # pivot right and left
    vtr -= throttle_x * Vstrength
    vtl += throttle_x * Vstrength
    vbr -= throttle_x * Vstrength
    vbl += throttle_x * Vstrength

    # servo claw
    servo += C - D



    #capping the pwm values at 1900/1100 and round
    pwmArray = [fr, fl, br, bl, vtr, vtl, vbr, vbl]
    for index in range(len(pwmArray)):
        # round to whole number
        pwmArray[index] = round(pwmArray[index])
        pwmArray[index] = max(1500-pwm_limit, pwmArray[index])
        pwmArray[index] = min(1500+pwm_limit, pwmArray[index])

    vtr = vtl = vbr = vbl = fr = fl = br = 1500

    #pwmArray[4] = pwmArray[4] 
    # sends the PWM values in the order:
    # fr, fl, br, bl, vtr, vtl, vbr, vbl, servo
    sendStr  = (str(pwmArray[0]) + "-" + 
                str(pwmArray[1]) + "=" + 
                str(pwmArray[2]) + "+" + 
                str(pwmArray[3]) + "*" + 
                str(pwmArray[4]) + "," + 
                str(pwmArray[5]) + "]" +
                str(pwmArray[6]) + "/" +
                str(pwmArray[7]) + "." +
                str(servo) + "!"
                )


    return sendStr
