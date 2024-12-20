import os
import sys
from PIL import Image

accepted_filetypes = ('.png', '.jpg', '.jpeg', '.webp', '.JPG')
format = "webp"

if (len(sys.argv) > 1):
    print("Found argument for format " + sys.argv[1])
    format = sys.argv[1]

print("Converting images to format " + format)

for image in os.listdir(".\\input\\"):
    if image.endswith(accepted_filetypes):  
        converted_image = Image.open(os.getcwd() + "\\input\\" + image)
        path = os.getcwd() + "\\output\\" + os.path.splitext(os.path.basename(image))[0] + "." + format
        converted_image.save(path, format, optimize = True, quality = 90)
        print("Converted " + os.path.splitext(os.path.basename(path))[0])