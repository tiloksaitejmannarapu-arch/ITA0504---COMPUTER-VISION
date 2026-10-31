import cv2
import numpy as np

# Read the input image
image = cv2.imread("IMAGES/inspiration.webp")

# Check whether image is loaded
if image is None:
    print("Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create a kernel
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
erosion = cv2.erode(gray, kernel, iterations=1)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Erosion Image", erosion)

# Save the output
cv2.imwrite("erosion_output.jpg", erosion)

# Wait and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
