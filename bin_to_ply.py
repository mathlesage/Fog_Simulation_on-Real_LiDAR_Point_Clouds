import numpy as np
import open3d as o3d
import os

data_dir = r"data\lidar_hdl64_strongest"

fichiers_bin = [
    "2018-02-12_08-56-38_00200.bin",
    "2018-02-12_12-27-11_00400.bin",
    "2018-02-12_16-58-00_00050.bin",
    "2018-03-15_09-40-42_00000.bin",
    "2018-03-15_09-50-52_00400.bin",
    "2018-12-09_10-28-11_01000.bin",
    "2018-12-09_11-23-03_01500.bin",
    "2018-12-12_09-34-31_03300.bin"

]
data_out = r"data/nuage_classique"

for nom_fichier in fichiers_bin:
    chemin_bin = os.path.join(data_dir, nom_fichier)
    data_dir_ply = data_dir + "_ply"
    chemin_ply = os.path.join(data_out, nom_fichier)
    chemin_ply = chemin_ply.replace('.bin', '.ply')
    
    if not os.path.exists(chemin_bin):
        print(f"Fichier introuvable : {nom_fichier}")
        continue
        
    print(f"Conversion de {nom_fichier} ...")
    
    points = np.fromfile(chemin_bin, dtype=np.float32).reshape(-1, 5)
    xyz = points[:, :3]
    
    intensite = points[:, 3]
    intensite_norm = np.clip(intensite / 255.0, 0, 1)
    couleurs = np.column_stack((intensite_norm, intensite_norm, intensite_norm))

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(xyz)
    pcd.colors = o3d.utility.Vector3dVector(couleurs)
    
    o3d.io.write_point_cloud(chemin_ply, pcd)
    print(f"Sauvegardé : {chemin_ply}")

