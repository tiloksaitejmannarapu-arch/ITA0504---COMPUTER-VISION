import cv2
import numpy as np

def subtract_background(image_path):

    # Read image
    image = cv2.imread(image_path)

    if image is None:
        print("Error: img.jpg not found.")
        return

    # Convert BGR to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Background color range
    lower_bound = np.array([30, 30, 30])
    upper_bound = np.array([255, 255, 255])

    # Create mask
    mask = cv2.inRange(
        hsv,
        lower_bound,
        upper_bound
    )

    # Invert mask
    mask_inv = cv2.bitwise_not(mask)

    # Extract foreground
    foreground = cv2.bitwise_and(
        image,
        image,
        mask=mask_inv
    )

    # Display
    cv2.imshow("Original Image", image)
    cv2.imshow("Background Subtracted", foreground)

    cv2.imwrite(
        "background_subtracted.jpg",
        foreground
    )

    cv2.waitKey(0)
    cv2.destroyAllWindows()


subtract_background("img.jpg")
