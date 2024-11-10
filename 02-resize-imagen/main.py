import sys
from PIL import Image

def resize_image(filename):
    img = Image.open(filename)
    print("width: {}, height: {}".format(img.width, img.height))
    third_width = img.width // 3
    third_height = img.height // 3
    print("new width: {}, new height: {}".format(third_width, third_height))
    third_img = img.resize((third_width, third_height))
    third_img.save(filename.replace(".jpg", "-third.jpg"))
    print("width: {}, height: {}".format(third_img.width, third_img.height))

def crop_image(filename):
    img = Image.open(filename)
    print("width: {}, height: {}".format(img.width, img.height))
    left = 1000
    top = 200
    right = img.width - 1000
    bottom = img.height - 100
    print("left: {}, top: {}, right: {}, bottom: {}".format(left, top, right, bottom))
    cropped_img = img.crop((left, top, right, bottom))
    cropped_img.save(filename.replace(".jpg", "-cropped.jpg"))
    print("width: {}, height: {}".format(cropped_img.width, cropped_img.height))


def zoom_image(src, dest=None, zoom=1):
    img = None
    try:
        img = Image.open(src)
    except:
        print("Error: No se pudo abrir el archivo {}".format(src))

    if not dest:
        pos_dot = src.rfind('.')
        dest = src[:pos_dot] + '_zoom_' + str(zoom) + src[pos_dot:]

    width, height = img.size
    new_width = int(width * zoom)
    new_height = int(height * zoom)

    print("zoom: {} width: {}, height: {}".format(zoom, width, height))
    print("new width: {}, new height: {}".format(new_width, new_height))

    img = img.resize((new_width, new_height))
    left = int((new_width - width) / 2)
    top = int((new_height - height) / 2)
    right = left + width
    bottom = top + height
    print("left: {}, top: {}, right: {}, bottom: {}".format(left, top, right, bottom))
    cropped_img = img.crop((left, top, right, bottom))
    cropped_img.save(dest)
    print("width: {}, height: {}".format(cropped_img.width, cropped_img.height))



if __name__ == "__main__":
    #resize_image("image.jpg")
    #crop_image("image.jpg")
    zoom_image("image.jpg", zoom=5)