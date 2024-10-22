import os
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

ground_truth_folder = '/home/stud1/Desktop/Anushree/Datasets_complete/LOLv1/LOLv1/train/our485/high'
model_output_folder = '/home/stud1/Desktop/Anushree/Diffusion-Low-Light-remote/results_500/test/LOLv1'

image_names = os.listdir(ground_truth_folder)

ssim_values = []

for image_name in image_names:
   
    gt_image_path = os.path.join(ground_truth_folder, image_name)
    model_image_path = os.path.join(model_output_folder, image_name)

    gt_image = cv2.imread(gt_image_path)
    model_image = cv2.imread(model_image_path)

    if gt_image is None or model_image is None:
        print(f"Error loading images: {gt_image_path} or {model_image_path}")
        continue

    gt_image_gray = cv2.cvtColor(gt_image, cv2.COLOR_BGR2GRAY)
    model_image_gray = cv2.cvtColor(model_image, cv2.COLOR_BGR2GRAY)

    ssim_value, _ = ssim(gt_image_gray, model_image_gray, full=True)
    ssim_values.append(ssim_value)

ssim_mean = np.mean(ssim_values)
ssim_median = np.median(ssim_values)

print(f"Mean SSIM: {ssim_mean:.4f}")
print(f"Median SSIM: {ssim_median:.4f}")

for i, ssim_value in enumerate(ssim_values):
    print(f"SSIM for image {image_names[i]}: {ssim_value:.4f}")
