import cv2

watch_cascade = cv2.CascadeClassifier(
    r"C:\Users\manna\OneDrive\Desktop\CV LAB\watch_cascade.xml"
)

if watch_cascade.empty():
    print("Watch cascade XML file not found!")
    exit()

image = cv2.imread(
    r"C:\Users\manna\OneDrive\Desktop\CV LAB\IMAGES\rishab.jpg"
)

if image is None:
    print("Image not found!")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

watches = watch_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

for (x, y, w, h) in watches:
    cv2.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

if len(watches) > 0:
    print("Watch detected!")
else:
    print("No watch detected!")

cv2.imshow("Detected Watch", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
