import cv2

image = cv2.imread("IMAGES/WhatsApp Image 2026-02-24 at 12.31.00 PM (3).jpeg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
