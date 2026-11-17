import cv2
from ultralytics import YOLO


# Load my amazing trained model from collab 
model = YOLO('CRAB_12FIN.pt')  


# Open  laptop webcam 
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(0, cv2.CAP_V4L2) 
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG")) #camera image format 

#to check if ur camera is opened or not / getting frames 

# print("Camera opened:", cap.isOpened())
# success, frame = cap.read() #(t/f, frame)
# print("Frame received:", success)


while cap.isOpened():
    success, frame = cap.read() 
    if not success:
        print("Ignoring empty camera frame.")
        break


    # Run YOLO inference on the frame
    results = model(frame)


    # draw results onto the frames 
    annotated_frame = results[0].plot() # .plot() is the boxes 


    # Display the annotated frame
    cv2.imshow("Ultralytics Webcam Inference", annotated_frame)


    # press q to quit 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()