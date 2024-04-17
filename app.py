import streamlit as st
import os
import base64

# Set page title and icon
st.set_page_config(page_title="Stellar discover")

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
name = st.text_input("Enter field1:")
age = st.number_input("Enter field2:", min_value=0, max_value=150, value=30, step=1)

# Center the "Generate Message" button
col1, col2, col3 = st.columns([1, 2, 1])

# Button to generate message
with col2:
    if st.button("Generate Message"):
        if name and age:
            if age < 18:
                st.error(f"Hi {name}, you are under 18 years old. You are not allowed to access this content.")
            else:
                st.success(f"Hi {name}, you are {age} years old. Welcome to our app!")
        else:
            st.warning("Please fill in all the fields.")
