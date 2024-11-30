from PIL import Image, ImageDraw

img = Image.new('RGB', (500, 400), (255, 255, 255))

d = ImageDraw.Draw(img)

d.text((50, 40), "Hello World!", fill=(0, 0, 0))

img.save('canvas_with_text.png')