
import cv2
import os
import numpy as np

# Get the CV LAB folder
folder = os.path.dirname(os.path.abspath(__file__))
images_folder = os.path.join(folder, "IMAGES")

# Check the IMAGES folder
if not os.path.isdir(images_folder):
    print("IMAGES folder not found!")

else:
    image_files = [
        f for f in os.listdir(images_folder)
        if f.lower().endswith((".jpg", ".jpeg", ".png", ".bmp"))
    ]

    if not image_files:
        print("No image found in the IMAGES folder!")

    else:
        # Read the input image
        image_path = os.path.join(images_folder, image_files[0])
        original = cv2.imread(image_path)

        if original is None:
            print("Unable to read the image!")

        else:
            # Rotate the image by 180 degrees
            rotated = cv2.rotate(original, cv2.ROTATE_180)

            # Resize images to the same display height
            height = 400

            def resize_height(img, target_height):
                width = int(img.shape[1] * target_height / img.shape[0])
                return cv2.resize(img, (width, target_height))

            original_display = resize_height(original, height)
            rotated_display = resize_height(rotated, height)

            # Add labels
            cv2.putText(
                original_display, "Original Image",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (0, 255, 0), 2
            )

            cv2.putText(
                rotated_display, "Rotated 180 Degrees",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (0, 255, 0), 2
            )

            # Original on left, rotated on right
            combined = np.hstack(
                (original_display, rotated_display)
            )

            # Display output
            cv2.imshow("Experiment 11 - Image Rotation", combined)

            # Save output
            output_path = os.path.join(
                folder, "experiment11_output.jpg"
            )
            cv2.imwrite(output_path, combined)

            print("Image used:", image_files[0])
            print("180-degree rotation completed successfully!")
            print("Output saved as experiment11_output.jpg")

            cv2.waitKey(0)
            cv2.destroyAllWindows()
