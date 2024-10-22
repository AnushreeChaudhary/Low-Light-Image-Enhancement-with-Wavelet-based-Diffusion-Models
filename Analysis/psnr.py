import cv2
import os
import numpy as np

def calculate_psnr(image1, image2):
    mse = np.mean((image1 - image2) ** 2)
    if mse == 0:  # If MSE is zero, return infinite PSNR (perfect match)
        return float('inf')
    psnr = 20 * np.log10(255.0 / np.sqrt(mse))
    return psnr

def get_images_from_folder(folder_path):
    image_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]
    image_files.sort()  # Ensure the same order for ground truth and outputs
    return image_files

def calculate_psnr_for_folders(ground_truth_folder, model_output_folder):
    gt_images = get_images_from_folder(ground_truth_folder)
    output_images = get_images_from_folder(model_output_folder)

    if len(gt_images) != len(output_images):
        print("The number of images in the folders do not match.")
        return

    psnr_values = []
    for gt_img_name, output_img_name in zip(gt_images, output_images):
        gt_img_path = os.path.join(ground_truth_folder, gt_img_name)
        output_img_path = os.path.join(model_output_folder, output_img_name)

        # Read the images
        gt_img = cv2.imread(gt_img_path, cv2.IMREAD_COLOR)
        output_img = cv2.imread(output_img_path, cv2.IMREAD_COLOR)

        if gt_img is None or output_img is None:
            print(f"Error reading images: {gt_img_name} or {output_img_name}")
            continue

        # Calculate PSNR
        psnr_value = calculate_psnr(gt_img, output_img)
        psnr_values.append(psnr_value)
        print(f"PSNR for {gt_img_name}: {psnr_value} dB")

    return psnr_values

# Provide the folder paths
ground_truth_folder = '/home/stud1/Desktop/Anushree/Datasets_complete/LOLv1/LOLv1/train/our485/high'
model_output_folder = '/home/stud1/Desktop/Anushree/Diffusion-Low-Light-remote/results_500/test/LOLv1'

# Calculate PSNR for all image pairs
psnr_values = calculate_psnr_for_folders(ground_truth_folder, model_output_folder)

# Print average PSNR
if psnr_values:
    print(f"Average PSNR: {np.mean(psnr_values)} dB")
    print(f"Median PSNR: {np.median(psnr_values)} dB")