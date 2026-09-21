import cv2
import math
import time
camera = cv2.VideoCapture(0)
width = round(int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))/2)
height = round(int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))/2)
pt = [(width-35,height),(width-20,height),(width-10,height+15),(width,height),(width+10,height+15),(width+20,height),(width+35,height)]
roll = 0
pitch = 0
depth = 0
a = -85
zoom = 24
print(height)
def endpoint(dist, roll1, pitch1):
    return (round(width + (dist * math.cos(roll1)) - (math.sin(roll1) * ((pitch1 + a) * zoom))),round(height + (math.cos(roll1) * ((pitch1 + a) * zoom)) + (dist * math.sin(roll1))))
while True:
    roll = 0
    pitch = 0
    depth = 0
    a = -85
    ret, frame = camera.read()
    cv2.line(frame, pt[0], pt[1], (0, 255, 0), 3, 1)
    cv2.line(frame, pt[1], pt[2], (0, 255, 0), 3, 1)
    cv2.line(frame, pt[2], pt[3], (0, 255, 0), 3, 1)
    cv2.line(frame, pt[3], pt[4], (0, 255, 0), 3, 1)
    cv2.line(frame, pt[4], pt[5], (0, 255, 0), 3, 1)
    cv2.line(frame, pt[5], pt[6], (0, 255, 0), 3, 1)
    cv2.putText(frame, "Depth >", (1550, 552), cv2.FONT_HERSHEY_DUPLEX, 1.2, (0, 255, 0), 2 )
    cv2.putText(frame, str(depth - (depth % 10) - 20), (1720, 552 - 100 - round(5*(depth % 10))), cv2.FONT_HERSHEY_DUPLEX, 1.2, (0, 255, 0), 2 )
    cv2.putText(frame, str(depth - (depth % 10) - 10), (1720, 552 - 50 - round(5*(depth % 10))), cv2.FONT_HERSHEY_DUPLEX, 1.2, (0, 255, 0), 2 )
    cv2.putText(frame, str(depth - (depth % 10)), (1720, 552 - round(5*(depth % 10))), cv2.FONT_HERSHEY_DUPLEX, 1.2, (0, 255, 0), 2 )
    cv2.putText(frame, str(depth - (depth % 10) + 10), (1720, 552 + 50 - round(5*(depth % 10))), cv2.FONT_HERSHEY_DUPLEX, 1.2, (0, 255, 0), 2 )
    cv2.putText(frame, str(depth - (depth % 10) + 20), (1720, 552 + 100 - round(5*(depth % 10))), cv2.FONT_HERSHEY_DUPLEX, 1.2, (0, 255, 0), 2 )
    cv2.putText(frame, str(depth - (depth % 10) + 30), (1720, 552 + 150 - round(5*(depth % 10))), cv2.FONT_HERSHEY_DUPLEX, 1.2, (0, 255, 0), 2 )
    cv2.rectangle(frame, (1710, 380), (1850, 400), (0, 255, 0), -1, 1)
    cv2.rectangle(frame, (1710, 380), (1850, 400), (0, 255, 0), 3, 1)
    cv2.rectangle(frame, (1710, 700), (1850, 680), (0, 255, 0), -1, 1)
    cv2.rectangle(frame, (1710, 700), (1850, 680), (0, 255, 0), 3, 1)
    cv2.line(frame, (1710, 380), (1710, 700), (0, 255, 0), 3, 1)
    cv2.line(frame, (1850, 380), (1850, 700), (0, 255, 0), 3, 1)
    while a < 85:
        if a == 0:
            start = endpoint(50, roll, pitch)
            end = endpoint(500, roll, pitch)
            cv2.line(frame, start, end, (0, 255, 0), 5, 1)
            start = endpoint(-50, roll, pitch)
            end = endpoint(-500, roll, pitch)
            cv2.line(frame, start, end, (0, 255, 0), 5, 1)
        else:
            start = endpoint(100, roll, pitch)
            end = endpoint(150, roll, pitch)
            cv2.line(frame, start, end, (0, 255, 0), 3, 1)
            start = endpoint(250, roll, pitch)
            end = endpoint(300, roll, pitch)
            cv2.line(frame, start, end, (0, 255, 0), 3, 1)
            start = endpoint(-100, roll, pitch)
            end = endpoint(-300, roll, pitch)
            cv2.line(frame, start, end, (0, 255, 0), 3, 1)
            b = str(-a)
            cv2.putText(frame, b, (round(width + (200 * math.cos(roll)) - (math.sin(roll) * ((pitch + a) * zoom))) - 30,round(height + (math.cos(roll) * ((pitch + a) * zoom)) + (200 * math.sin(roll))) + 10), cv2.FONT_HERSHEY_DUPLEX, 1.2, (0, 255, 0), 2)
        a += 5
    cv2.imshow("finalCamera", frame)
    if cv2.waitKey(1) == ord('c'):
        cv2.destroyAllWindows()
        break
camera.release()