# CT-MRI Thoracic Image Fusion using Wavelet Transform

## AIM

To combine CT and MRI thoracic images using wavelet-based fusion to create a single image that preserves both bone structures (from CT) and soft tissue details (from MRI), improving diagnostic accuracy and aiding medical decision-making.

## OBJECTIVES

* Understand multi-sensor image fusion
* Apply wavelet-based fusion
* Evaluate fused image using SSIM
* Provide comprehensive thoracic view

## TOOLS & TECHNOLOGIES

* Python 3.x
* NumPy
* OpenCV
* Matplotlib
* PyWavelets
* Scikit-image

## ALGORITHM

1. Load CT and MRI images
2. Resize MRI to match CT
3. Apply DWT
4. Fuse coefficients using max rule
5. Perform inverse DWT
6. Calculate SSIM-based accuracy
7. Display images




## RESULT

The fused image successfully combines CT and MRI features, preserving both bone and soft tissue details, improving diagnostic interpretation.
