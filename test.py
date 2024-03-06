import cv2

# Load the image
image = cv2.imread('static/img/sample.jpg')

# Convert to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define range of red color in HSV
lower_red = (0, 100, 100)
upper_red = (10, 255, 255)

# Threshold the HSV image to get only red colors
mask = cv2.inRange(hsv_image, lower_red, upper_red)

# Count pixels
red_pixel_count = cv2.countNonZero(mask)
total_pixel_count = image.shape[0] * image.shape[1]

# Calculate percentage
red_percentage = (red_pixel_count / total_pixel_count) * 100

print("Percentage of red color in the image:", red_percentage)
