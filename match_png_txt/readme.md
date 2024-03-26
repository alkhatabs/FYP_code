
README
This script is designed to organize image and label files into separate directories for testing purposes. It operates in the following steps:

Move Label Files: The script iterates through each set (set00 to set10) in the "generated_labels" directory and moves corresponding label files to the "test_labels" directory. Each label file is renamed to include the set number.

Consolidate Label Files: It checks and moves label files containing 's00' to 's06' in their names from the "test_labels" directory to the "test_labels" directory itself.

Move Image Files: Similarly, the script iterates through each set (set00 to set10) in the "generated_img" directory and moves corresponding image files to the "test_images" directory. Each image file is renamed to include the set number.

Consolidate Image Files: It checks and moves image files containing 's00' to 's06' in their names from the "test_images" directory to the "test_images" directory itself.

Validate File Integrity: Finally, the script checks if every PNG file in "test_images" has a corresponding TXT file in "test_labels". If not, it deletes the PNG files without corresponding TXT files.

Usage
Directories: Ensure that you have the following directory structure:

Copy code
├── generated_img
│   ├── set00
│   │   ├── V001_N001.png
│   │   └── ...
│   ├── set01
│   │   ├── V001_N001.png
│   │   └── ...
│   └── ...
├── generated_labels
│   ├── set00
│   │   ├── V001_frame001.txt
│   │   └── ...
│   ├── set01
│   │   ├── V001_frame001.txt
│   │   └── ...
│   └── ...
├── test_images
└── test_labels
Execution: Run the script. It will organize the files as described above.

Output: After execution, the "test_images" and "test_labels" directories will contain organized files suitable for testing purposes.

Notes
Ensure that all necessary libraries, particularly os and shutil, are installed.
Before executing the script, ensure that you have backed up any important data as it performs file operations that may modify your directory structure.
