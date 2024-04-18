import streamlit as st
import base64
from optimize.model import predict_class

# Set page title and icon
st.set_page_config(page_title="Stellar discover")

# Import custom CSS file
with open("custom_styles.css", "r") as f:
    custom_css = f.read()

# Inject custom CSS into Streamlit app
st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)

# Custom CSS to apply background image
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('./assets/starry_night.jpg')

# Page title
st.title("Welcome to the world of astrophysics")

# Input fields
color = st.selectbox("Select Star Color:", ['red', 'blue white', 'white', 'yellowish white',
       'pale yellow orange', 'blue', 'whitish', 'yellow white', 'orange',
       'white yellow', 'yellowish', 'orange red'])
temperature = st.number_input("Enter Temperature (K):", min_value=2000.0, max_value=40000.0, value=2000.0, step=1.0)
luminosity = st.number_input("Enter Luminosity (L/Lo):", min_value=0.0, max_value=900000.0, value=0.0, step=0.01)
radius = st.number_input("Enter Radius (R/Ro):", min_value=0.0, max_value=2000.0, value=0.0, step=0.01)
magnitude = st.number_input("Enter Absolute magnitude (Mv):", min_value=-10.0, max_value=20.0, value=0.0, step=0.01)
type = st.number_input("Enter Star type:", min_value=1.0, max_value=5.0, value=1.0, step=1.0)

# Center the "Generate Message" button
col1, col2, col3 = st.columns([1, 2, 1])

# Button to generate message
with col2:
    if st.button("Guess the star"):
        if color and temperature and luminosity and radius and magnitude and type:
            input_fields = [temperature, luminosity, radius, magnitude, type, color]
            result = predict_class(input_fields)
            st.success(f"The predicted class is {result}")  # Display the predicted class
        else:
            st.warning("Please fill in all the fields.")
