# 01-contrast-adjustment

This file contains implementations of various image processing techniques for **histogram equalization** and **contrast enhancement** using OpenCV.
The goal is to enhance the contrast of grayscale images and analyze the changes through their histograms and cumulative distribution functions (CDFs).

## Why Contrast Adjustment?
Consider an image where the pixel values are restricted to a specific range.
For example, a darker image will have most of its pixel values concentrated in the lower range.
However, ***an ideal image should have pixel values distributed across the entire intensity spectrum, from dark to bright***.
To achieve this, the histogram needs to be stretched towards both ends, and this is essentially what **histogram equalization** does. 
This process typically enhances image contrast, improving the interpretability of visual data and making images more suitable for further analysis in computer vision tasks.

<p align="center">
  <img src="https://github.com/user-attachments/assets/9a75282a-6edd-4606-b199-76fcf025f468" width="400">
</p>

<p align="right">
  Image source: <a href="https://en.wikipedia.org/wiki/Histogram_equalization">Wikipedia</a>
</p>



## Example Image: Demonstrating Histogram Equalization

<p align="center">
  <img src="https://github.com/user-attachments/assets/8566ea94-9ca4-4d5c-a781-91fbd68e929c" width="1000">
</p>

The demonstrated image is of Eda U. Gerstacker Grove on the North Campus of the University of Michigan.
The histogram shows that this image's grayscale distribution is concentrated in three distinct areas.
This is not ideal, as such an image lacks detail and natural gradation. However, is there a way we can improve it?

**Yes! Histogram Equalization !!!**

In the next section, I'll use three different histogram equalization techniques to enhance it.



## Contrast Adjustment Algorithms
### 1. Histogram Equalization (HE)

<p align="center">
  <img src="https://github.com/user-attachments/assets/a2f48f52-cba0-4b4d-bb5c-1482303f00e1" width="1000">
</p>

### 2. Adaptive Histogram Equalization (AHE)

<p align="center">
  <img src="https://github.com/user-attachments/assets/3a95c878-b08a-4278-b824-2a6e2888efe8" width="1000">
</p>

### 3. Contrast Limited Adaptive Histogram Equalization (CLAHE)

<p align="center">
  <img src="https://github.com/user-attachments/assets/e7b68588-8b05-4a8d-b9e0-aa071d944717" width="1000">
</p>
