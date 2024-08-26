import cv2
import numpy as np
from FaceDetection.face_detector import get_face_detector, find_faces, draw_faces
from FaceDetection.face_landmarks import get_landmark_model, detect_marks, draw_marks


def perform_face_detection(admission_number):
    # Load the face detection model
    face_model = get_face_detector()

    # Load the facial landmark model
    landmark_model = get_landmark_model()

    # Capture an image using the webcam
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    # Perform face detection on the captured image
    faces = find_faces(frame, face_model)

    # Draw rectangles around the detected faces
    draw_faces(frame, faces)

    # Find and draw facial landmarks for each detected face
    for face in faces:
        landmarks = detect_marks(frame, landmark_model, face)
        draw_marks(frame, landmarks)

    # Save the image with the admission number as the filename
    filename = f'data/{admission_number}.jpg'
    cv2.imwrite(filename, frame)

    # Display the image with the detected faces and landmarks
    cv2.imshow("Face Detection", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return filename
