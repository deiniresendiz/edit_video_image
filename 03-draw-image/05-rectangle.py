from PIL import Image, ImageDraw

img = Image.open('image.jpg')

width = img.size[0] * 60 //100
height = img.size[1] * 60 //100

margin_w = int((img.size[0] - width)//2)
margin_h = int((img.size[1] - height)//2)

area = (margin_w, margin_h, margin_w + width, margin_h + height)
blue = (0, 0, 255)
yellow = (255, 255, 0)

img1 = ImageDraw.Draw(img)
img1.rectangle(area, fill=blue, outline=yellow, width=50)


img.save('image-rectangle.jpg')

