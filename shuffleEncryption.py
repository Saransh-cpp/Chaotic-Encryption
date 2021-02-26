import cv2
import numpy as np
import matplotlib.pyplot as plt

path = str(input('Enter path of the image\n'))
image = cv2.imread(path, 0)
plt.imshow(image)
plt.show()
height = image.shape[0]
width = image.shape[1]
encryptedImage = np.zeros(shape=[width, height], dtype=np.uint8)


def index_generator(x, r, n):

    index = []
    keys = []

    for i in range(n):
        x = r*x*(1-x)
        keys.append(x)
        index.append(i)

    for i in range(n):
        for j in range(n):
            if keys[i] > keys[j]:
                keys[i], keys[j] = keys[j], keys[i]
                index[i], index[j] = index[j], index[i]
    return index


def shuffle_image(image, index, x, y):
    for i in range(x):
        k = 0
        for j in range(y):
            encryptedImage[i][j] = image[i][index[k]]
            k += 1
        return encryptedImage


key = index_generator(0.1, 3.91, height)
encryptedImage = shuffle_image(image, key, width, height)

key = index_generator(0.01, 3.89, height)
encryptedImage = shuffle_image(encryptedImage, key, width, height)

plt.imshow(encryptedImage)
plt.plot()
