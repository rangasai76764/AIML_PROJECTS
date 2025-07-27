import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Class labels
class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", 
               "Sandal", "Shirt", "Sneaker", "Bag", "Ankle Boot"]

# Load model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("Image_Classification_CNN_app.h5")

model = load_model()

st.title("🧠 Image Classification Using CNN")
st.write("Upload a 28x28 grayscale image to classify fashion items.")

uploaded_file = st.file_uploader("Upload image...", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("L")  # convert to grayscale
    image_resized = image.resize((28, 28))
    st.image(image_resized, caption="Uploaded Image", width=150)

    # Preprocess
    img_array = np.array(image_resized).astype("float32") / 255.0
    img_array = img_array.reshape(1, 28, 28, 1)

    prediction = model.predict(img_array)
    class_id = np.argmax(prediction)
    confidence = np.max(prediction)

    st.success(f"🧠 Prediction: **{class_names[class_id]}** ({confidence:.2%} confidence)")
