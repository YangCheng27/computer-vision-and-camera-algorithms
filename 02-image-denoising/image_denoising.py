import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys


def get_noisy_image(path, mean=0, sigma=5):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    #img = cv2.resize(img, (1000, 750))
    gauss_noise = np.random.normal(mean, sigma, img.shape).astype(img.dtype)
    img_noisy = cv2.add(img, gauss_noise)
    return img, img_noisy

def get_noisy_image_color(path, mean=0, sigma=5):
    img= cv2.imread(path) #BGR
    #img = cv2.resize(img, (1000, 750))
    row, col, ch = img.shape
    gauss = np.random.normal(mean, sigma, (row, col, ch))  # 產生高斯噪聲
    gauss_noise = gauss.reshape(row, col, ch).astype('uint8')  # 將噪聲轉換為 uint8 類型
    img_noisy = cv2.add(img, gauss_noise)
    return img, img_noisy

def visualization(imgs: dict):
    cnt = len(imgs)
    fig, axes = plt.subplots(3, 2, figsize = (6, 8))
    axes = axes.flatten()  

    num = 0
    img_noisy = None
    for img in imgs:
        axes[num].imshow(imgs[img], cmap = 'gray')
        axes[num].axis('off')

        if img == 'img_orig':
            img_noisy = imgs[img]
            axes[num].set_title(img)
        else:
            psnr = cv2.PSNR(img_noisy, imgs[img])
            axes[num].set_title(img + f', psnr: {psnr: .2f}')
        num += 1
    plt.tight_layout()
    plt.show()

def get_mean_filter_results(img_orig, img_noisy):
    mean_filtering_3 = cv2.blur(img_noisy, (3,3))
    mean_filtering_9 = cv2.blur(img_noisy, (9,9))
    mean_filtering_15 = cv2.blur(img_noisy, (15,15))
    mean_filtering_21 = cv2.blur(img_noisy, (21,21))

    imgs = {'img_orig': img_orig, 'img_noisy': img_noisy, 'mean_filter_3': mean_filtering_3,
            'mean_filter_9': mean_filtering_9, 'mean_filter_15': mean_filtering_15, 'mean_filter_21': mean_filtering_21}
    return imgs

def get_gaussian_filter_results(img_orig, img_noisy):
    gaussian_filtering_3 = cv2.GaussianBlur(img_noisy, (3,3), 0)
    gaussian_filtering_9 = cv2.GaussianBlur(img_noisy, (9,9), 0)
    gaussian_filtering_15 = cv2.GaussianBlur(img_noisy, (15,15), 0)
    gaussian_filtering_21 = cv2.GaussianBlur(img_noisy, (21,21), 0)

    imgs = {'img_orig': img_orig,
            'img_noisy': img_noisy,
            'gaussian_filter_3': gaussian_filtering_3,
            'gaussian_filter_9': gaussian_filtering_9,
            'gaussian_filter_15': gaussian_filtering_15,
            'gaussian_filter_21': gaussian_filtering_21}
    return imgs

def get_median_filter_results(img_orig, img_noisy):
    median_filtering_3 = cv2.medianBlur(img_noisy, 3)
    median_filtering_9 = cv2.medianBlur(img_noisy, 9)
    median_filtering_15 = cv2.medianBlur(img_noisy, 15)
    median_filtering_21 = cv2.medianBlur(img_noisy, 21)
    imgs = {'img_orig': img_orig,
            'img_noisy': img_noisy,
            'median_filter_3': median_filtering_3,
            'median_filter_9': median_filtering_9,
            'median_filter_15': median_filtering_15,
            'median_filter_21': median_filtering_21}
    return imgs

if __name__ == '__main__':

    # original image visualization
    img_color_orig, img_color_noisy = get_noisy_image_color(sys.argv[1], mean=0, sigma=2)
    plt.subplot(1,2,1); plt.title('original image'); plt.axis('off'); plt.imshow(img_color_orig)
    plt.subplot(1,2,2); plt.title('noisy image'); plt.axis('off'); plt.imshow(img_color_noisy)
    fig = plt.gcf()
    fig.set_size_inches(12, 6)
    plt.tight_layout()
    plt.show()

    visualization(get_mean_filter_results(img_color_orig, img_color_noisy))
    visualization(get_gaussian_filter_results(img_color_orig, img_color_noisy))
    visualization(get_median_filter_results(img_color_orig, img_color_noisy))