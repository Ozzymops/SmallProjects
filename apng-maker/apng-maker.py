import os
import sys
from PIL import Image
from apng import APNG

accepted_filetypes = ('.png', '.jpg', '.jpeg')

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
Convert(frames, "result")

def Convert(frames, filename):
    APNG.from_files(frames, delay=int(delay)).save(filename + ".png")