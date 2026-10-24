
import cv2
import os
import numpy as np

# Get folder paths
folder = os.path.dirname(os.path.abspath(__file__))
images_folder = os.path.join(folder, "IMAGES")

# Find an image
image_files = [
    f for f in os.listdir(images_folder)
    if f.lower().endswith((".jpg", ".jpeg", ".png", ".bmp"))
]

if not image_files:
    print("No image found in IMAGES folder!")

else:
    image_path = os.path.join(images_folder, image_files[0])
    original = cv2.imread(image_path)

    if original is None:
        print("Unable to read image!")

    else:
        # Resize image to double size
        updated = cv2.resize(
            original, None,
            fx=2, fy=2,
            interpolation=cv2.INTER_LINEAR
        )

        # Make both images the same display height
        height = 400
        original_display = cv2.resize(
            original,
            (int(original.shape[1] * height / original.shape[0]), height)
        )
        updated_display = cv2.resize(
            updated,
            (int(updated.shape[1] * height / updated.shape[0]), height)
        )

        # Add labels
        cv2.putText(
            original_display, "Original Image",
            (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
            0.8, (0, 255, 0), 2
        )
        cv2.putText(
            updated_display, "Resized Image",
            (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
            0.8, (0, 255, 0), 2
        )

        # Place original left and updated right
        combined = np.hstack((original_display, updated_display))

        cv2.imshow("Experiment 9 - Image Scaling", combined)

        # Save combined output
        output_path = os.path.join(folder, "experiment9_output.jpg")
        cv2.imwrite(output_path, combined)

        print("Original image: LEFT")
        print("Resized image: RIGHT")
        print("Output saved as experiment9_output.jpg")

        cv2.waitKey(0)
        cv2.destroyAllWindows()
