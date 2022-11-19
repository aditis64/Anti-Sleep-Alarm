import face_recognition
import cv2
import numpy as np
import time
from espeak import espeak
import cv2
import RPi.GPIO as GPIO
from time import sleep
from gpiozero import Buzzer
import eye_game
in1 = 3
in2 = 4
en = 2
buzzer = Buzzer(23)
led = 21
GPIO.setup(led,GPIO.OUT)
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
7 | P a g e
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p=GPIO.PWM(en,1000)
p.start(100)
previous ="unkno"
count=0
video_capture = cv2.VideoCapture(0)
#frame = (video_capture, file)
file = 'image_data/image.jpg'
# Load a sample picture and learn how to recognize it.
cha_image = face_recognition.load_image_file("cha.jpg")
cha_face_encoding = face_recognition.face_encodings(cha_image)[0]
# Create arrays of known face encodings and their names
known_face_encodings = [
cha_face_encoding
]
known_face_names = [
"Charan Teja"
]
8 | P a g e
# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
temp_count = -1
GPIO.output(in1,GPIO.HIGH)
GPIO.output(in2,GPIO.LOW)
print("Engine running")
while(True):
# Grab a single frame of video
ret, frame = video_capture.read()
# Resize frame of video to 1/4 size for faster face recognition processing
small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
# Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
rgb_small_frame = small_frame[:, :, ::-1]
# Only process every other frame of video to save time
9 | P a g e
if process_this_frame:
# Find all the faces and face encodings in the current frame of video
face_locations = face_recognition.face_locations(rgb_small_frame)
face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
cv2.imwrite(file, small_frame)
face_names = []
for face_encoding in face_encodings:
# See if the face is a match for the known face(s)
matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
name = "Unknown"
# # If a match was found in known_face_encodings, just use the first one.
# if True in matches:
# first_match_index = matches.index(True)
# name = known_face_names[first_match_index]
# Or instead, use the known face with the smallest distance to the new face
face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
best_match_index = np.argmin(face_distances)
if matches[best_match_index]:
name = known_face_names[best_match_index]
direction= eye_game.get_eyeball_direction(file)
print(direction)
10 | P a g e
#eye_game.api.get_eyeball_direction(cv_image_array)
if previous != direction:
previous=direction
else:
print("old same")
count=1+count
print(count)
if (count>=30):
if(temp_count <= 15):
espeak.synth("Driver entering unconscious mode")
#led on
GPIO.output(led, GPIO.HIGH)
temp_count += 1
else:
# Buzzer.................
tt = 0
while(tt <= 8):
buzzer.beep()
tt += 1
buzzer.on()
sleep(10)
# Motor stop............
buzzer.off()
GPIO.output(in1, GPIO.LOW)
11 | P a g e
GPIO.output(in2, GPIO.LOW)
break
else:
espeak.synth(" ")
face_names.append(name)
process_this_frame = not process_this_frame
# Display the results
for (top, right, bottom, left), name in zip(face_locations, face_names):
# Scale back up face locations since the frame we detected in was scaled to 1/4 size
top *= 4
right *= 4
bottom *= 4
left *= 4
# Draw a box around the face
cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
# Draw a label with a name below the face
cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
12 | P a g e
font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
#cv2.putText(frame, frame_string, (left + 10, top - 10), font, 1.0, (255, 255, 255), 1)
# Display the resulting image
cv2.imshow('Video', frame)
# Hit 'q' on the keyboard to quit!
if cv2.waitKey(1) & 0xFF == ord('q'):
break
# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()