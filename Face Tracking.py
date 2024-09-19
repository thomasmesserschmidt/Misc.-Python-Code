# pip install cmake
# pip install dlib
import sys
import dlib
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import imutils
import numpy as np
from operator import itemgetter
import math
import dnn

dnn.FaceDetector.set_param("resolution", dnn.RESOLUTION.HIGH)
detectum = dnn.FaceDetector()
THRESHOLD = 0.6 # Value between 0 and 1 for confidence score

# initialize the camera and grab a reference to the raw camera capture
RES_W = 256 # 1280 # 640 # 256 # 320 # 480 # pixels
RES_H = 144 # 720 # 480 # 144 # 240 # 360 # pixels

camera = PiCamera()
camera.resolution = (RES_W, RES_H)
camera.framerate = 30 # FPS
rawCapture = PiRGBArray(camera, size=(RES_W, RES_H))

# allow the camera to warmup
time.sleep(0.1)

frame_count = 0

trackers = []

# loop over frames from the video stream
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    image_cpy = np.copy(image) # Create copy since cant modify orig

    if image_cpy is None:
        break

    if frame_count == 0:
        _, bboxes = detectum.process_frame(image_cpy, THRESHOLD)

        # Loop through list (if empty this will be skipped) and overlay green bboxes
        for i in bboxes:
            cv2.rectangle(image_cpy, (i[0], i[1]), (i[2], i[3]), (0, 255, 0), 3)
            (startX, startY, endX, endY) = (i[0], i[1], i[2], i[3])

            # We need to initialize the tracker on the first frame
            # Create the correlation tracker - the object needs to be initialized
            # before it can be used
            tracker = dlib.correlation_tracker()

            # Start a track on face detected on first frame.
            rect = dlib.rectangle(i[0], i[1], i[2], i[3])
            tracker.start_track(image_cpy, rect)

            # add the tracker to our list of trackers so we can
            # utilize it during skip frames
            trackers.append(tracker)

    else:
        # Else we just attempt to track from the previous frame
        # track all the detected faces
        for tracker in trackers:
            tracker.update(image_cpy)
            pos = tracker.get_position()

            # unpack the position object
            startX = int(pos.left())
            startY = int(pos.top())
            endX = int(pos.right())
            endY = int(pos.bottom())

            # draw bounding box
            cv2.rectangle(image_cpy, (startX, startY), (endX, endY), (0, 255, 0), 3)

    frame_count += 1

    cv2.imshow('frame',image_cpy)
    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break  
