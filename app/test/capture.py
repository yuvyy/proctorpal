import cv2

def capture_and_save_image(admission_no):
    # Open a connection to the webcam (usually camera index 0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Unable to access the webcam.")
        return None

    # Capture a single frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Unable to capture an image.")
        return None

    # Save the image to the file system
    image_filename = f"user_{admission_no}.jpg"
    cv2.imwrite(image_filename, frame)

    # Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()

    print(f"Image captured and saved as {image_filename}")

    return image_filename


