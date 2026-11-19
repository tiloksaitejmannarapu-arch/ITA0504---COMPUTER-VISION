import cv2
import pytesseract

# Tesseract OCR location
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_video(video_path):

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Cannot open VID2.mp4")
        return

    frame_count = 0

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        frame_count += 1

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Extract text using OCR
        text = pytesseract.image_to_string(gray)

        if text.strip():
            print("\nFrame:", frame_count)
            print(text)

    cap.release()
    cv2.destroyAllWindows()

    print("\nText extraction completed successfully.")


extract_text_from_video("VID2.mp4")
