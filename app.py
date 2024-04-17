import streamlit as st
import base64

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
field1 = st.text_input("Enter field1:")
field2 = st.number_input("Enter field2:", min_value=0, max_value=150, value=30, step=1)
field3 = st.number_input("Enter field3:", min_value=0, max_value=150, value=30, step=1)

# Center the "Generate Message" button
col1, col2, col3 = st.columns([1, 2, 1])

# Button to generate message
with col2:
    if st.button("Guess the star"):
        if field1 and field2 and field3:
            st.success(f"Hi, you submitted {field1}, {field2} and {field3} successfully!")
        else:
            st.warning("Please fill in all the fields.")
