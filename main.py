import numpy as np
import cv2
import matplotlib.pyplot as plt
import pywt
from skimage.metrics import structural_similarity as ssim


ct_path = "images/ct.png"
mri_path = "images/mri.png"

ct = cv2.imread(ct_path, cv2.IMREAD_GRAYSCALE)
mri = cv2.imread(mri_path, cv2.IMREAD_GRAYSCALE)


if ct is None:
    print("Error: Could not load CT image")
elif mri is None:
    print("Error: Could not load MRI image")
else:
 
    mri = cv2.resize(mri, (ct.shape[1], ct.shape[0]))

   
    def wavelet_fusion(img1, img2):
        coeffs1 = pywt.dwt2(img1, 'db1')
        coeffs2 = pywt.dwt2(img2, 'db1')

        cA1, (cH1, cV1, cD1) = coeffs1
        cA2, (cH2, cV2, cD2) = coeffs2

        
        cA = np.maximum(cA1, cA2)
        cH = np.maximum(cH1, cH2)
        cV = np.maximum(cV1, cV2)
        cD = np.maximum(cD1, cD2)

        fused = pywt.idwt2((cA, (cH, cV, cD)), 'db1')
        fused = np.uint8(np.clip(fused, 0, 255))

        return fused

   
    fused_img = wavelet_fusion(ct, mri)

   
    ssim_ct = ssim(ct, fused_img)
    ssim_mri = ssim(mri, fused_img)

    diagnostic_accuracy = (ssim_ct + ssim_mri) / 2 * 100

    
    cv2.imwrite("output/fused.png", fused_img)

    
    plt.figure(figsize=(15,5))

    plt.subplot(1,3,1)
    plt.imshow(ct, cmap='gray')
    plt.title("CT Image")

    plt.subplot(1,3,2)
    plt.imshow(mri, cmap='gray')
    plt.title("MRI Image")

    plt.subplot(1,3,3)
    plt.imshow(fused_img, cmap='gray')
    plt.title(f"Fused Image\nAccuracy: {diagnostic_accuracy:.2f}%")

    plt.tight_layout()
    plt.show()
