# images

import matplotlib.pyplot as plt
import numpy as np
from imageio import imread
import seaborn as sns

m = 3
n = 5

M = np.random.randint(10, size=(m, n))
print(M)

plt.imshow(M)

for i in range(m):
    for j in range(n):
        plt.text(j, i, str(M[i, j]), fontsize=10, horizontalalignment='center', verticalalignment='center')

plt.colorbar()
plt.show()

img = imread(
    'https://scontent.fpfb7-1.fna.fbcdn.net/v/t39.30808-6/297192965_575940604212380_2796628958234673299_n.jpg?stp=dst-jpg_p600x600&_nc_cat=108&ccb=1-7&_nc_sid=dd5e9f&_nc_ohc=5i7agVNth5kAX-B7t4Q&_nc_ht=scontent.fpfb7-1.fna&oh=00_AfByTpnplGwyDqZmWofRoaMMv8bSt8wmceaD0G4-2qIfGA&oe=658DF6CD')

plt.imshow(img)
plt.title('Sakayanagi')
plt.show()

plt.hist(img.flatten(), bins=100)
plt.show()

plt.imshow(img, cmap='gray', vmin=150, vmax=200)
plt.xticks([])
plt.yticks([])
plt.show()

hilbertMatrix = np.zeros([10, 10])
for i in range(10):
    for j in range(10):
        hilbertMatrix[i, j] = 1 / (i + j + 1)

sns.heatmap(hilbertMatrix, vmax=.4)
plt.show()
