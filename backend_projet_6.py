# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 11:47:51 2024

@author: ADMIN
"""


import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Charger le modèle optimisé
MODEL_PATH = "cifar10_cnn_optimized_2.h5"
model = load_model(MODEL_PATH)

# Les classes de CIFAR-10
CLASSES = [
    "Avion", "Automobile", "Oiseau", "Chat", "Cerf",
    "Chien", "Grenouille", "Cheval", "Bateau", "Camion"
]

def preprocess_image(image_path, target_size=(32, 32)):
    """
    Prétraiter une image pour qu'elle soit compatible avec le modèle.
    
    :param image_path: Chemin de l'image
    :param target_size: Dimensions cibles pour le modèle (par défaut 32x32)
    :return: Image prétraitée sous forme de tableau numpy
    """
    try:
        image = load_img(image_path, target_size=target_size)
        image_array = img_to_array(image)
        image_array = image_array / 255.0  # Normalisation
        return np.expand_dims(image_array, axis=0)  # Ajouter une dimension pour le batch
    except Exception as e:
        raise ValueError(f"Erreur lors du prétraitement de l'image {image_path}: {e}")

def classify_images(image_paths):
    """
    Classifier une liste d'images en utilisant le modèle chargé.
    
    :param image_paths: Liste des chemins des images
    :return: Liste des classes prédites
    """
    predictions = []
    for image_path in image_paths:
        try:
            processed_image = preprocess_image(image_path)
            prediction = model.predict(processed_image, verbose=0)  # Prédiction
            predicted_class = CLASSES[np.argmax(prediction)]  # Classe ayant la plus grande probabilité
            predictions.append(predicted_class)
        except Exception as e:
            raise ValueError(f"Erreur lors de la classification de l'image {image_path}: {e}")
    return predictions
