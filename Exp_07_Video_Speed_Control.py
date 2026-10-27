
import cv2
import os

# Input video path
video_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "cv lab video.mp4"
)

# Check whether the video exists and can be opened
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video file!")
    print("Check that cv lab video.mp4 is in the same folder.")
else:
    fps = cap.get(cv2.CAP_PROP_FPS)
    cap.release()

    if fps <= 0:
        fps = 30

    # Calculate delay for normal playback
    normal_delay = max(1, int(1000 / fps))

    def play_video(title, delay):
        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            print("Unable to open video.")
            return

        print("Playing:", title)

        while True:
            ret, frame = cap.read()

            if not ret:
                break

            cv2.imshow(title, frame)

            # Press q to stop playback
            if cv2.waitKey(delay) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    # 1. Normal motion
    play_video("Normal Motion", normal_delay)

    # 2. Slow motion
    play_video("Slow Motion", normal_delay * 2)

    # 3. Fast motion
    play_video("Fast Motion", max(1, normal_delay // 2))

    print("Experiment 7 completed successfully!")
