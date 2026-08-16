import streamlit as st
import numpy as np
import cv2
import pywt
from PIL import Image
from skimage.metrics import structural_similarity as ssim
import io

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="CT-MRI Thoracic Image Fusion",
    page_icon="🩻",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #666;
    font-size: 18px;
    margin-bottom: 30px;
}

.card {
    padding: 20px;
    border-radius: 12px;
    background: white;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="title">🩻 CT-MRI Thoracic Image Fusion</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Wavelet Transform Based Medical Image Fusion</div>',
    unsafe_allow_html=True
)

st.divider()

# --------------------------------------------------
# AIM
# --------------------------------------------------

with st.expander("🎯 About the Project", expanded=True):

    st.write("""
    This application combines CT and MRI thoracic images using
    wavelet-based image fusion.

    CT images provide detailed bone structures, while MRI images
    provide better soft-tissue information. The fusion process
    combines information from both modalities into a single image.
    """)

# --------------------------------------------------
# IMAGE UPLOAD
# --------------------------------------------------

st.subheader("📤 Upload Medical Images")

col1, col2 = st.columns(2)

with col1:

    st.markdown("### 🦴 CT Image")

    ct_file = st.file_uploader(
        "Upload CT image",
        type=["png", "jpg", "jpeg"],
        key="ct_upload"
    )

with col2:

    st.markdown("### 🧠 MRI Image")

    mri_file = st.file_uploader(
        "Upload MRI image",
        type=["png", "jpg", "jpeg"],
        key="mri_upload"
    )

# --------------------------------------------------
# IMAGE LOADING FUNCTION
# --------------------------------------------------

def load_image(uploaded_file):

    image = Image.open(uploaded_file).convert("L")

    return np.array(image)


# --------------------------------------------------
# WAVELET FUSION
# --------------------------------------------------

def wavelet_fusion(ct, mri):

    # Resize MRI to CT dimensions

    mri = cv2.resize(
        mri,
        (ct.shape[1], ct.shape[0])
    )

    # Convert to floating point

    ct = ct.astype(np.float32)
    mri = mri.astype(np.float32)

    # Apply DWT

    ct_coeff = pywt.dwt2(ct, "haar")
    mri_coeff = pywt.dwt2(mri, "haar")

    ct_ll, (ct_lh, ct_hl, ct_hh) = ct_coeff
    mri_ll, (mri_lh, mri_hl, mri_hh) = mri_coeff

    # Maximum coefficient fusion

    fused_ll = np.maximum(ct_ll, mri_ll)

    fused_lh = np.maximum(ct_lh, mri_lh)

    fused_hl = np.maximum(ct_hl, mri_hl)

    fused_hh = np.maximum(ct_hh, mri_hh)

    # Inverse DWT

    fused = pywt.idwt2(
        (
            fused_ll,
            (
                fused_lh,
                fused_hl,
                fused_hh
            )
        ),
        "haar"
    )

    # Convert to image

    fused = np.clip(
        fused,
        0,
        255
    ).astype(np.uint8)

    return fused


# --------------------------------------------------
# FUSION PROCESS
# --------------------------------------------------

if ct_file is not None and mri_file is not None:

    ct = load_image(ct_file)

    mri = load_image(mri_file)

    st.divider()

    st.subheader("🖼️ Input Images")

    col1, col2 = st.columns(2)

    with col1:

        st.image(
            ct,
            caption="CT Image",
            width="stretch"
        )

    with col2:

        st.image(
            mri,
            caption="MRI Image",
            width="stretch"
        )

    st.divider()

    # --------------------------------------------------
    # FUSE BUTTON
    # --------------------------------------------------

    if st.button(
        "🔄 Fuse CT + MRI Images",
        type="primary",
        width="stretch"
    ):

        with st.spinner(
            "Performing Wavelet Transform Fusion..."
        ):

            # Perform fusion

            fused = wavelet_fusion(
                ct,
                mri
            )

            # Resize MRI for evaluation

            resized_mri = cv2.resize(
                mri,
                (
                    ct.shape[1],
                    ct.shape[0]
                )
            )

            # --------------------------------------------------
            # SSIM
            # --------------------------------------------------

            h = min(
                ct.shape[0],
                fused.shape[0]
            )

            w = min(
                ct.shape[1],
                fused.shape[1]
            )

            ct_eval = ct[:h, :w]

            fused_eval = fused[:h, :w]

            score_ct = ssim(
                ct_eval,
                fused_eval,
                data_range=255
            )

            mri_eval = resized_mri[:h, :w]

            score_mri = ssim(
                mri_eval,
                fused_eval,
                data_range=255
            )

            average_ssim = (
                score_ct + score_mri
            ) / 2

        # --------------------------------------------------
        # RESULT
        # --------------------------------------------------

        st.divider()

        st.subheader("🧬 Fused Image")

        st.image(
            fused,
            caption="CT-MRI Fused Image",
            width="stretch"
        )

        # --------------------------------------------------
        # METRICS
        # --------------------------------------------------

        st.subheader("📊 Fusion Evaluation")

        metric1, metric2, metric3 = st.columns(3)

        with metric1:

            st.metric(
                "CT-Fused SSIM",
                f"{score_ct:.4f}"
            )

        with metric2:

            st.metric(
                "MRI-Fused SSIM",
                f"{score_mri:.4f}"
            )

        with metric3:

            st.metric(
                "Average SSIM",
                f"{average_ssim:.4f}"
            )

        # --------------------------------------------------
        # IMAGE INFORMATION
        # --------------------------------------------------

        st.subheader("📋 Image Information")

        info1, info2, info3 = st.columns(3)

        with info1:

            st.metric(
                "CT Resolution",
                f"{ct.shape[1]} × {ct.shape[0]}"
            )

        with info2:

            st.metric(
                "MRI Resolution",
                f"{mri.shape[1]} × {mri.shape[0]}"
            )

        with info3:

            st.metric(
                "Fused Resolution",
                f"{fused.shape[1]} × {fused.shape[0]}"
            )

        # --------------------------------------------------
        # DOWNLOAD
        # --------------------------------------------------

        output = io.BytesIO()

        Image.fromarray(
            fused
        ).save(
            output,
            format="PNG"
        )

        st.download_button(
            label="⬇️ Download Fused Image",
            data=output.getvalue(),
            file_name="CT_MRI_Fused_Image.png",
            mime="image/png",
            width="stretch"
        )

else:

    st.info(
        "📤 Please upload both CT and MRI images to start the fusion process."
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "CT-MRI Thoracic Image Fusion using Wavelet Transform | "
    "Developed using Python, Streamlit, PyWavelets and OpenCV"
)