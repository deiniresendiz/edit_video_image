from PIL import Image

im = Image.open('image.jpg')
width = im.width //2

im = im.convert('L')
im = im.crop((0, 0, width, im.height))
im.show()
im.save('image-cropped.jpg')