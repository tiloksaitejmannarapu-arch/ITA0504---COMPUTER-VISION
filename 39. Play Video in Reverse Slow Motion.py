import cv2

def play_video_reverse_slow(video_path):

    # Open video
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Cannot open video.")
        return

    # Store frames
    frames = []

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        frames.append(frame)

    cap.release()

    # Play in reverse
    for frame in reversed(frames):

        cv2.imshow(
            "Reverse Slow Motion Video",
            frame
        )

        # 100 ms delay
        if cv2.waitKey(100) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()


play_video_reverse_slow("VID2.mp4")
