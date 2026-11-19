import cv2

def segment_image(image_path, threshold_value=127):

    # Read image
    image = cv2.imread(
        image_path,
        cv2.IMREAD_GRAYSCALE
    )

    if image is None:
        print("Error: img.jpg not found.")
        return

    # Apply threshold
    _, segmented_image = cv2.threshold(
        image,
        threshold_value,
        255,
        cv2.THRESH_BINARY
    )

    # Display
    cv2.imshow("Original Image", image)
    cv2.imshow("Segmented Image", segmented_image)

    # Save
    cv2.imwrite("segmented.jpg", segmented_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


segment_image("img.jpg", 127)
