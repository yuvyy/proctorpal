import cv2
import face_recognition

def start_face_tracking():
    # Initialize video capture (live video feed)
    cap = cv2.VideoCapture(0)

    # Initialize tracker for tracking the face
    tracker = cv2.TrackerCSRT_create()

    # Initialize variables for tracking face position
    bbox = None

    while True:
        ret, frame = cap.read()

        # If the face bounding box is not yet available, detect it in the first frame
        if bbox is None:
            face_locations = face_recognition.face_locations(frame)
            if face_locations:
                top, right, bottom, left = face_locations[0]
                bbox = (left, top, right - left, bottom - top)
                tracker.init(frame, bbox)

        # Update tracker and get new bounding box for the face
        else:
            success, bbox = tracker.update(frame)

            # If tracking is successful, draw rectangle around the face
            if success:
                (x, y, w, h) = [int(v) for v in bbox]
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            else:
                bbox = None

        # Display the current frame with face tracking
        cv2.imshow("Face Tracking", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()