from PIL import Image, ImageFilter

img = Image.open('image.jpg')

#img = img.filter(ImageFilter.BLUR)

for i in range(0, 10):
    img = img.filter(ImageFilter.BLUR)

img.save('image-blurry.jpg')