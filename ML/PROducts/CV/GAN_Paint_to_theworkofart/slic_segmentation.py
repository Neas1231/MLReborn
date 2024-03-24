from skimage import io
from skimage import color
from skimage.util import img_as_float
from skimage.segmentation import slic
from matplotlib import pyplot as plt
import os

numSegments = 20
for file in os.listdir('./datasets/landscapes'):
    try:
        image = img_as_float(io.imread(f'./datasets/landscapes/{file}'))
        segments = slic(image, n_segments=numSegments, sigma=5)
        image = color.label2rgb(segments, image, kind='avg')
        io.imsave(f'./datasets/seg_landscapes/seg_{file}',image)
    except:
        os.remove(f'./datasets/landscapes/{file}')
