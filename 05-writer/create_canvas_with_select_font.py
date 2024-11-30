from PIL import Image, ImageDraw, ImageFont

fnt = ImageFont.truetype('arial.ttf', size=55)

img = Image.new('RGB', (900, 500), (255, 255, 255))

d = ImageDraw.Draw(img)

d.text((150, 100), "Hello World!", font=fnt, fill=(0, 0, 0))

img.save('canvas_with_select_font.png')