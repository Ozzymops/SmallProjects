# scan folder -> convert -> rename
import os
import sys
from PIL import Image

# Count files
def count_files(dir, whitelist, target):
    files = 0
    
    for file in os.listdir(dir):
        if (file.endswith(whitelist) and not file.endswith(target)):
            files += 1       
    return files

# Convert files
def convert_files(dir, whitelist, target):
    print("|| CONVERTING '" + os.path.basename(os.path.normpath(dir)) + "' ||")
    
    for file in os.listdir(dir):
        if (file.endswith(whitelist) and not file.endswith(target)):
            save_path = os.path.join(dir, file + target)
            converted_image = Image.open(dir + "\\" + file)
            converted_image = converted_image.convert('RGB')
            
            if "jpg" in target.lower():
               converted_image.save(save_path, "JPEG", optimize = True, quality = 90) 
            else:
                converted_image.save(save_path, target.lstrip('.'), optimize = True, quality = 90)
                
            print('Converted and saved: ' + os.path.basename(os.path.normpath(file)))
            os.remove(dir + "\\" + file)

# Rename files
def rename_files(dir, whitelist, target):
    print("|| RENAMING '" + os.path.basename(os.path.normpath(dir)) + "' ||")
    count = 0
    temp_count = 0
    
    # temporary rename to not have it all fuck up
    for file in os.listdir(dir):
        if (file.endswith(whitelist)):
            temp_path = os.path.join(dir, "temp_{name}".format(name = file))
            os.rename(dir + "\\" + file, temp_path)
            
    # actual rename
    for file in os.listdir(dir):
        if (file.endswith(whitelist)):
            count += 1
            temp_count = count
            new_path = os.path.join(dir, str(count).zfill(4) + target)
                        
            # check for duplicate name
            while os.path.isfile(new_path):
                temp_count += 1
                new_path = os.path.join(dir, str(temp_count).zfill(4) + target)
            
            os.rename(dir + "\\" + file, new_path)
            print("Renamed {old} => {new}".format(old = file, new = new_path)) 
    
# Start
def main(argv):
    root = os.getcwd()
    whitelist = ('.png', '.jpg', '.JPG', '.jpeg', '.webp')

    target = input("Target filetype: ")
    target_sub = input("Subdirs? 'Y' for yes, or anything else for no. ")
    
    if target_sub.lower() == "y":
        target_sub = True
    else:
        target_sub = False

    subdirs = []

    print("This script will target the following directories:")
    print("1. [root] {dir} ({count})".format(dir = os.path.basename(os.path.normpath(root)), count = count_files(root, whitelist, target)))

    # subdirectory check
    if (target_sub):
        subdirs = [f.path for f in os.scandir(root) if f.is_dir()]

    if (target_sub and len(subdirs) != 0):
        subdir_count = 1
        for dir in subdirs:
            subdir_count += 1
            print("{subdir}. {dir} ({count})".format(subdir = subdir_count, dir = os.path.basename(os.path.normpath(dir)), count = count_files(dir, whitelist, target)))   
        print()

    # final verification
    print("Press ENTER to continue, or exit the application.")
    input()

    # run
    convert_files(root, whitelist, target)
    rename_files(root, whitelist, target)

    for dir in subdirs:
        convert_files(dir, whitelist, target)
        rename_files(dir, whitelist, target)
        
if __name__ == "__main__":
    main(sys.argv[1:])