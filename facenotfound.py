import cv2
import face_recognition



def liveVerification(face_locations, face_encodings, frame, path):

    checker = 0
    # Load the known face image (registered student)
    known_image = face_recognition.load_image_file(path)
    known_face_encoding = face_recognition.face_encodings(known_image)[0]

    while True:

        for face_encoding in face_encodings:
            # Compare the current face encoding with the known student's face encoding
            matches = face_recognition.compare_faces([known_face_encoding], face_encoding)
            name = "Unknown"  # Default: Unknown person
            checker -= 5

            if matches[0]:
                name = "Registered Student"  # Matched with the registered student
                checker += 50

            # Draw a rectangle around the face and display the name
            top, right, bottom, left = face_locations[0]
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

            # Display the current frame with identity verification
        cv2.imshow("Identity Verification", frame)

        print(checker)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if checker >= 2000:
            break

        if checker <= -2000:
            
            break
    
    if checker >= 2000:
        return True
    else:
        return False
        

def facenotfound():


    # Initialize video capture (live video feed)
    cap = cv2.VideoCapture(0)
    
    face_found = False

    notFoundCouter = 0

    while True:
        ret, frame = cap.read()

        # Find face locations and face encodings in the current frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        if not face_locations:

            if not face_found:
                print("Warning: No face found in the frame!")
                notFoundCouter += 1
                face_found = False
        else:
            # Face is found, call the verification function
            if liveVerification(face_locations, face_encodings,frame,"data/2021PE6421.jpg") == False:
                print("Stop cheating")
            else:
                print("Welcome back")
                        
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


    # Release the video capture and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
