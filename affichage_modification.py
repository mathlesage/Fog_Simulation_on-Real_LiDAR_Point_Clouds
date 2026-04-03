import numpy as np
import open3d as o3d
import os
import matplotlib.pyplot as plt
from fog_simulation import simulate_fog, ParameterSet

fichier_bin = r"data\lidar_hdl64_strongest\2018-12-12_09-34-31_03300.bin"
alphas_a_tester = [0.01, 0.03, 0.06, 0.1]
n_features = 5

print(f"Chargement du nuage de points original...")
if not os.path.exists(fichier_bin):
    raise FileNotFoundError(f"Fichier introuvable : {fichier_bin}")

points_originaux = np.fromfile(fichier_bin, dtype=np.float32).reshape(-1, n_features)

for alpha in alphas_a_tester:
    print(f"\n--- Génération du brouillard (Alpha = {alpha}) ---")
    
    p_set = ParameterSet(alpha=alpha, gamma=0.000001)
    points_brouillard, _, _ = simulate_fog(p_set, points_originaux, noise=10)
    vecteurs_deplacement = points_brouillard[:, :3] - points_originaux[:, :3]
    distances_m = np.linalg.norm(vecteurs_deplacement, axis=1)
    mask_deplaces = distances_m > 0.001
    
    couleurs = np.zeros((len(points_brouillard), 3))
    
    intensite_norm = np.clip(points_originaux[~mask_deplaces, 3] / 255.0, 0, 1)
    couleurs[~mask_deplaces] = np.column_stack((intensite_norm, intensite_norm, intensite_norm))

    if np.any(mask_deplaces):
        distances_modifiees = distances_m[mask_deplaces]
        
        dep_min = distances_modifiees.min()
        dep_max = distances_modifiees.max() + 1e-6
        
        dep_norm = (distances_modifiees - dep_min) / (dep_max - dep_min)
        
        cmap = plt.get_cmap("YlOrRd")
        couleurs_heatmap = cmap(dep_norm)[:, :3]
        
        couleurs[mask_deplaces] = couleurs_heatmap
        
        print(f"-> {np.sum(mask_deplaces)} points ont bougé de place !")
        print(f"-> Déplacement maximal : {dep_max:.2f} mètres.")

    xyz = points_brouillard[:, :3]
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(xyz)
    pcd.colors = o3d.utility.Vector3dVector(couleurs)
    
    nom_sortie = fichier_bin.replace('.bin', f'_FOG_deplacement_alpha_{alpha}.ply').replace("lidar_hdl64_strongest", "plot_modification")
    o3d.io.write_point_cloud(nom_sortie, pcd)
    print(f"Fichier sauvegardé : {nom_sortie}")

