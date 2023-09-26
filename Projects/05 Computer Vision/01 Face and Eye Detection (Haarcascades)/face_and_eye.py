"""
Face and Eye detection in cv2 using Haarcascades

Source link : https://machinelearningprojects.net/face-and-eye-detection-in-cv2/
"""

import cv2

face_detector = cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml")
eye_detector = cv2.CascadeClassifier("data/haarcascade_eye.xml")

cam = cv2.VideoCapture(0)

ret = True

print("Select the frame and press ESC key to close...")

while ret:
    ret, frame = cam.read()

    if ret is True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_points = face_detector.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in face_points:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 20), 2)

            face = frame[y:y+h, x:x+w]
            eyes = eye_detector.detectMultiScale(face, 1.3,5)
            for (x, y, w, h) in eyes:
                cv2.rectangle(face, (x, y), (x+w, y+h), (155, 0, 120), 2)

        cv2.imshow("Live feed", frame)

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()
