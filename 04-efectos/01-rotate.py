from PIL import Image, ImageDraw

img = Image.open('image.jpg')

#img = img.rotate(90)
img = img.rotate(90, expand=1)

img.save('image-rotate.jpg')