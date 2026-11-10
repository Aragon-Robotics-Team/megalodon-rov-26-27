import cv2
import numpy as np
import time
import math

def hypo(a:list,b:list):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

# -----------------------------
# Configuration
# -----------------------------
video = ""           # Video file path, or "" for webcam
camId = 0
markerLength = 0.05   # Marker side length in meters
width = 0
height = 0

showRejected = False

# Camera calibration (replace with your actual calibration values)
camMatrix = np.array([
    [800, 0, 320],
    [0, 800, 240],
    [0, 0, 1]
], dtype=np.float64)

distCoeffs = np.zeros((5, 1), dtype=np.float64)

# -----------------------------
# ArUco detector
# -----------------------------
dictionary = cv2.aruco.getPredefinedDictionary(
    cv2.aruco.DICT_6X6_250
)

detectorParams = cv2.aruco.DetectorParameters()

detector = cv2.aruco.ArucoDetector(
    dictionary, detectorParams
)

# -----------------------------
# Video input
# -----------------------------
if video:
    inputVideo = cv2.VideoCapture(video)
    waitTime = 0
else:
    inputVideo = cv2.VideoCapture(camId)
    waitTime = 10

width = inputVideo.get(cv2.CAP_PROP_FRAME_WIDTH)
height = inputVideo.get(cv2.CAP_PROP_FRAME_HEIGHT)

if not inputVideo.isOpened():
    raise RuntimeError("Could not open video source")

totalTime = 0
totalIterations = 0

# -----------------------------
# Marker coordinate system
# -----------------------------
objPoints = np.array([
    [-markerLength / 2,  markerLength / 2, 0],
    [ markerLength / 2,  markerLength / 2, 0],
    [ markerLength / 2, -markerLength / 2, 0],
    [-markerLength / 2, -markerLength / 2, 0]
], dtype=np.float32)

# -----------------------------
# Main loop
# -----------------------------
while inputVideo.grab():

    ret, image = inputVideo.retrieve()

    if not ret:
        break

    imageCopy = image.copy()

    tick = time.perf_counter()

    # Detect markers
    corners, ids, rejected = detector.detectMarkers(image)

    nMarkers = len(corners)

    # -----------------------------
    # Detection timing
    # -----------------------------
    currentTime = time.perf_counter() - tick

    totalTime += currentTime
    totalIterations += 1

    if totalIterations % 30 == 0:
        roll = 0
        yaw = 0
        centre = [0,0]
        print("Translate up, Yaw right, Translate right, Translate forward")
        if len(corners) > 0: 
            roll = math.degrees(math.atan2((int(corners[0][0][0][1])-int(corners[0][0][1][1])),-(int(corners[0][0][0][0])-int(corners[0][0][1][0]))))
            yaw = math.degrees(math.acos(min(1,(hypo(corners[0][0][0],corners[0][0][1])/hypo(corners[0][0][0],corners[0][0][3])))))
            if hypo(corners[0][0][0],corners[0][0][3]) > hypo(corners[0][0][1],corners[0][0][2]): yaw *= -1
            centre = [float((corners[0][0][0][0] + corners[0][0][2][0])/2),float((corners[0][0][0][1] + corners[0][0][2][1])/2)]
            print((-2*centre[1]/height)+1)
            print((2*centre[0]/width)-1)
            print(-yaw/90) 
            print(min(1,max(-1,(hypo(corners[0][0][0],corners[0][0][2])-330)/-500)))
    # -----------------------------
    # Draw detected markers
    # -----------------------------
    if ids is not None and len(ids) > 0:

        cv2.aruco.drawDetectedMarkers(
            imageCopy, corners, ids
        )
        math

    # -----------------------------
    # Draw rejected candidates
    # -----------------------------
    if showRejected and len(rejected) > 0:

        cv2.aruco.drawDetectedMarkers(
            imageCopy,
            rejected,
            np.array([], dtype=np.int32),
            borderColor=(100, 0, 255)
        )

    # -----------------------------
    # Display output
    # -----------------------------
    cv2.imshow("out", imageCopy)

    if cv2.waitKey(1) == ord('c'):  # ESC
        break

# -----------------------------
# Cleanup
# -----------------------------
inputVideo.release()
cv2.destroyAllWindows()