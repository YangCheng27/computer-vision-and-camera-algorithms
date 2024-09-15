# 02-image-denoising

This file contains implementations of various neighbor filters for **image denoising** using OpenCV.
The goal is to remove noise while preserving important information features in the image.
Noise is often introduced during image acquisition due to sensor limitations, compression, or transmission errors.

In this file, I will demonstrate three common image smoothing techniques: **Mean Blurring**, **Gaussian Blurring**, and **Median Blurring**.
These techniques involve selecting a small neighborhood around each pixel and applying different operations,
such as calculating the mean of the pixel values, computing a Gaussian-weighted average, or finding the median value within the neighborhood.
These operations replace the central pixel value with the result of the chosen operation.
In essence, noise removal at each pixel is localized to its surrounding neighborhood,
allowing for smoother and cleaner images while preserving important details like edges.


<p align="center">
  <img src="https://github.com/user-attachments/assets/d16fbb64-94c8-4fa3-ba2c-3e8ec3740964" width="400">
</p>

<p align="right">
  Image source: <a href="https://en.wikipedia.org/wiki/Kernel_(image_processing)">Wikipedia</a>
</p>

## Evaluation Metric

Before delving into algorithms, let's explore a widely used metric for evaluating image denoising quality: **Peak Signal-to-Noise Ratio (PSNR)**.
It measures the ratio between the maximum possible power of an image signal and the power of corrupting noise.
PSNR is expressed in decibels (dB), and it provides a quantitative comparison of image quality after applying denoising algorithms.


The formula to calculate PSNR is:

$$
PSNR = 10 \cdot \log_{10} \left( \frac{MAX^2}{MSE} \right)
$$

- **MAX**: The maximum possible pixel value of the image (for an 8-bit image, this value is 255).
- **MSE (Mean Squared Error)**: The average of the squared differences between the original and processed image.

MSE formula:

$$
MSE = \frac{1}{m \cdot n} \sum_{i=0}^{m-1} \sum_{j=0}^{n-1} \left[ I(i,j) - K(i,j) \right]^2
$$

Where:
- \( ***I***(i,j) \) is the pixel value of the original image at position (i, j).
- \( ***K***(i,j) \) is the pixel value of the processed (e.g., denoised) image at position (i, j).
- \( m \) and \( n \) are the dimensions of the image.

### Interpreting PSNR:
- **30 dB and above**: Excellent quality, minimal noise.
- **20-30 dB**: Acceptable quality, but some noise may be visible.
- **Below 20 dB**: Significant noise or distortion, poor image quality.

PSNR is commonly used to assess the performance of image denoising techniques, where a higher PSNR indicates that the algorithm has effectively reduced noise while preserving important image details.


## Denoising Neighbor Filters

#### Features
- Add Gaussian noise to color image.
- Apply three types of filters with different kernel sizes.: Mean, Gaussian, and Median filters.
- Visualize the original, noisy, and denoised images side by side.
- Calculate and display PSNR to evaluate the performance of denoising algorithms.

<p align="center">
  <img src="https://github.com/user-attachments/assets/e1ab4e76-14e3-4b51-8dae-3da0dc4e64e6" width="1200">
</p>

### 1. Mean Filter

The mean filter is a simple smoothing technique where the pixel value is replaced by the average of the pixel values within the neighborhood defined by the kernel. It reduces noise, but it also blurs the image, especially for larger kernel sizes.

<p align="center">
  <img src="https://github.com/user-attachments/assets/52baa3d3-36bd-4d93-b262-7f920ff2a541" width="600">
</p>

### 2. Gaussian Filter

The Gaussian filter applies a weighted average based on a Gaussian distribution, where pixels closer to the center have more influence than those farther away. While the PSNR values are slightly higher than those of the mean filter, the overall increase is not significant. It still blurs the image as the kernel size increases.

<p align="center">
  <img src="https://github.com/user-attachments/assets/e9fe3df7-7b12-419a-a834-cc25042faf7e" width="600">
</p>

### 3. Median Filter

The median filter replaces each pixel with the median value of the neighboring pixels. The results show a dramatic improvement in PSNR for the 9x9 kernel, indicating that the median filter excels at reducing noise while maintaining image sharpness. However, for larger kernels (15x15 and 21x21), the PSNR decreases slightly, indicating that over-smoothing occurs when the kernel size is too large, leading to some loss of detail.

<p align="center">
  <img src="https://github.com/user-attachments/assets/93c158be-7b50-4349-8721-93d40d7a5e75" width="600">
</p>


