## README

This script is designed to organize image and label files into separate directories for testing purposes. It operates in the following steps:

1. **Move Label Files**: The script iterates through each set (`set00` to `set10`) in the `generated_labels` directory and moves corresponding label files to the `test_labels` directory. Each label file is renamed to include the set number.

2. **Consolidate Label Files**: It checks and moves label files containing `s00` to `s06` in their names from the `test_labels` directory to the `test_labels` directory itself.

3. **Move Image Files**: Similarly, the script iterates through each set (`set00` to `set10`) in the `generated_img` directory and moves corresponding image files to the `test_images` directory. Each image file is renamed to include the set number.

4. **Consolidate Image Files**: It checks and moves image files containing `s00` to `s06` in their names from the `test_images` directory to the `test_images` directory itself.

5. **Validate File Integrity**: Finally, the script checks if every PNG file in `test_images` has a corresponding TXT file in `test_labels`. If not, it deletes the PNG files without corresponding TXT files.

### Usage

1. **Directories**: Ensure that you have the following directory structure:
