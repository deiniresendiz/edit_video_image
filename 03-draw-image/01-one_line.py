from PIL import Image, ImageDraw

img = Image.open('image.jpg')
position = (0, 0, img.size[0], img.size[1])

red = (255, 0, 0)

img1 = ImageDraw.Draw(img)
img1.line(position, fill=red, width=50)
img.save('image-line.jpg')