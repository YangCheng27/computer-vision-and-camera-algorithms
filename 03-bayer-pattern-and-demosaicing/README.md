# bayer-pattern-and-demosaicing

The **Bayer pattern** is a **CFA** (color filter array) used in most digital cameras to capture color images. Each pixel on the camera's sensor is covered by a color filter (either red, green, or blue), allowing only light of that specific color to reach the sensor. Since the **human eye is more sensitive to green light**, the Bayer pattern assigns 50% of the pixels to green and the remaining pixels equally to red and blue, creating a 2x2 grid with two green pixels, one red, and one blue. The sensor records the intensity of light for each pixel, and a process called **demosaicing** is applied later to reconstruct a full-color image by interpolating the missing color information for each pixel.

<p align="center">
  <img src="https://github.com/user-attachments/assets/99600c6a-08e6-4a44-9e05-20d99407200a" width="400">
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/b9b50524-2032-4f42-901c-bcc5deed3a20" width="400">
</p>


<p align="right">
  Image source: <a href="https://en.wikipedia.org/wiki/Bayer_filter">Wikipedia</a>
</p>

> The physics of light.

Physics behind the Bayer pattern:
Optics: The pattern leverages the properties of light and filters it into RGB components.
Human vision: The pattern mimics the way the human eye perceives color, prioritizing green to align with the eye's higher sensitivity to green wavelengths.
Sensor technology: The sensor detects the intensity of light that passes through the filter, and the Bayer pattern ensures efficient color sampling.
This combination allows cameras to create high-quality color images using a relatively simple and cost-effective sensor design.

<p align="center">
  <img src="https://github.com/user-attachments/assets/3e63ee81-1b09-4bae-ae8c-d9b53b0b3e50" width="400">
</p>

<p align="right">
  Image source: <a href="https://en.wikipedia.org/wiki/Cone_cell">Wikipedia</a>
</p>

## Demosaicing

**Demosaicing** is a method used in digital image processing to reconstruct a full-color image from the incomplete color samples output by an **image sensor** overlaid with a **Bayer filter**. A Bayer filter captures color information for red, green, and blue channels by placing a mosaic of color filters over the camera's sensor, where each pixel records only one of the three primary colors.

#### 1. Bayer Filter
This program uses a **Bayer filter** to simulate this process and then implements interpolation techniques to recover the full RGB image.

<p align="center">
  <img src="https://github.com/user-attachments/assets/8a721a27-6cfc-4d81-a132-4d177e8cfa7e" width="800">
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/be5b17a3-b777-4e43-934f-9832365fe6e9" width="800">
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/1ae5cb8a-673c-4d64-a5e6-a1c0c11cd163" width="800">
</p>

#### 2. Demosaicing
The algorithm **rgb_demosaicing(img_gray)** interpolates the missing color information for each pixel. Green pixels are used to recover the red and blue channels, and red and blue pixels are used to recover the green channel.

<p align="center">
  <img src="https://github.com/user-attachments/assets/e981a33d-646b-4346-bb35-55ebac41d78c" width="800">
</p>

> Helper Functions:

- **four_neighbors_avg**: Averages the color values of the four neighboring pixels.
- **four_corners_avg**: Averages the values of the four diagonal corner pixels.
- **top_bottom_avg**: Averages the top and bottom neighboring pixels.
- **left_right_avg**: Averages the left and right neighboring pixels.

#### 3. Result: recovered image

This file demonstrates the basic principles of demosaicing using a Bayer filter, a fundamental technique in digital image processing. Through this script, we simulate how digital cameras process raw sensor data to generate full-color images.

<p align="center">
  <img src="https://github.com/user-attachments/assets/88ee9887-1657-4e58-986a-4252f2056dc0" width="800">
</p>



