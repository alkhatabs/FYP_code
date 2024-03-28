
This Python script is designed to simulate blemishes on images stored in a specified directory. It uses the OpenCV library for image processing.

## Installation

Ensure you have Python installed on your system. You can install the required libraries using pip:

```bash
pip install opencv-python numpy
```
## Usage

1. Place your images in a directory named `dataset`.
2. Run the script `blemish_effect.py`.
3. The script will process each `.png` image in the `dataset` directory, simulate blemishes on them, and save the modified images in an `output` directory.

## Parameters

You can adjust the following parameters in the script according to your preferences:

- `image_dir`: Path to the directory where your images are stored.
- `output_dir`: Path to the directory where modified images with blemishes will be saved.
- `blemish_size`: Size of the blemishes to be drawn on the images.
- `num_blemishes`: Number of blemishes to be drawn on each image.
- `alpha_blend`: Weight for blending the original image with the blemish mask.

## Example

```bash
python blemish_effect.py
