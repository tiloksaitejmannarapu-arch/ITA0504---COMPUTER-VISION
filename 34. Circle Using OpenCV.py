import numpy as np
import cv2

def create_circle_image(image_size):

    height, width = image_size

    # Create white image
    image = np.ones(
        (height, width, 3),
        dtype=np.uint8
    ) * 255

    # Circle center
    center = (
        width // 2,
        height // 2
    )

    # Circle radius
    radius = min(width, height) // 4

    # Draw circle
    cv2.circle(
        image,
        center,
        radius,
        (0, 0, 255),
        2
    )

    # Display
    cv2.imshow("Circle Image", image)

    cv2.imwrite("circle.jpg", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


width = int(input("Enter image width: "))
height = int(input("Enter image height: "))

create_circle_image((height, width))
