import cv2

# Load the image
img = cv2.imread('World.png')

# Define the regions to copy from and to
region_to_copy_from = img[0x005:0x082, 0x050:0x054, :]
region_to_copy_to = img[0x005:0x082, 0x078:0x07C, :]

# Perform the assignment
region_to_copy_to[:] = region_to_copy_from

# Save the modified image
cv2.imwrite('modified_xyz.png', img)

