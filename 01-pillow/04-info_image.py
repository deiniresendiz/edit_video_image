from PIL import Image

im = Image.open('image.jpg')
print("El fichero se llama {}".format(im.filename))
print("El tamaño es {}".format(im.size))
print("El formato es {}".format(im.format))
print("El número de colores es {}".format(im.mode))
print("La altura es {}".format(im.height))
print("La anchura es {}".format(im.width))

#solo funciona con formatos de archivo de imagen
print("La paleta de la imagen es {}".format(im.palette))
print("El diccionario de información de la imagen es {}".format(im.info))