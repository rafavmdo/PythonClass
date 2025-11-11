from os import system
system("cls")
from PIL import Image

img = Image.open("tigre.jpg")
img_colorida = Image.open("tigre.jpg")
img_pb = img_colorida.convert('L')
img_pb.save("foto_pb.jpg")
print("Imagem convertida para preto e branco!")


