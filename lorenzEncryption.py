# Importing all the required libraries
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

# Using lorenz_key function to generate 3 lists of keys
xkey, ykey, zkey = key.lorenz_key(0.01, 0.02, 0.03, height*width)

l = 0
x = []
y = []
xindex = []
yindex = []

# Initializing an empty image to store the encrypted image
encryptedImage = np.zeros(shape=[height, width, 3], dtype=np.uint8)
l = 0

for i in range(width):
    xindex.append(i)

for i in range(height):
    yindex.append(i)

for i in range(width):
    for j in range(width):
        if xkey[i] > xkey[j]:
            xkey[i], xkey[j] = xkey[j], xkey[i]
            xindex[i], xindex[j] = xindex[j], xindex[i]

for i in range(height):
    for j in range(height):
        if ykey[i] > ykey[j]:
            ykey[i], ykey[j] = ykey[j], ykey[i]
            yindex[i], yindex[j] = yindex[j], yindex[i]

for i in range(height):
    k = 0
    for j in range(width):
        encryptedImage[i][j] = image[yindex[k]][j] 
        k += 1

for i in range(height):
    k = 0
    for j in range(width):
        encryptedImage[i][j] = encryptedImage[i][xindex[k]]
        k += 1

plt.imshow(encryptedImage)
plt.show()

l = 0
for i in range(height):
    for j in range(width):
        zk = (int((zkey[l]*pow(10, 5))%256))
        encryptedImage[i, j] = encryptedImage[i, j]^zk
        l += 1

plt.imshow(encryptedImage)
plt.show()




# decryptedImage = np.zeros(shape=[height, width, 3], dtype=np.uint8)

# l = 0
# for i in range(height):
#     for j in range(width):
#         zk = (int((zkey[l]*pow(10, 5))%256))
#         decryptedImage[i, j] = encryptedImage[i, j]^zk
#         l += 1

# print(decryptedImage[0][0])

# plt.imshow(decryptedImage)
# plt.show()


# for i in range(height):
#     k = 0
#     for j in range(width):
#         encryptedImage[i][xindex[k]] = encryptedImage[i][j]
#         k += 1

# print(image[70][0])
# print(encryptedImage[0][0])


# for i in range(height):
#     k = 0
#     for j in range(width):
#         decryptedImage[yindex[k]][j] = encryptedImage[i][j]
#         k += 1

# print(image[70][0])
# print(encryptedImage[0][0])


# plt.imshow(decryptedImage)
# plt.show()
