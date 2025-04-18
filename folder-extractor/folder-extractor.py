import os
import sys
import shutil
import string
import random

# Generate gibberish
def gibberish():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))

# Copy files
def copy_files(source_dir, target_dir, whitelist):
    for file in os.listdir(source_dir):
        try:
            full_path = os.path.join(source_dir, file)
            if os.path.isfile(full_path):
                print(f"Found file: {file}")
                if file.lower().endswith(whitelist):
                    extension = os.path.splitext(file)[1]
                    new_name = gibberish() + extension
                    target_path = os.path.join(target_dir, new_name)
                    shutil.copyfile(full_path, target_path)
                    print(f"Copied: {file} → {new_name}")
        except Exception as e:
            print(f"Error handling file {file}: {e}")

# Rename files
def rename_files(dir, whitelist):
    count = 0

    # temporary rename to avoid conflicts
    for file in os.listdir(dir):
        full_path = os.path.join(dir, file)
        if os.path.isfile(full_path) and file.lower().endswith(whitelist):
            temp_path = os.path.join(dir, f"temp_{file}")
            os.rename(full_path, temp_path)

    # actual rename
    for file in os.listdir(dir):
        full_path = os.path.join(dir, file)
        if os.path.isfile(full_path) and file.lower().endswith(whitelist):
            count += 1
            extension = os.path.splitext(file)[1]
            new_name = f"{str(count).zfill(4)}{extension}"
            new_path = os.path.join(dir, new_name)

            # check for duplicates
            while os.path.exists(new_path):
                count += 1
                new_name = f"{str(count).zfill(4)}{extension}"
                new_path = os.path.join(dir, new_name)

            os.rename(full_path, new_path)
            print(f"Renamed {file} => {new_name}")

# Start
def main(argv):
    root = os.getcwd()
    whitelist = ('.png', '.jpg', '.jpeg', '.webp', '.pngjpg')

    extracted = os.path.join(root, "extracted")
    os.makedirs(extracted, exist_ok=True)

    subdirs = []
    for dirpath, dirnames, filenames in os.walk(root):
        if os.path.normpath(dirpath) == os.path.normpath(extracted):
            continue  # Skip the extracted dir
        subdirs.append(dirpath)

    print("This script will target the following directories:\n")
    for i, dir in enumerate(subdirs, 1):
        print(f"{i}. {os.path.basename(dir)}")
    print("\nPress ENTER to continue, or exit the application.")
    input()

    for dir in subdirs:
        copy_files(dir, extracted, whitelist)

    rename_files(extracted, whitelist)

if __name__ == "__main__":
    main(sys.argv[1:])
