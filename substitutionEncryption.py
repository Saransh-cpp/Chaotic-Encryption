import logisticKey as key   # Importing the key generating function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img

# Accepting an image
path = str(input('Enter the path of image\n'))
image = img.imread(path)

# Displaying the image
plt.imshow(image)
plt.show()

# Generating dimensions of the image
height = image.shape[0]
width = image.shape[1]
print(height, width)

# Generating keys
# Calling logistic_key and providing r value such that the keys are pseudo-random
# and generating a key for every pixel of the image
generatedKey = key.logistic_key(0.01, 3.95, height*width) 
print(generatedKey)

# Encryption using XOR
z = 0

# Initializing the encrypted image
encryptedImage = np.zeros(shape=[height, width, 3], dtype=np.uint8)

# Substituting all the pixels in original image with nested for
for i in range(height):
    for j in range(width):
        # USing the XOR operation between image pixels and keys
        encryptedImage[i, j] = image[i, j].astype(int) ^ generatedKey[z]
        z += 1

# Displaying the encrypted image
plt.imshow(encryptedImage)
plt.show()

# Decryption using XOR
z = 0

# Initializing the decrypted image
decryptedImage = np.zeros(shape=[height, width, 3], dtype=np.uint8)

# Substituting all the pixels in encrypted image with nested for
for i in range(height):
    for j in range(width):
        # USing the XOR operation between encrypted image pixels and keys
        decryptedImage[i, j] = encryptedImage[i, j].astype(int) ^ generatedKey[z]
        z += 1

# Displaying the decrypted image
plt.imshow(decryptedImage)
plt.show()
