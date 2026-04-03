# Analyse et Visualisation du Dataset STF

Ce projet s'appuie sur les travaux de Martin Hahner : [LiDAR_fog_sim](https://github.com/MartinHahner/LiDAR_fog_sim).

## Mes Contributions 


- **`affichage_modification.py`** : Génère le brouillard et crée une heatmap (jaune vers rouge) pour visualiser précisément quels points ont été déplacés par la simulation.
- **`bin_to_ply.py`** : Convertit les fichiers bruts `.bin` du dataset en fichiers `.ply` standards pour permettre une lecture facile dans n'importe quel logiciel 3D.
- **`label_image.py`** : Analyse les fichiers JSON d'origine pour créer un fichier `inventaire_meteo.csv` listant les conditions (clair, brouillard, pluie, neige) de chaque scan.

## Installation

1. Installer [Anaconda](https://docs.anaconda.com/anaconda/install/).

2. Créer un nouvel environnement conda.

```bash
conda create --name foggy_lidar python=3.9 -y
```

3. Activer l'environnement.

```bash
conda activate foggy_lidar
```

4. Installer les dépendances.

```bash
conda install matplotlib numpy opencv pandas plyfile pyopengl pyqt pyqtgraph quaternion scipy tqdm -c conda-forge -y
pip install pyquaternion
```

5. Cloner le dépôt (avec les sous-modules).

```bash
git clone git@github.com:MartinHahner/LiDAR_fog_sim.git --recursive
cd LiDAR_fog_sim
```

## Usage

Visualiser la théorie d'un faisceau LiDAR en conditions de brouillard :

```bash
python theory.py
```

![theory](https://user-images.githubusercontent.com/14181188/115370049-f9b74200-a1c8-11eb-88d0-474b8dd5daa3.gif)

Visualiser des nuages de points entiers de différents datasets :

```bash
python pointcloud_viewer.py -d <path_to_where_you_store_your_datasets>
```