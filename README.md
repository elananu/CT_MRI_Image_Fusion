# 🩻 CT-MRI Thoracic Image Fusion using Wavelet Transform

## 🚀 Live Demo

**[Open the Deployed CT-MRI Image Fusion Application](https://elananu-ct-mri-image-fusion-app-5qhud7.streamlit.app/)**

---

## 📌 Project Overview

CT and MRI are two important medical imaging modalities that provide different types of information.

* **CT (Computed Tomography)** provides detailed information about bones and high-density structures.
* **MRI (Magnetic Resonance Imaging)** provides detailed information about soft tissues.

This project combines CT and MRI thoracic images using a **Wavelet Transform-based image fusion technique** to produce a single fused image containing useful information from both modalities.

The application provides an interactive web interface where users can upload CT and MRI images, perform image fusion, evaluate the result using SSIM, and download the fused image.

---

## 🎯 AIM

To combine CT and MRI thoracic images using wavelet-based fusion to create a single image that preserves both bone structures from CT and soft-tissue details from MRI, supporting improved image interpretation and medical decision-making.

---

## 🎯 OBJECTIVES

* Understand multi-sensor medical image fusion.
* Combine complementary information from CT and MRI images.
* Apply Discrete Wavelet Transform (DWT).
* Perform wavelet coefficient-based image fusion.
* Reconstruct the fused image using inverse DWT.
* Evaluate the fused image using Structural Similarity Index Measure (SSIM).
* Provide an easy-to-use web-based interface.
* Allow users to download the generated fused image.

---

## 🧠 Problem Definition

CT and MRI images provide complementary information about the human body. CT is particularly useful for visualizing bone structures, while MRI provides better soft-tissue contrast.

Analyzing these images separately can make it difficult to obtain all relevant information at once.

Therefore, this project aims to develop an image fusion system that combines information from CT and MRI images into a single fused image.

---

## ⚙️ Methodology

The application follows these steps:

```text
        CT Image
            │
            ▼
      Preprocessing
            │
            │
            ├──────────────┐
            │              │
            ▼              ▼
       DWT on CT      DWT on MRI
            │              │
            └──────┬───────┘
                   ▼
          Wavelet Coefficient
               Fusion
                   │
                   ▼
             Inverse DWT
                   │
                   ▼
            Fused Image
                   │
          ┌────────┴────────┐
          ▼                 ▼
       SSIM Score      Download Image
```

---

## 🔬 Algorithm

1. Upload the CT image.
2. Upload the MRI image.
3. Convert the images into grayscale format.
4. Resize the MRI image to match the CT image dimensions.
5. Apply Discrete Wavelet Transform (DWT) to both images.
6. Separate the wavelet coefficients into:

   * Approximation coefficients
   * Horizontal detail coefficients
   * Vertical detail coefficients
   * Diagonal detail coefficients
7. Fuse corresponding wavelet coefficients using a maximum-selection rule.
8. Apply inverse DWT to reconstruct the fused image.
9. Calculate SSIM for evaluating image similarity.
10. Display the CT, MRI, and fused images.
11. Allow the user to download the fused image.

---

## 🛠️ Tools & Technologies

### Programming Language

* Python 3.x

### Libraries

* NumPy
* OpenCV
* PyWavelets
* Scikit-image
* Pillow
* Matplotlib

### Web Framework

* Streamlit

### Version Control

* Git
* GitHub

### Deployment

* Streamlit Community Cloud

---

## ✨ Features

* 🩻 CT image upload
* 🧠 MRI image upload
* 🔄 Wavelet-based image fusion
* 🖼️ CT image preview
* 🖼️ MRI image preview
* 🧬 Fused image generation
* 📊 SSIM-based evaluation
* 📐 Image resolution information
* ⬇️ Download fused image
* 🌐 Online Streamlit deployment
* 🎨 Interactive web dashboard

---

## 📊 Evaluation

The project uses **Structural Similarity Index Measure (SSIM)** to evaluate the similarity between the fused image and the input images.

The application displays:

* CT-Fused SSIM
* MRI-Fused SSIM
* Average SSIM

A higher SSIM value indicates greater structural similarity between the compared images.

---

## 📂 Project Structure

```text
CT_MRI_Image_Fusion/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── ct.png
├── mri.png
└── output.png
```

### File Description

| File               | Description                          |
| ------------------ | ------------------------------------ |
| `app.py`           | Streamlit web application            |
| `main.py`          | Original image fusion implementation |
| `requirements.txt` | Required Python dependencies         |
| `ct.png`           | Sample CT image                      |
| `mri.png`          | Sample MRI image                     |
| `output.png`       | Sample fused output                  |
| `README.md`        | Project documentation                |

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/elananu/CT_MRI_Image_Fusion.git
```

Move into the project directory:

```bash
cd CT_MRI_Image_Fusion
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application Locally

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

## 🌐 Deployment

The application is deployed using **Streamlit Community Cloud**.

### Live Application

👉 **[Launch CT-MRI Thoracic Image Fusion](https://elananu-ct-mri-image-fusion-app-5qhud7.streamlit.app/)**

### Deployment Configuration

```text
Repository:
elananu/CT_MRI_Image_Fusion

Branch:
main

Main file:
app.py
```

---

## 📥 How to Use

1. Open the deployed application.
2. Upload a CT image.
3. Upload an MRI image.
4. Click **Fuse CT + MRI Images**.
5. Wait for the wavelet fusion process to complete.
6. View the generated fused image.
7. Check the SSIM evaluation results.
8. Download the fused image using the download button.

---

## 📈 Result

The application generates a fused CT-MRI image by combining information from both imaging modalities using Wavelet Transform.

The resulting image provides a combined representation of information from CT and MRI images. The application also provides SSIM-based evaluation and allows the generated fused image to be downloaded.

---

## 🔮 Future Enhancements

* Support for multiple medical image formats.
* Support for DICOM images.
* Batch CT-MRI image fusion.
* Additional fusion algorithms.
* Improved image quality metrics.
* Deep-learning-based image fusion.
* Enhanced visualization and comparison tools.
* Integration with medical image databases.

---

## ⚠️ Disclaimer

This project is developed for **educational and research purposes**.

The generated fused images should not be considered a replacement for professional medical diagnosis or clinical decision-making.

---

## 👨‍💻 Project

**CT-MRI Thoracic Image Fusion using Wavelet Transform**

**Technology:** Python + Streamlit + Wavelet Transform

**Deployment:** Streamlit Community Cloud

### 🔗 Live Application

**https://elananu-ct-mri-image-fusion-app-5qhud7.streamlit.app/**
