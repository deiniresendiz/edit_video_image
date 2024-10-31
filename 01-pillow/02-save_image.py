from PIL import Image

im = Image.open('image.jpg')
im = im.resize((555, 250))
im.save('image-resized.jpg')
im.show()