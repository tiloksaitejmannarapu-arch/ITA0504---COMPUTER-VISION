
import cv2
import os
import numpy as np

# Get the CV LAB folder
folder = os.path.dirname(os.path.abspath(__file__))
images_folder = os.path.join(folder, "IMAGES")

# Find an image in the IMAGES folder
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
        image_path = os.path.join(images_folder, image_files[0])
        original = cv2.imread(image_path)

        if original is None:
            print("Unable to read the image!")

        else:
            # Rotate the image 90 degrees clockwise
            rotated = cv2.rotate(
                original, cv2.ROTATE_90_CLOCKWISE
            )

            # Resize both images for display
            height = 400

            def resize_height(image, target_height):
                width = int(
                    image.shape[1] * target_height / image.shape[0]
                )
                return cv2.resize(image, (width, target_height))

            original_display = resize_height(original, height)
            rotated_display = resize_height(rotated, height)

            # Add labels
            cv2.putText(
                original_display, "Original Image",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (0, 255, 0), 2
            )

            cv2.putText(
                rotated_display, "Rotated 90 Degrees Clockwise",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                0.65, (0, 255, 0), 2
            )

            # Original on the left, rotated on the right
            combined = np.hstack(
                (original_display, rotated_display)
            )

            # Display the result
            cv2.imshow("Experiment 10 - Image Rotation", combined)

            # Save the output
            output_path = os.path.join(
                folder, "experiment10_output.jpg"
            )
            cv2.imwrite(output_path, combined)

            print("Image used:", image_files[0])
            print("90-degree clockwise rotation completed!")
            print("Output saved as experiment10_output.jpg")

            cv2.waitKey(0)
            cv2.destroyAllWindows()
