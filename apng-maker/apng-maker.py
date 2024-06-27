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

# Convert to apng
filename = (os.path.splitext(os.path.basename(frames[0]))[0]).split('_', 1)[0]
APNG.from_files(frames, delay=int(delay)).save(filename + ".png")