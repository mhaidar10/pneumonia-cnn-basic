import streamlit as st
import tensorflow as tf
from PIL import Image
import requests
from io import BytesIO

# Load the pre-trained model
model_path = 'model/pneunomia_model.h5'
model = tf.keras.models.load_model(model_path)

def preprocess_image(image):
    # Convert the image to grayscale
    img_gray = image.convert('L')

    # Resize the image to the required input shape for the model
    img_gray = img_gray.resize((200, 200))
    # Convert the image to a NumPy array
    img_array = tf.keras.preprocessing.image.img_to_array(img_gray)

    # Expand the dimensions to match the model's expected input shape
    img_array = tf.expand_dims(img_array, axis=0)
    img_array = tf.expand_dims(img_array, axis=-1)  # Add a channel dimension

    # Normalize the pixel values to the range [0, 1]
    img_array /= 255.0

    return img_array

def predict(image):
    img = preprocess_image(image)
    prediction = model.predict(img)
    return prediction

# Streamlit UI
st.set_page_config(page_title="Pneumonia Detection App", page_icon=":microscope:")

st.header('Pneumonia Detection :sparkles:')

with st.sidebar:
    
    # Menambahkan logo perusahaan
    st.image("https://upload.wikimedia.org/wikipedia/commons/7/77/Streamlit-logo-primary-colormark-darktext.png")
    

    # Define the URL and link text
    url = "https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia"
    link_text = "Dataset Source"

    # Create the link
    st.write('Chest X-Ray(Pneumonia) Dataset')
    st.write(f"[{link_text}]({url})")

    url_sc = "https://github.com/mhaidar10/pneumonia-cnn-basic"
    link_text_sc = "Visit Source"

    # Create the link
    st.write('Chest X-Ray(Pneumonia) Source Code')
    st.write(f"[{link_text_sc}]({url_sc})")




uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image_url = st.text_input("Or enter image URL:")

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Predict"):
        # Make predictions when the user clicks the button
        prediction = predict(image)
        st.subheader("Prediction:")
        if prediction[0][0] > 0.5:
            st.write("Pneumonia Detected")
        else:
            st.write("No Pneumonia Detected")

elif image_url:
    # Fetch image from URL
    try:
        image_response = requests.get(image_url)
        image = Image.open(BytesIO(image_response.content))
        st.image(image, caption="Image from URL", use_column_width=True)

        if st.button("Predict"):
            # Make predictions when the user clicks the button
            prediction = predict(image)
            st.subheader("Prediction:")
            if prediction[0][0] > 0.5:
                st.write("Pneumonia Detected")
            else:
                st.write("No Pneumonia Detected")
    except Exception as e:
        st.error(f"Error loading image from URL: {e}")

else:
    st.warning("Please upload an image or enter an image URL.")
