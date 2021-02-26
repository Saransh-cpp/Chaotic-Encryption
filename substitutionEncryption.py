import logisticKey as key
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img

# Accepting an image
path = str(input('Enter the path of image\n'))
image = img.imread(path)

# Displaying the image
plt.imshow(image)
plt.show()

# Generating keys
height = image.shape[0]
width = image.shape[1]
print(height, width)

generatedKey = key.logistic_key(0.01, 3.95, height*width)
print(generatedKey)

# Encryption using XOR
z = 0

encryptedImage = np.zeros(shape=[height, width, 3], dtype=np.uint8)
for i in range(height):
    for j in range(width):
        # print(image[i, j])
        # break
        encryptedImage[i, j] = image[i, j].astype(int) ^ generatedKey[z]
        z += 1

plt.imshow(encryptedImage)
plt.show()

# Decryption
z = 0

decryptedImage = np.zeros(shape=[height, width, 3], dtype=np.uint8)
for i in range(height):
    for j in range(width):
        # print(image[i, j])
        # break
        decryptedImage[i, j] = encryptedImage[i, j].astype(int) ^ generatedKey[z]
        z += 1

plt.imshow(decryptedImage)
plt.show()
