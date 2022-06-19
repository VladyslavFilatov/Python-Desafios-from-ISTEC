import os
import re
os.chdir(r'/Users/vladyslavfilatov/Downloads/images scrambled_2')

for image in os.listdir():
  ext = image.split(".")[-1]

  if ext.lower() in ['png', 'jpg', 'jpeg']:
    rename_file = re.sub(r'[0-9]+', '', image)
    os.rename(image, rename_file)
sort_a = os.listdir()
sort_a.sort()
print("Mensagem perdida: Keys are in the closet. Behind the shoe box.")
input()

