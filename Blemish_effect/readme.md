
This Python script is designed to simulate blemishes on images stored in a specified directory. It uses the OpenCV library for image processing.

## Installation

Ensure you have Python installed on your system. You can install the required libraries using pip:

```bash
pip install opencv-python numpy
```
Usage
Place your images in a directory named dataset.
Run the ```script blemish_effect.py```.
The script will process each .png image in the dataset directory, simulate blemishes on them, and save the modified images in an output directory.
Parameters
You can adjust the following parameters in the script according to your preferences:

image_dir: Path to the directory where your images are stored.
output_dir: Path to the directory where modified images with blemishes will be saved.
blemish_size: Size of the blemishes to be drawn on the images.
num_blemishes: Number of blemishes to be drawn on each image.
alpha_blend: Weight for blending the original image with the blemish mask.
Example
bash
Copy code
python blemish_effect.py
This command will run the script and process all .png images in the dataset directory, adding blemishes to them and saving the modified images in the output directory.

Author
This script was created by [Alkhatab_albusaidi].

