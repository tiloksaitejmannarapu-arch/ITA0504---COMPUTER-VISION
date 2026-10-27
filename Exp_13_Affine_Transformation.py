
import cv2
import numpy as np
import os

# Get the CV LAB folder
folder = os.path.dirname(os.path.abspath(__file__))
images_folder = os.path.join(folder, "IMAGES")

if not os.path.isdir(images_folder):
    print("IMAGES folder not found!")

else:
    # Find an image
    image_files = [
        f for f in os.listdir(images_folder)
        if f.lower().endswith(
            (".jpg", ".jpeg", ".png", ".bmp")
        )
    ]

    if not image_files:
        print("No image found in the IMAGES folder!")

    else:
        # Read the input image
        image_path = os.path.join(
            images_folder, image_files[0]
        )
        original = cv2.imread(image_path)

        if original is None:
            print("Unable to read the image!")

        else:
            height, width = original.shape[:2]

            # Select three points from the original image
            pts1 = np.float32([
                [0, 0],
                [width - 1, 0],
                [0, height - 1]
            ])

            # Define their new positions
            pts2 = np.float32([
                [width * 0.1, height * 0.1],
                [width * 0.9, height * 0.2],
                [width * 0.2, height * 0.9]
            ])

            # Calculate affine transformation matrix
            matrix = cv2.getAffineTransform(pts1, pts2)

            # Apply affine transformation
            transformed = cv2.warpAffine(
                original, matrix, (width, height)
            )

            # Resize both images for side-by-side display
            display_height = 400

            def resize_image(img):
                h, w = img.shape[:2]
                new_width = int(w * display_height / h)
                return cv2.resize(
                    img, (new_width, display_height)
                )

            original_display = resize_image(original)
            transformed_display = resize_image(transformed)

            # Add labels
            cv2.putText(
                original_display, "Original Image",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (0, 255, 0), 2
            )

            cv2.putText(
                transformed_display, "Affine Transformed",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                0.65, (0, 255, 0), 2
            )

            # Original on left, transformed on right
            combined = np.hstack((
                original_display,
                transformed_display
            ))

            # Display result
            cv2.imshow(
                "Experiment 13 - Affine Transformation",
                combined
            )

            # Save output
            output_path = os.path.join(
                folder, "experiment13_output.jpg"
            )
            cv2.imwrite(output_path, combined)

            print("Image used:", image_files[0])
            print("Affine transformation completed!")
            print("Output saved as experiment13_output.jpg")

            cv2.waitKey(0)
            cv2.destroyAllWindows()
