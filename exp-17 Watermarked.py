import cv2

# Read the input image
image = cv2.imread("IMAGES/inspiration.webp")

# Check whether image is loaded
if image is None:
    print("Image not found!")
    exit()

# Get image dimensions
h, w = image.shape[:2]

# Select Region of Interest (ROI)
roi = image[h//4:h//2, w//4:w//2]

# Copy the selected region
copied_roi = roi.copy()

# Create a copy of original image
output = image.copy()

# Paste ROI at the bottom-right corner
rh, rw = copied_roi.shape[:2]
output[h-rh:h, w-rw:w] = copied_roi

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Cropped Image", copied_roi)
cv2.imshow("Image After Copying and Pasting", output)

# Save output image
cv2.imwrite("roi_output.jpg", output)

# Wait and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
