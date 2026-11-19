import numpy as np
import cv2

def add_text_to_image(image_size, text):

    height, width = image_size

    # Create white image
    image = np.ones(
        (height, width, 3),
        dtype=np.uint8
    ) * 255

    # Text properties
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    thickness = 2
    color = (0, 0, 255)

    # Get text size
    text_size = cv2.getTextSize(
        text,
        font,
        font_scale,
        thickness
    )[0]

    # Center text
    text_x = (width - text_size[0]) // 2
    text_y = (height + text_size[1]) // 2

    # Draw text
    cv2.putText(
        image,
        text,
        (text_x, text_y),
        font,
        font_scale,
        color,
        thickness
    )

    # Display
    cv2.imshow("Image with Text", image)

    cv2.imwrite("text_image.jpg", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


width = int(input("Enter image width: "))
height = int(input("Enter image height: "))
text = input("Enter the text to display: ")

add_text_to_image((height, width), text)
