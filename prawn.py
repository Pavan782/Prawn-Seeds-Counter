import cv2
import numpy as np

# Load the image
image = cv2.imread(r"C:\Users\PAVAN KALYAN\Documents\CV Projects\Prawnseeds counter\prawn2.jpeg")

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Apply adaptive thresholding
thresh = cv2.adaptiveThreshold(blurred_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

# Find contours in the binary image
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter contours based on area
min_area = 1  
max_area = 1000
filtered_contours = [cnt for cnt in contours if min_area < cv2.contourArea(cnt) < max_area]

# Draw contours on the original image
cv2.drawContours(image, filtered_contours, -1, (0, 255, 0), 2)

# Display the image with contours
cv2.imshow('Contours', image)

# Print the number of contours (assumed to be the number of prawn seeds)
print('Number of prawn seeds:', len(filtered_contours))

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
