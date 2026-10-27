import cv2

image = cv2.imread("IMAGES/WhatsApp Image 2026-02-24 at 12.31.00 PM (3).jpeg")

blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

cv2.imshow("Original Image", image)
cv2.imshow("Gaussian Blurred Image", blurred_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
