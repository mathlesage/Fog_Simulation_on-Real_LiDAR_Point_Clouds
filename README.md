# Analyse et Visualisation du Dataset STF

Ce projet s'appuie sur les travaux de Martin Hahner : [LiDAR_fog_sim](https://github.com/MartinHahner/LiDAR_fog_sim).

## Mes Ajouts 


- **`affichage_modification.py`** : Génère le brouillard et crée une heatmap (jaune vers rouge) pour visualiser précisément quels points ont été déplacés par la simulation.
- **`bin_to_ply.py`** : Convertit les fichiers bruts `.bin` du dataset en fichiers `.ply` standards pour permettre une lecture facile dans n'importe quel logiciel 3D.
- **`label_image.py`** : Analyse les fichiers JSON d'origine pour créer un fichier `inventaire_meteo.csv` listant les conditions (clair, brouillard, pluie, neige) de chaque scan.
