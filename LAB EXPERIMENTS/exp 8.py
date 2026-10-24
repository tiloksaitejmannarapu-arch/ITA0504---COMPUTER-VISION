
import cv2
import numpy as np
import os

# Get the CV LAB folder
folder = os.path.dirname(os.path.abspath(__file__))

# Open the IMAGES folder
images_folder = os.path.join(folder, "IMAGES")

# Find an image automatically
image_files = [
    f for f in os.listdir(images_folder)
    if f.lower().endswith((".jpg", ".jpeg", ".png", ".bmp"))
]

if not image_files:
    print("No image found in the IMAGES folder!")

else:
    image_path = os.path.join(images_folder, image_files[0])
    image = cv2.imread(image_path)

    if image is None:
        print("Unable to read the image!")

    else:
        # Create a 5x5 kernel
        kernel = np.ones((5, 5), np.uint8)

        # Apply dilation
        dilated_image = cv2.dilate(
            image, kernel, iterations=1
        )

        # Display images
        cv2.imshow("Original Image", image)
        cv2.imshow("Dilated Image", dilated_image)

        # Save output in CV LAB folder
        output_path = os.path.join(
            folder, "dilated_image.jpg"
        )
        cv2.imwrite(output_path, dilated_image)

        print("Image used:", image_files[0])
        print("Dilation completed successfully!")
        print("Output saved as dilated_image.jpg")

        cv2.waitKey(0)
        cv2.destroyAllWindows()
