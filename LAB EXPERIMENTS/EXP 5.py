import cv2
import matplotlib.pyplot as plt

def analyze_histogram(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("Image not found")
        return

    image = cv2.resize(image, (800, 600))

    color_channels = ('b', 'g', 'r')

    plt.figure(figsize=(10, 5))

    for i, color in enumerate(color_channels):
        histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(histogram, color=color, label=f"{color.upper()} Channel")

    plt.xlim([0, 256])
    plt.title("Color Histogram Analysis")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()

analyze_histogram("IMAGES/WhatsApp Image 2026-02-24 at 12.31.00 PM (3).jpeg")
