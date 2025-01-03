from fpdf import FPDF
import streamlit as st

from fpdf import FPDF
import streamlit as st

# Fonction pour créer le rapport PDF
def create_pdf():
    pdf = FPDF()

    # Définir les couleurs pour les titres
    main_color = (0, 102, 204)  # Bleu principal
    secondary_color = (102, 204, 102)  # Vert secondaire

    # Fonction pour ajouter des titres avec couleur
    def add_colored_title(text, color, size=18):
        pdf.set_text_color(*color)
        pdf.set_font("Arial", size=size, style='B')
        pdf.cell(0, 10, txt=text, ln=True, align="C")
        pdf.set_text_color(0, 0, 0)  # Retour à la couleur par défaut
        pdf.ln(8)

    # Première page avec le logo et titre principal
    pdf.add_page()
    pdf.image("ise.png", x=10, y=10, w=30)  # Logo ISE
    pdf.image("eneam.png", x=170, y=10, w=30)  # Logo ENEAM

    pdf.ln(25)
    add_colored_title("Projet 6 - Classification d'image", main_color, size=24)

    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 8, txt="Il s'agit de la classification d'images en utilisant le classificateur des k voisins les plus proches (Machine Learning), on évaluera comment régler au mieux les hyper paramètres correspondants. Et surtout vous construirez cette IA permettant de classifier ces images et leur assigner une étiquette pour savoir ce qu'il y a sur cette image! Vous travaillerez sur le dataset le plus utilisé dans le domaine de la classification pour entrainer votre IA. "
    "VisionPro est une application de classification d'images qui utilise des réseaux de neurones convolutifs (CNN). L'application permet d'importer des images et de les classer automatiquement en fonction de catégories pré-définies. Ce projet vise à offrir une solution simple et rapide pour l'analyse d'images et leur classification. Cette application est particulièrement utile dans les domaines de l'intelligence artificielle et de la vision par ordinateur, où des modèles de CNN sont utilisés pour traiter des images avec une grande précision. ")

    # Contexte du projet
    pdf.add_page()
    pdf.image("ise.png", x=10, y=10, w=30)
    pdf.image("eneam.png", x=170, y=10, w=30)
    pdf.ln(25)

    add_colored_title("Contexte du Projet", main_color)

    pdf.set_font("Arial", size=12)
    context_text = (
        "Le projet consiste à développer une application capable de classer des images à l'aide de l'intelligence artificielle. "
        "Pour ce faire, un modèle de Réseau de Neurones Convolutifs (CNN) a été utilisé. Le CNN est un type de modèle de deep learning "
        "spécialement conçu pour traiter des données sous forme d'images. Grâce à sa capacité à extraire des caractéristiques complexes "
        "des images, il est particulièrement performant dans des tâches telles que la reconnaissance d'objets et la classification d'images.\n\n"
        "Les données utilisées pour ce projet proviennent de CIFAR-10, une base de données populaire en apprentissage machine. "
        "Cette base de données contient 60 000 images de 32x32 pixels, réparties en 10 classes différentes. Les classes incluent des catégories telles que "
        "des avions, des automobiles, des oiseaux, des chats, des chiens, des grenouilles, des chevaux, des navires, des camions et des voitures. "
        "Cette base de données permet de tester la performance des modèles de classification sur des images variées, ce qui est essentiel "
        "pour l'apprentissage des réseaux neuronaux convolutifs.\n\n"
        "Le modèle CNN utilisé pour ce projet a été entraîné sur l'ensemble des images de CIFAR-10 et a été optimisé pour "
        "produire des prédictions précises et rapides. L'application VisionPro utilise ce modèle pour fournir une interface simple "
        "et rapide permettant aux utilisateurs de télécharger et de classer leurs images automatiquement."
    )
    pdf.multi_cell(0, 8, txt=context_text)

    # Page avec les chefs de projet et leurs images
    pdf.add_page()
    pdf.ln(15)  # Espacement en haut

    add_colored_title("Chefs de Projet", secondary_color)

# Affichage des images et des noms des chefs de projet
    pdf.ln(10)  # Espacer un peu avant les images

# Espacement avant la première image
    pdf.ln(10)

# Centrer la première image et agrandir
    image_x = (pdf.w - 40) / 2  # Calculer la position x pour centrer l'image
    pdf.image("abdiel.jpg", x=image_x, y=pdf.get_y(), w=50)  # Image centrée et agrandie
    pdf.ln(50)  # Espacer l'image du texte (ajusté pour l'espacement souhaité)
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, txt="1. Abdiel Ulrich ZOUNTCHEME - Ingénieur Statisticien Économiste", ln=True, align="C")
    pdf.cell(0, 10, txt="   Cycle II ISE-ENEAM", ln=True, align="C")

# Espacement avant la deuxième image
    pdf.ln(10)  # Ajuste l'espacement entre les sections

# Centrer la deuxième image et agrandir
    pdf.image("abdiel.jpg", x=image_x, y=pdf.get_y(), w=50)  # Image centrée et agrandie
    pdf.ln(50)  # Espacer l'image du texte
    pdf.cell(0, 10, txt="2. Brillant BABA - Ingénieur Statisticien Économiste", ln=True, align="C")
    pdf.cell(0, 10, txt="   Cycle II ISE-ENEAM", ln=True, align="C")


    # Générer le PDF en mémoire
    pdf_output = pdf.output(dest='S').encode('latin1')
    return pdf_output

# Fonction pour télécharger le PDF
def download_pdf(pdf_output):
    st.download_button(
        label="Télécharger maintenant",
        data=pdf_output,
        file_name="Rapport du Projet.pdf",
        mime="application/pdf"
    )

# Streamlit - Exemple d'utilisation
st.title("Recevez le PDF avant l'entraînement - Rapport PDF")


# Bouton pour générer et télécharger le rapport
if st.button("Avoir le Rapport"):
    pdf_output = create_pdf()
    download_pdf(pdf_output)
