from skimage import io, color, filters, measure
import matplotlib.pyplot as plt
import numpy as np
import os

# Load the image
image_path = './tennis3x3.jpg'
image = io.imread(image_path)

# If the image has an alpha channel, remove it
if image.shape[-1] == 4:
    image = image[:, :, :3]

# Convert to grayscale
gray_image = color.rgb2gray(image)

# Apply Sobel edge detection
edges = filters.sobel(gray_image)

# Find contours at a constant value of 0.2 (adjust this level if needed)
contours = measure.find_contours(edges, level=0.2)

# Path for the output file
output_file_path = "imgcoordinates.txt"

if contours:
    with open(output_file_path, 'w') as f:
        for contour in contours:
            # Reduce the coordinates scale by 3 times
            scaled_contour = contour / 3.0
            # Write the coordinates in (x,y) format
            for point in scaled_contour:
                f.write(f"({point[1]:.2f},{point[0]:.2f}),\n")

    print(f"Saved all contours to {output_file_path}")

    # Plot the image with contours
    fig, ax = plt.subplots()
    ax.imshow(image, cmap=plt.cm.gray)

    for contour in contours:
        scaled_contour = contour / 3.0
        ax.plot(scaled_contour[:, 1], scaled_contour[:, 0], linewidth=2)

    ax.set_title('Traced Contours')
    plt.show()
else:
    print("No contours found")
