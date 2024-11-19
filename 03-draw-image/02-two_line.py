from PIL import Image, ImageDraw

img = Image.open('image.jpg')
position = (0, 0, img.size[0], img.size[1])

red = (255, 0, 0)
green = (0, 255, 0)

img1 = ImageDraw.Draw(img)
img1.line(position, fill=red, width=50)

position_2 = ( img.size[0], 0 , 0, img.size[1])
img1.line(position_2, fill=green, width=50)

img.save('image-line-2.jpg')