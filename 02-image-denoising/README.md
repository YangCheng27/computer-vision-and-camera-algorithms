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

<p align="center">
  <img src="https://github.com/user-attachments/assets/cdb6733a-0a73-4a34-8050-23747f4d7567" width="1200">
</p>

### 1. Mean Filter

<p align="center">
  <img src="https://github.com/user-attachments/assets/a4a626d1-06b7-4cb3-b19e-22becfa088d5" width="600">
</p>

### 2. Gaussian Filter

<p align="center">
  <img src="https://github.com/user-attachments/assets/e5b7df8f-5a90-4440-a00c-93f3f27c76d7" width="600">
</p>

### 3. Median Filter

<p align="center">
  <img src="https://github.com/user-attachments/assets/be919d7a-76a4-45d1-86fc-494305c8de72" width="600">
</p>


