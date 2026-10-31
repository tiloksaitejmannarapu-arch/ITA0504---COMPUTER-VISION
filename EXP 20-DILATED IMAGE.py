
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
            # Convert to grayscale
            gray = cv2.cvtColor(
                original, cv2.COLOR_BGR2GRAY
            )

            # Apply Sobel filter in X and Y directions
            sobel_x = cv2.Sobel(
                gray, cv2.CV_64F, 1, 0, ksize=3
            )
            sobel_y = cv2.Sobel(
                gray, cv2.CV_64F, 0, 1, ksize=3
            )

            # Convert gradients to 8-bit images
            sobel_x = cv2.convertScaleAbs(sobel_x)
            sobel_y = cv2.convertScaleAbs(sobel_y)

            # Combine X and Y gradients
            sobel_combined = cv2.addWeighted(
                sobel_x, 0.5, sobel_y, 0.5, 0
            )

            # Convert edge image to BGR for display
            sobel_color = cv2.cvtColor(
                sobel_combined, cv2.COLOR_GRAY2BGR
            )

            # Resize both images to the same height
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
            edge_display = resize_image(sobel_color)

            # Add labels
            cv2.putText(
                original_display, "Original Image",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (0, 255, 0), 2
            )

            cv2.putText(
                edge_display, "Sobel Edge Detection",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                0.65, (0, 255, 0), 2
            )

            # Original on left, filtered image on right
            combined = np.hstack((
                original_display, edge_display
            ))

            # Display output
            cv2.imshow(
                "Experiment 16 - Sobel Algorithm",
                combined
            )

            # Save output
            output_path = os.path.join(
                folder, "experiment16_output.jpg"
            )
            cv2.imwrite(output_path, combined)

            # Save individual Sobel results
            cv2.imwrite(
                os.path.join(folder, "sobel_x.jpg"),
                sobel_x
            )
            cv2.imwrite(
                os.path.join(folder, "sobel_y.jpg"),
                sobel_y
            )

            print("Image used:", image_files[0])
            print("Sobel edge detection completed!")
            print("Output saved as experiment16_output.jpg")

            cv2.waitKey(0)
            cv2.destroyAllWindows()
