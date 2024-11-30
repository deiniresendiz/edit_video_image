from PIL import Image, ImageFilter

img = Image.open('image.jpg')
#The limit of this property would be 50; beyond that, the difference is not noticeable.
img = img.filter(ImageFilter.BoxBlur(10))

img.save('image-boxblur.jpg')