import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

resolution = 0.05   # ganti sesuai nilai di file .yaml

img = mpimg.imread("lab_map_slow.pgm")
plt.imshow(img, cmap="gray")
plt.title("Klik 2 titik")
(p1, p2) = plt.ginput(2)
plt.close()

d_px = math.dist(p1, p2)
print(f"Jarak: {d_px:.1f} piksel = {d_px * resolution:.2f} m")
