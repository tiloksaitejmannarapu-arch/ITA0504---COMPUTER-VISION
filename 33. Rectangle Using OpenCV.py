import numpy as np
import cv2

def create_rectangle_image(image_size):

    height, width = image_size

    # Create white image
    image = np.ones(
        (height, width, 3),
        dtype=np.uint8
    ) * 255

    # Rectangle coordinates
    top_left = (width // 4, height // 4)
    bottom_right = (
        3 * width // 4,
        3 * height // 4
    )

    # Draw rectangle
    cv2.rectangle(
        image,
        top_left,
        bottom_right,
        (255, 0, 0),
        2
    )

    # Display
    cv2.imshow("Rectangle Image", image)

    cv2.imwrite("rectangle.jpg", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


width = int(input("Enter image width: "))
height = int(input("Enter image height: "))

create_rectangle_image((height, width))
