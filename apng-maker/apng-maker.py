import os
import sys
from PIL import Image
from apng import APNG

accepted_filetypes = ('.png')

# Command line argument, delay in ms
if (len(sys.argv) > 1):
    delay = sys.argv[1]
else:
    delay = 1000 # = 1 second

# Read files from 'frames' folder
frames = []

for image in os.listdir(".\\frames\\"):
    if image.endswith(accepted_filetypes):
        frames.append(os.getcwd() + "\\frames\\" + image)

# Sort into dictionary
# Basename: [image1, image2, image3]
frameList = {}

for frame in frames:
    framename = (os.path.splitext(os.path.basename(frame))[0]).split('_', 1)[0]
    if framename in frameList:
        frameList[framename].append(frame)
    else:
        tempList = [frame]
        frameList[framename] = tempList

# Convert to apng
for key in frameList:
    print(key)
    for value in frameList[key]:
        print("- " + value)
    APNG.from_files(frameList[key], delay=int(delay)).save(key + ".png")