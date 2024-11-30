from PIL import Image, ImageFilter
#The limit of this property would be 50; beyond that, the difference is not noticeable.
img = Image.open('image.jpg')

img = img.filter(ImageFilter.GaussianBlur(5))

img.save('image-blur.jpg')