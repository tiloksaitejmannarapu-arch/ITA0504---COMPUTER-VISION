import cv2

def detect_faces(image_path):

    # Load face cascade
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    # Read image
    image = cv2.imread(image_path)

    if image is None:
        print("Error: img.jpg not found.")
        return

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw rectangles
    for (x, y, w, h) in faces:
        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    print("Faces detected:", len(faces))

    # Display
    cv2.imshow("Face Detection", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


detect_faces("img.jpg")
