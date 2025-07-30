import streamlit as st
from PIL import Image
import base64
from KrishiMitraa import run_app

# Set page config
st.set_page_config(page_title="KrishiMitra", layout="centered")

# Load and encode image for background
def set_background(image_file):
    with open(image_file, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    css = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    [data-testid="stHeader"], [data-testid="stToolbar"] {{
        background: rgba(0,0,0,0);
    }}
    [data-testid="stSidebar"], [data-testid="collapsedControl"] {{
        display: none;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# ✅ Set the background image
set_background("image.jpg")

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "welcome"

def go_to_main():
    st.session_state.page = "main"

# Welcome Page
if st.session_state.page == "welcome":
    st.markdown("<h1 style='text-align: center; color: white;'>Welcome to KrishiMitra 🌾</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: white;'>Empowering Farmers with AI</h4>", unsafe_allow_html=True)

    st.markdown("---")

    with st.form("user_info"):
        language = st.selectbox("🌐 Select Language", ["English", "Hindi", "Telugu", "Tamil", "Marathi"])
        region = st.selectbox("📍 Select Your Region", ["Punjab", "Maharashtra", "Telangana", "UP", "Tamil Nadu"])
        submitted = st.form_submit_button("Continue")

        if submitted:
            st.session_state.language = language
            st.session_state.region = region
            go_to_main()

# Main Page
elif st.session_state.page == "main":
    st.markdown(f"### 🌍 Language: {st.session_state.language} | 📍 Region: {st.session_state.region}")
    st.markdown("""
        <h2 style='color: green;'>Welcome, Farmer!</h2>
        <p>This is the main KrishiMitra interface. Below is your full app.</p>
    """, unsafe_allow_html=True)

    run_app()

    st.button("🔙 Go Back", on_click=lambda: st.session_state.update({"page": "welcome"}))