import cv2

# Load the pre-trained Haar cascade for watch detection
watch_cascade = cv2.CascadeClassifier(
    r"C:\Users\manna\OneDrive\Desktop\CV LAB\watch_cascade.xml"
)

# Check whether cascade file is loaded
if watch_cascade.empty():
    print("Watch cascade XML file not found!")
    exit()

# Read the input image
image = cv2.imread(
    r"C:\Users\manna\OneDrive\Desktop\CV LAB\IMAGES\watch.jpg"
)

# Check whether image is loaded
if image is None:
    print("Image not found!")
    exit()

# Convert image into grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect watch in the image
watches = watch_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Draw bounding boxes around detected watches
for (x, y, w, h) in watches:
    cv2.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

# Display detected watch
if len(watches) > 0:
    print("Watch detected!")
else:
    print("No watch detected!")

cv2.imshow("Detected Watch", image)

# Wait and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
