import os
from PIL import Image

# Functions
def convert_files(subdirectory):
    
    print("\n===== CONVERTING =====")
    print("Processing " + os.path.basename(os.path.normpath(subdirectory)))

    for file in os.listdir(subdirectory):
        if file.endswith(accepted_filetypes):
            save_path = os.path.join(subdirectory, file + '.webp')
            converted_image = Image.open(subdirectory + "\\" + file)
            converted_image = converted_image.convert('RGB')
            converted_image.save(save_path, 'webp', optimize = True, quality = 90)
            print('Converted and saved: ' + os.path.basename(os.path.normpath(file)))
            os.remove(subdirectory + "\\" + file)
        continue
        
def rename_files(subdirectory):
    count = 0
    temp_count = 0
    
    print("\n===== RENAMING =====")
    print("Processing " + os.path.basename(os.path.normpath(subdirectory)))
    
    # rename all to temp
    for image in os.listdir(subdirectory):
        if image.endswith('.webp'):
            temp_path = os.path.join(subdirectory, "temp_" + os.path.basename(os.path.normpath(image)))
            os.rename(subdirectory + "\\" + image, temp_path)
     
    # actual rename
    for image in os.listdir(subdirectory):
        if image.endswith('.webp'):
            count += 1
            temp_count = count
            new_path = os.path.join(subdirectory, str(count).zfill(4) + '.webp')
            
            while os.path.isfile(new_path):
                print(new_path + " already exists.")
                temp_count += 1
                new_path = os.path.join(subdirectory, str(temp_count).zfill(4) + '.webp')
                
            os.rename(subdirectory + "\\" + image, new_path)
            print("Renamed: " + image + " => " + os.path.basename(os.path.normpath(new_path)))

# Execute
root = os.getcwd()
accepted_filetypes = ('.png', '.jpg', '.jpeg')
subdirectories = [f.path for f in os.scandir(root) if f.is_dir() ]
subdirectory_count = 0

print("This script will target the following folders:\n")
for subdirectory in subdirectories:
    subdirectory_count += 1
    print(str(subdirectory_count) + ". " + os.path.basename(os.path.normpath(subdirectory)))

print("\nPress ENTER to continue, or exit the application.")
input()

for subdirectory in subdirectories:
    convert_files(subdirectory)
    rename_files(subdirectory)