from skimage import io
from skimage import color
from skimage.util import img_as_float
from skimage.segmentation import slic
from matplotlib import pyplot as plt
import os
image = img_as_float(io.imread(f'./datasets/X/seg_landscapes/seg_0.jpg'))
fig, ax = plt.subplots()
ax.tick_params(axis='both', length=0)
ax.set_xticklabels('')
ax.set_yticklabels('')
ax.imshow(image)