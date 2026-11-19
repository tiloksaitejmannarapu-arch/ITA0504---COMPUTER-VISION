import cv2

def detect_vehicles(video_path):

    # Load vehicle cascade
    vehicle_cascade = cv2.CascadeClassifier("cars.xml")

    if vehicle_cascade.empty():
        print("Error: cars.xml not found.")
        return

    # Open video
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Cannot open video.")
        return

    while cap.isOpened():

        ret, frame = cap.read()

        if not ret:
            break

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect vehicles
        vehicles = vehicle_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(50, 50)
        )

        # Draw rectangles
        for (x, y, w, h) in vehicles:
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

        # Display
        cv2.imshow("Vehicle Detection", frame)

        # Press q to exit
        if cv2.waitKey(30) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


detect_vehicles("VID2.mp4")
