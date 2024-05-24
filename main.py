import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def histo(I, N):
    m = 0
    M = 255
    pas = (M - m) / N
    H = np.zeros(N)
    Nx, Ny = I.shape[:2]
    for n in range(N):
        nb = ((I.ravel() >= m + pas * n) & (I.ravel() < m + pas * (n + 1))).astype(int)
        if not np.all(nb == 0):
            H[n] = np.sum(nb)
    H = H / (Nx * Ny)
    h = H.copy()
    for i in range(1, N):
        h[i] = h[i-1] + H[i-1]
    return H, h

# Lecture et vectorisation de l'image
I = np.array(Image.open('lena.jpg'))

# Calcul des histogrammes
H, h = histo(I, 50)

# Visualisation et analyse
import matplotlib.pyplot as plt
plt.figure(1)
plt.imshow(I, cmap='gray')
plt.figure(2)
plt.bar(np.arange(len(h)), h)
plt.title('Histogramme cumulé')
plt.figure(3)
plt.bar(np.arange(len(H)), H)
plt.title('Histogramme d\'amplitude')
plt.show()

# Lecture et vectorisation de l'image
I = np.array(Image.open('cameraman.tif'))

# Calcul des histogrammes
H, h = histo(I, 50)

# Visualisation et analyse
plt.figure(1)
plt.imshow(I, cmap='gray')
plt.figure(2)
plt.bar(np.arange(len(h)), h)
plt.title('Histogramme d\'amplitude cumulé')
plt.figure(3)
plt.bar(np.arange(len(H)), H)
plt.title('Histogramme d\'amplitude normalisé')
plt.show()