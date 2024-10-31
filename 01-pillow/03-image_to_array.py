from PIL import Image
import numpy as np

# im = Image.open('image.jpg')
# a = np.asarray(im)


width = 500
height = 400

array = np.zeros((height, width, 3), dtype=np.uint8)
im = Image.fromarray(array)
im.show()