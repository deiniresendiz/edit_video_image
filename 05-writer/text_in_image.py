from PIL import Image, ImageDraw, ImageFont


img = Image.open('image.jpg')

fnt = ImageFont.truetype('arial.ttf', size=55)

d = ImageDraw.Draw(img)

d.text((50, 40), "Hello World!", font=fnt, fill=(255, 255, 255))

img.save('text_in_image.png')