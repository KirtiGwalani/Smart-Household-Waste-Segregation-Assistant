import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from pathlib import Path

# Page settings
st.set_page_config(
    page_title="Smart Waste Segregation Assistant",
    page_icon="♻️",
    layout="centered"
)

# Model configuration
MODEL_PATH = Path(__file__).parent / "smart_waste_final_candidate.keras"
NON_GLASS_THRESHOLD = 0.35

@st.cache_resource
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)

# Application title
st.title("♻️ Smart Household Waste Segregation Assistant")

st.write(
    "Upload a household waste image to identify whether "
    "the object is Glass or Non-Glass."
)

st.caption(
    "An AI-based prototype for assisting household waste segregation."
)

# Load model
try:
    model = load_model()
except Exception as e:
    st.error(f"Could not load model: {e}")
    st.stop()

# Image upload
uploaded_file = st.file_uploader(
    "Upload a waste image",
    type=["jpg", "jpeg", "png", "webp"]
)

if uploaded_file is not None:

    try:
        image = Image.open(uploaded_file).convert("RGB")

        st.image(
            image,
            caption="Uploaded waste image",
            use_container_width=True
        )

        if st.button("Classify Image"):

            with st.spinner("Analysing image..."):

                # Resize image
                resized_image = image.resize((224, 224))

                # Convert image into numerical array
                image_array = np.array(
                    resized_image,
                    dtype=np.float32
                )

                image_array = np.expand_dims(
                    image_array,
                    axis=0
                )

                # Predict Non-Glass score
                non_glass_score = float(
                    model.predict(image_array, verbose=0)[0][0]
                )

                glass_score = 1 - non_glass_score

                # Classification using selected threshold
                if non_glass_score >= NON_GLASS_THRESHOLD:
                    prediction = "Non-Glass"
                else:
                    prediction = "Glass"

            # Display result
            st.subheader(f"Prediction: {prediction}")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Glass model score",
                    f"{glass_score * 100:.2f}%"
                )

            with col2:
                st.metric(
                    "Non-Glass model score",
                    f"{non_glass_score * 100:.2f}%"
                )

            # Segregation guidance
            st.subheader("Segregation Guidance")

            if prediction == "Glass":
                st.success(
                    "The model identifies this object as Glass. "
                    "Check local recycling guidelines before disposal. "
                    "Handle broken glass carefully."
                )
            else:
                st.info(
                    "The model identifies this object as Non-Glass. "
                    "Check the material type and follow local waste "
                    "segregation and recycling guidelines."
                )

            st.warning(
                "This is an experimental AI prototype. Predictions "
                "may be incorrect, especially for transparent, "
                "reflective, or unfamiliar objects. Always verify "
                "the material before disposal."
            )

    except Exception as e:
        st.error(f"Unable to process this image: {e}")


