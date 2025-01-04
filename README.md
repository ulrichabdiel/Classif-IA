# Classif-IA

Bienvenue sur **Classif-IA** !  
Une application intuitive conçue pour classer des images en fonction de leur classe proche grâce à un modèle basé sur des réseaux de neurones convolutifs (CNN).

---

## Fonctionnalités principales

- **Classification d'images** : Déterminez la classe proche à laquelle appartient une image parmi 10 catégories, telles que :
  - Chien, Chat, Camion, Automobile, Grenouille, Cheval, Avion, Cerf, et autres.
- **Rapidité et précision** : Notre modèle CNN atteint une précision de **81%** dans le processus de classification.
- **Génération de rapports PDF** : Téléchargez un rapport complet de classification directement depuis l'application.

**Note** : Classif-IA est une application de **classification d'image** et non une application de reconnaissance d'image. Par exemple, une image représentant un "Aigle royal volant" peut être classée comme un "Avion", car notre modèle se concentre sur des catégories proches.

---

## Mode d'utilisation

### Étape 1 : Importer des images
- Cliquez sur **"Browse files"** pour importer vos images.
- Formats supportés : **PNG**, **JPG**, **JPEG**, **BMP**.
- Limite : Jusqu'à **12 images** avec une taille maximale de **200 MB** par fichier.  
**Conseil** : Pour une meilleure précision, utilisez des images qui correspondent directement aux classes définies.

### Étape 2 : Classer les images
- Une fois les images importées, cliquez sur **"Classer les images"**.  
- Le modèle analysera vos images et affichera la classe prédite sous chacune d'entre elles.

### Étape 3 : Télécharger un rapport
- Après la classification, téléchargez un rapport au format PDF en cliquant sur **"Avoir le rapport"**.  
- Le fichier sera enregistré dans votre dossier **Téléchargements** ou **Downloads**.

---

## À propos de l'équipe
Nous sommes une équipe d'ingénieurs statisticiens économistes de ISE ENEAM, spécialisés en analyse de données et en solutions innovantes.
Nos chefs de projet :

- Mr. Abdiel Ulrich ZOUNTCHEME -Ingénieur Statisticien Économiste
- Mr. Brillant BABA -Ingénieur Statisticien Économiste

---

## Technologies utilisées

L'application repose sur des outils robustes et performants :  
- **[NumPy](https://numpy.org/)** : Manipulation de données et calculs numériques.  
- **[Pillow](https://python-pillow.org/)** : Gestion des images.  
- **[Streamlit](https://streamlit.io/)** : Développement de l'interface utilisateur.  
- **[TensorFlow](https://www.tensorflow.org/)** : Modélisation et classification des images.

Voici les dépendances principales utilisées dans le projet :
```plaintext
numpy==2.2.1
Pillow==11.1.0
streamlit==1.39.0
tensorflow_intel==2.18.0

