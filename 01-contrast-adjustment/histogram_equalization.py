import cv2
print(cv2.__version__)
import numpy as np
import matplotlib.pyplot as plt


def show_img_and_hist(name, img):
    plt.figure(figsize=(15, 5))

    plt.subplot(1,2,1)
    plt.title(name)
    plt.imshow(img, cmap = 'gray')
    plt.axis('off')

    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * float(hist.max()) / cdf.max()
    plt.subplot(1,2,2)
    plt.title('Historgram and CDF')
    plt.plot(cdf_normalized, color = 'r')
    plt.hist(img.flatten(),256,[0,256], color = 'b')
    plt.xlim([0,256])
    plt.ylim([0,180000])
    plt.legend(('cdf','histogram'), loc = 'upper left')

    plt.tight_layout()
    plt.savefig('results/' + name)
    plt.show()


def hist_equ(img):
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_m = np.ma.masked_equal(cdf,0)
    cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
    cdf = np.ma.filled(cdf_m,0).astype('uint8')
    img_hist_equ = cdf[img]
    return img_hist_equ


if __name__ == "__main__":
    # original image
    img = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)
    show_img_and_hist('Original Image', img)

    img_his_equ = hist_equ(img)
    show_img_and_hist('Histogram Eualization', img_his_equ)

    ahe = cv2.createCLAHE(clipLimit = 10000, tileGridSize = (8, 8))
    img_ahe = ahe.apply(img)
    show_img_and_hist('AHE', img_ahe)

    clahe = cv2.createCLAHE(clipLimit = 2, tileGridSize = (8, 8))
    img_clahe = clahe.apply(img)
    show_img_and_hist('CLAHE', img_clahe)
