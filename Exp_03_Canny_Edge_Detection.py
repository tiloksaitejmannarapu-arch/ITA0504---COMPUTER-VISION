import cv2

image = cv2.imread("IMAGES/WhatsApp Image 2026-02-24 at 12.31.00 PM (3).jpeg")

if image is None:
    print("Image not found")
    exit()

image = cv2.resize(image, (800, 600))

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray_image, 100, 200)

cv2.imshow("Original Image", image)
cv2.imshow("Canny Outline", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
