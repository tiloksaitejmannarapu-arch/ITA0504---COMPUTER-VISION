import cv2
import numpy as np

# Read the first image
image = cv2.imread(
    r"C:\Users\manna\OneDrive\Desktop\CV LAB\IMAGES\inspiration.webp"
)

# Check whether image is loaded
if image is None:
    print("Image not found!")
    exit()

# Convert image into grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create kernel
kernel = np.ones((5, 5), np.uint8)

# Perform Closing operation
closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Gray Image", gray)
cv2.imshow("Closing Operation", closing)

# Save output
cv2.imwrite("closing_output.jpg", closing)

# Wait and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
