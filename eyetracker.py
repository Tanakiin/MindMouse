# Importing necessary libraries
import cv2 as cv
import numpy as np
import pyautogui
from playsound import playsound
  
  
# Setting up the video capture source. 0 for webcam, add path to file for video detection
capture = cv.VideoCapture(0)

# Load the HAAR face and eye cascades
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier("haarcascade_eye.xml")

x = 0
face_x1, face_y1 = 0, 0

# Read 50 frames to initialize the face variables
while x < 50:
    ret1, frame1 = capture.read()
    gray = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY) # Convert to grayscale for processing
    faces1 = face_cascade.detectMultiScale(gray, 1.3, 5) # Detect faces in the frame
    
    # Store the center of the face detected
    face_y1 = 0
    for (x1, y1, w1, h1) in faces1:
        face_y1 = int(y1 + h1/2)
    x += 1

# Initialize the blink counter
count = 0

# Start processing frames
while True:
    ret, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    # Draw a rectangle around the face
    x, y, w, h = 0, 0, 0, 0
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.circle(frame, (x + int(w * 0.5), y + int(h * 0.5)), 4, (0, 255, 0), -1)
        face_y = int(y + h/2)

        # Check if the face has moved up or down and move the mouse accordingly
        if face_y > face_y1 + 10:
            pyautogui.moveRel(0, 20)
        elif face_y < face_y1 - 10:
            pyautogui.moveRel(0, -20)

    # Detect eyes in the face region
    eyes = eye_cascade.detectMultiScale(gray[y:(y + h), x:(x + w)], 1.1, 4)

    # Check if any eyes were detected
    temp_flag = np.any(eyes)
    if temp_flag == False:

        # If no eyes are detected for 10 consecutive frames, consider it a blink and simulate a mouse click
        if count >= 10:
            playsound('beep-01a.mp3')
            pyautogui.click()
            count = 0
        count += 1
    index = 0

    # Keep track of the eyes detected
    eye_1 = [None, None, None, None]
    eye_2 = [None, None, None, None]
    for (ex, ey, ew, eh) in eyes:
        if index == 0:
            eye_1 = [ex, ey, ew, eh]
        elif index == 1:
            eye_2 = [ex, ey, ew, eh]
        cv.rectangle(frame[y:(y + h), x:(x + w)], (ex, ey),
                     (ex + ew, ey + eh), (0, 0, 255), 2)
        index = index + 1
    
    # Detect the direction of the head tilt
    if (eye_1[0] is not None) and (eye_2[0] is not None):
        if eye_1[0] < eye_2[0]:
            left_eye = eye_1
            right_eye = eye_2
        else:
            left_eye = eye_2
            right_eye = eye_1
        left_eye_center = (
            int(left_eye[0] + (left_eye[2] / 2)), 
          int(left_eye[1] + (left_eye[3] / 2)))
          
        right_eye_center = (
            int(right_eye[0] + (right_eye[2] / 2)),
          int(right_eye[1] + (right_eye[3] / 2)))
          
        left_eye_x = left_eye_center[0]
        left_eye_y = left_eye_center[1]
        right_eye_x = right_eye_center[0]
        right_eye_y = right_eye_center[1]
  
        delta_x = right_eye_x - left_eye_x
        delta_y = right_eye_y - left_eye_y
          
        if delta_x == 0:
            delta_x = 0.00001
        angle = np.arctan(delta_y / delta_x)  
          
        # Converting radians to degrees
        angle = (angle * 180) / np.pi  
  
        # Provided a margin of error of 10 degrees
        # (i.e, if the face tilts more than 10 degrees
        # on either side the program will classify as right or left tilt)
        if angle > 10:
            cv.putText(frame, 'RIGHT TILT :' + str(int(angle))+' degrees',
                       (20, 30), cv.FONT_HERSHEY_SIMPLEX, 1,
                       (0, 0, 0), 2, cv.LINE_4)
            pyautogui.moveRel(-20, 0)
        elif angle < -10:
            cv.putText(frame, 'LEFT TILT :' + str(int(angle))+' degrees',
                       (20, 30), cv.FONT_HERSHEY_SIMPLEX, 1, 
                       (0, 0, 0), 2, cv.LINE_4)
            pyautogui.moveRel(20, 0)
        else:
            cv.putText(frame, 'STRAIGHT :', (20, 30),
                       cv.FONT_HERSHEY_SIMPLEX, 1, 
                       (0, 0, 0), 2, cv.LINE_4)

    cv.imshow('Frame', frame)
  
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
