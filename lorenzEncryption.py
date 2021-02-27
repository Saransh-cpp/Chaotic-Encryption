import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np
import lorenzSystem as key

path = str(input('Enter path of the image\n'))
image = img.imread(path)

plt.imshow(image)
plt.show()

height = image.shape[0]
width = image.shape[1]
print(width)

xkey, ykey, zkey = key.lorenz_key(0.01, 0.02, 0.03, height*width)
# print(xkey, ykey, zkey)

l = 0
x = []
y = []
xindex = []
yindex = []
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
        # print(zkey[l])
        zk = (int((zkey[l]*pow(10, 12))%256))
        # print(zk)
        # print(encryptedImage[i, j])
        encryptedImage[i, j] = encryptedImage[i, j]^zk
        # print(encryptedImage[i, j])
        l += 1
        # plt.imshow(encryptedImage)

plt.imshow(encryptedImage)
plt.show()