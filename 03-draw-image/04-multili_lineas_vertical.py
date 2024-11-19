from PIL import Image, ImageDraw

img = Image.open('image.jpg')

blue = (0, 0, 255)

img1 = ImageDraw.Draw(img)

for i in range(0, img.size[0], 10):
    position = (i, 0, i, img.size[1])
    img1.line(position, blue, 1)

img.save('image-multili_lineas_vertical.jpg')