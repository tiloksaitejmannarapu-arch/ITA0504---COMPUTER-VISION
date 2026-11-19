import cv2
import numpy as np

def subtract_foreground(image_path):

    # Read image
    image = cv2.imread(image_path)

    if image is None:
        print("Error: img.jpg not found.")
        return

    # Convert to HSV
    hsv = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2HSV
    )

    # Foreground color range
    lower_bound = np.array([0, 50, 50])
    upper_bound = np.array([120, 255, 255])

    # Create mask
    mask = cv2.inRange(
        hsv,
        lower_bound,
        upper_bound
    )

    # Extract foreground
    foreground = cv2.bitwise_and(
        image,
        image,
        mask=mask
    )

    # Display
    cv2.imshow("Original Image", image)
    cv2.imshow("Foreground", foreground)

    cv2.imwrite(
        "foreground.jpg",
        foreground
    )

    cv2.waitKey(0)
    cv2.destroyAllWindows()


subtract_foreground("img.jpg")
