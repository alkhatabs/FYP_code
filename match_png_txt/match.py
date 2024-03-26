import os
import shutil

# Function to move files to the test_images directory
def move_files(png_file, set_number):
    new_filename = f"{os.path.splitext(png_file)[0]}_s{set_number:02d}.png"
    source_path = os.path.join("generated_img", f"set{set_number:02d}", png_file)
    destination_path = os.path.join("test_images", new_filename)

    # Ensure the destination directory exists before moving
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)

    shutil.move(source_path, destination_path)
    print(f"Moved {png_file} to test_images (set{set_number:02d})")

# Function to move txt files to the test_labels directory
def move_txt_files(txt_file, set_number):
    new_filename = f"{os.path.splitext(txt_file)[0]}_s{set_number:02d}.txt"
    source_path = os.path.join("generated_labels", f"set{set_number:02d}", txt_file)
    destination_path = os.path.join("test_labels", new_filename)

    # Ensure the destination directory exists before moving
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)

    shutil.move(source_path, destination_path)
    print(f"Moved {txt_file} to test_labels (set{set_number:02d})")

# Function to move txt files to the test_labels directory
def move_test_labels(txt_file):
    source_path = os.path.join("test_labels", txt_file)
    destination_path = os.path.join("test_labels", txt_file)

    # Ensure the destination directory exists before moving
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)

    shutil.move(source_path, destination_path)
    print(f"Moved {txt_file} to test_labels")

# Function to move images to the test_images directory
def move_test_images(png_file):
    source_path = os.path.join("test_images", png_file)
    destination_path = os.path.join("test_images", png_file)

    # Ensure the destination directory exists before moving
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)

    shutil.move(source_path, destination_path)
    print(f"Moved {png_file} to test_images")

# Create test_labels and test_images directories if they don't exist
os.makedirs("test_labels", exist_ok=True)
os.makedirs("test_images", exist_ok=True)

# Iterate through sets from set00 to set10
for set_number in range(11):
    # Iterate through txt files in generated_labels/set{set_number}
    txt_files = os.listdir(os.path.join("generated_labels", f"set{set_number:02d}"))
    total_files = len(txt_files)

    for idx, txt_file in enumerate(txt_files):
        # Move the corresponding txt file to the test_labels directory and add the set number to its name
        move_txt_files(txt_file, set_number)

        # Print progress
        print(f"Processing set{set_number:02d} - {idx + 1}/{total_files} files", end='\r')

# Check and move files in test_labels with 's00', 's01', 's02', 's03', 's04', 's05', or 's06' in their names to test_labels
test_labels_files = os.listdir("test_labels")
for txt_file in test_labels_files:
    if any(f"s{set_num:02d}" in txt_file for set_num in range(7)):
        move_test_labels(txt_file)

# Iterate through sets from set00 to set10
for set_number in range(11):
    # Iterate through png files in generated_img/set{set_number}
    png_files = os.listdir(os.path.join("generated_img", f"set{set_number:02d}"))
    total_files = len(png_files)

    for idx, png_file in enumerate(png_files):
        # Move the corresponding png file to the test_images directory and add the set number to its name
        move_files(png_file, set_number)

        # Print progress
        print(f"Processing set{set_number:02d} - {idx + 1}/{total_files} files", end='\r')

# Check and move files in test_images with 's00', 's01', 's02', 's03', 's04', 's05', or 's06' in their names to test_images
test_images_files = os.listdir("test_images")
for png_file in test_images_files:
    if any(f"s{set_num:02d}" in png_file for set_num in range(7)):
        move_test_images(png_file)

# Check if every PNG file in test_images has a corresponding TXT file in test_labels
test_images_files = os.listdir("test_images")
test_labels_files = os.listdir("test_labels")

# Delete PNG files in test_images without corresponding TXT files in test_labels
deleted_files_count = 0

for png_file in test_images_files:
    txt_file = f"{os.path.splitext(png_file)[0]}.txt"
    if txt_file not in test_labels_files:
        file_path = os.path.join("test_images", png_file)
        os.remove(file_path)
        print(f"Deleted {png_file}")
        deleted_files_count += 1

# Print completion message
print(f"\nProcessing complete. Number of deleted files: {deleted_files_count}")

