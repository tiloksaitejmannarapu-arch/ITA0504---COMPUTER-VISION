import cv2
import numpy as np

image = cv2.imread("IMAGES/WhatsApp Image 2026-02-24 at 12.31.00 PM (3).jpeg")

if image is None:
    print("Image not found")
    exit()

image = cv2.resize(image, (800, 600))

kernel = np.ones((5, 5), np.uint8)

eroded_image = cv2.erode(image, kernel, iterations=1)

cv2.imshow("Original Image", image)
cv2.imshow("Eroded Image", eroded_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
