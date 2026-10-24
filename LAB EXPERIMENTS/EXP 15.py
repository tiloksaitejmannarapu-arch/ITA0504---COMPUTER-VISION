
import cv2
import numpy as np
import os

# Get the CV LAB folder
folder = os.path.dirname(os.path.abspath(__file__))
images_folder = os.path.join(folder, "IMAGES")

if not os.path.isdir(images_folder):
    print("IMAGES folder not found!")

else:
    # Find an image in the IMAGES folder
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
            # Convert image to grayscale
            gray = cv2.cvtColor(
                original, cv2.COLOR_BGR2GRAY
            )

            # Convert to float32
            gray_float = np.float32(gray)

            # Apply Harris Corner Detection
            corners = cv2.cornerHarris(
                gray_float,
                blockSize=2,
                ksize=3,
                k=0.04
            )

            # Dilate corners to make them visible
            corners = cv2.dilate(corners, None)

            # Copy original image for marking corners
            detected = original.copy()

            # Mark detected corners in red
            threshold = 0.01 * corners.max()
            detected[corners > threshold] = [0, 0, 255]

            # Resize images for side-by-side display
            display_height = 400

            def resize_image(img):
                h, w = img.shape[:2]
                new_width = int(
                    w * display_height / h
                )
                return cv2.resize(
                    img, (new_width, display_height)
                )

            original_display = resize_image(original)
            detected_display = resize_image(detected)

            # Add labels
            cv2.putText(
                original_display,
                "Original Image",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (0, 255, 0), 2
            )

            cv2.putText(
                detected_display,
                "Harris Corners",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (0, 255, 0), 2
            )

            # Original left, detected corners right
            combined = np.hstack((
                original_display,
                detected_display
            ))

            # Display output
            cv2.imshow(
                "Experiment 15 - Harris Corner Detection",
                combined
            )

            # Save output
            output_path = os.path.join(
                folder, "experiment15_output.jpg"
            )
            cv2.imwrite(output_path, combined)

            print("Image used:", image_files[0])
            print("Harris corner detection completed!")
            print("Output saved as experiment15_output.jpg")

            cv2.waitKey(0)
            cv2.destroyAllWindows()
