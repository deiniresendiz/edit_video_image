from PIL import Image

im = Image.open('image.jpg')
im.resize((555, 250)).show()