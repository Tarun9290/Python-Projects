#Image processing tool
#Create a tool that can process and manipulate images.

import cv2

# Load an image
img = cv2.imread("image.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a Gaussian blur to the image
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply a threshold to the image
threshold = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)[1]

# Show the resulting image
cv2.imshow("Threshold", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
