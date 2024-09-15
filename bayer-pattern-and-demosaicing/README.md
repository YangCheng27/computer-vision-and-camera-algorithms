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

## Placeholder
TBD



