from PIL import Image

im1 = Image.open('image-cropped.jpg')
im2 = Image.open('image.jpg')


im2.paste(im1)
im2.show()