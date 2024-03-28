import cv2
import numpy as np
import os

# Define the directory where your images are stored
image_dir = "dataset"

# Create an output directory if it doesn't exist
output_dir = "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Loop through each image file in the directory
for filename in os.listdir(image_dir):
    if filename.endswith(".png"):
        # Read the image
        img_path = os.path.join(image_dir, filename)
        img = cv2.imread(img_path)
        
        # Create a blank mask image
        mask = np.zeros_like(img)
        
        # Generate random positions for blemishes
        for _ in range(50):  # Adjust the number of blemishes you want
            x = np.random.randint(0, img.shape[1])
            y = np.random.randint(0, img.shape[0])
            
            # Draw blemish on the mask
            cv2.circle(mask, (x, y), 10, (255, 255, 255), -1)
        
        # Apply Gaussian blur to the mask
        blurred_mask = cv2.GaussianBlur(mask, (51, 51), 0)
        
        # Convert the mask to grayscale
        blurred_mask_gray = cv2.cvtColor(blurred_mask, cv2.COLOR_BGR2GRAY)
        
        # Invert the mask
        inverted_mask = cv2.bitwise_not(blurred_mask_gray)
        
        # Convert the inverted mask to alpha channel
        alpha = cv2.cvtColor(inverted_mask, cv2.COLOR_GRAY2BGR)
        
        # Blend the original image and the alpha channel
        result = cv2.addWeighted(img, 0.7, alpha, 0.3, 0)
        
        # Save the image with blemishes
        output_path = os.path.join(output_dir, filename)
        cv2.imwrite(output_path, result)
        
        # Report the image and its saved location
        print(f"Blemishes drawn on {filename} and saved at {output_path}")

print("All .png images processed successfully!")

