from PIL import Image

img = Image.open('image.jpg')

img = img.transpose(method=Image.FLIP_LEFT_RIGHT)

img.save('image-mirror-left.jpg')