import streamlit as st
from PIL import Image
import base64
from io import BytesIO
import backend_projet_6
from fpdf import FPDF

# Configurer la page
st.set_page_config(page_title="ClassifIA", layout="wide")

# CSS pour positionner les logos avec un z-index élevé
st.markdown(
    """
    <style>
        .left-logo {
            position: fixed;
            top: 10px;
            left: 10px;
            z-index: 1000;
        }
        .right-logo {
            position: fixed;
            top: 10px;
            right: 10px;
            z-index: 1000;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Fonction pour convertir une image en base64
def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Ajouter les logos avec CSS
try:
    logo_left_path = r"C:/Users/HP/Downloads/projet_6/projet_streamlit/images/ise.png"
    logo_left = Image.open(logo_left_path).resize((200, 200))
    logo_left_base64 = image_to_base64(logo_left)
    st.markdown(
        f'<img class="left-logo" src="data:image/png;base64,{logo_left_base64}">',
        unsafe_allow_html=True
    )
except FileNotFoundError:
    st.write("Logo gauche non disponible.")

try:
    logo_right_path = r"C:/Users/HP/Downloads/projet_6/projet_streamlit/images/eneam.png"
    logo_right = Image.open(logo_right_path).resize((100, 100))
    logo_right_base64 = image_to_base64(logo_right)
    st.markdown(
        f'<img class="right-logo" src="data:image/png;base64,{logo_right_base64}">',
        unsafe_allow_html=True
    )
except FileNotFoundError:
    st.write("Logo droit non disponible.")

# Chargement et affichage des fichiers CSS et HTML
try:
    with open(r"C:/Users/HP/Downloads/projet_6/projet_streamlit/file_css/style.css") as css_file:
        css = css_file.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

    with open(r"C:/Users/HP/Downloads/projet_6/projet_streamlit/file_html/index.html") as html_file:
        html_content = html_file.read()
    st.markdown(html_content, unsafe_allow_html=True)
except FileNotFoundError as e:
    st.write(f"Fichier introuvable : {e}")

# Zone d'importation d'images
uploaded_files = st.file_uploader("Importer des images", type=["png", "jpg", "jpeg", "bmp"], accept_multiple_files=True)

if uploaded_files:
    st.session_state["images"] = uploaded_files

    st.markdown("# **Images importées :**")
    cols = st.columns(5)
    img_files = []

    for i, file in enumerate(uploaded_files):
        img = Image.open(file)
        resized_img = img.resize((150, 150))
        cols[i % 5].image(resized_img, caption=file.name, width=150)
        img_files.append(file)

    st.markdown(
        """
        <style>
            .stImage img {
                border: 2px solid black;
                border-radius: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    if st.button("Classer les Images"):
        
        try:
            predictions = backend_projet_6.classify_images(img_files)
            st.write("## Résultats de la Classification")
            for file, pred in zip(img_files, predictions):
                st.image(file, caption=f"Classe prédite : {pred}", use_column_width=True)

            if st.button("Réinitialiser"):
                st.session_state.clear()
                st.stop()
        except Exception as e:
            st.error(f"Erreur lors de la classification : {e}")

# Chargement et affichage des fichiers CSS et HTML supplémentaires
try:
    with open(r"C:/Users/HP/Downloads/projet_6/projet_streamlit/file_css/team.css") as css_file:
        css = css_file.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

    with open(r"C:/Users/HP/Downloads/projet_6/projet_streamlit/file_html/team.html") as html_file:
        html_content = html_file.read()
    st.markdown(html_content, unsafe_allow_html=True)
except FileNotFoundError as e:
    st.write(f"Fichier introuvable : {e}")
