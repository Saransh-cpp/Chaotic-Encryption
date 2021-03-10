"""
Encrypting an image through substitution algorithm 
using pseudo-random numbers generated from
Lorenz system of differential equations
"""

# Importing all the necessary libraries
import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np
import lorenzSystem as key

# Accepting Image using it's path
path = str(input('Enter path of the image\n'))
image = img.imread(path)

# Displaying original image
plt.imshow(image)
plt.show()

# Storing the size of image in variables
height = image.shape[0]
width = image.shape[1]

# Using lorenz_key function to generate a key for every pixel
x, y, keys = key.lorenz_key(0.01, 0.02, 0.03, height*width)

l = 0

# Initializing an empty image to store the encrypted image
encryptedImage = np.zeros(shape=[height, width, 3], dtype=np.uint8)

# XORing each pixel with a pseudo-random number generated above/ Performing the 
# substitution algorithm
for i in range(height):
    for j in range(width):
        # Converting the pseudo-random nuber generated into a number between 0 and 255
        zk = (int((keys[l]*pow(10, 5))%256))
        # Performing the XOR operation
        encryptedImage[i, j] = image[i, j]^zk
        l += 1

# Displaying the encrypted image
plt.imshow(encryptedImage)
plt.show()

# Initializing an empty image to store the decrypted image
decryptedImage = np.zeros(shape=[height, width, 3], dtype=np.uint8)

# XORing each pixel with the same number it was XORed above above/
# Performing the reverse substitution algorithm
l = 0
for i in range(height):
    for j in range(width):
        zk = (int((keys[l]*pow(10, 5))%256))
        decryptedImage[i, j] = encryptedImage[i, j]^zk
        l += 1

# Displaying the decrypted image
plt.imshow(decryptedImage)
plt.show()