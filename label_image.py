import os
import json
import csv

input_folder = r"C:\Users\USER\datasets\DENSE\SeeingThroughFog\labeltool_labels_refined"
output_csv = r"data/inventaire_meteo.csv"

def extraire_meteo_stf():
    resultats = []
    
    fichiers = [f for f in os.listdir(input_folder) if f.endswith('.json')]
    print(f"Analyse de {len(fichiers)} fichiers en cours...")

    for nom_fichier in fichiers:
        chemin_complet = os.path.join(input_folder, nom_fichier)
        
        try:
            with open(chemin_complet, 'r', encoding='utf-8') as f:
                data = json.load(f)
                condition = "clair"
                fog_data = data.get('fog', {})
                if fog_data.get('yes'):
                    details = fog_data['yes']
                    if details.get('denseFog'):
                        condition = "brouillard dense"
                    elif details.get('lightFog'):
                        condition = "brouillard léger"
                
                precip = data.get('precipitation', {})
                if condition == "clair" and precip.get('yes'):
                    details = precip['yes']
                    if details.get('rain'):
                        condition = "pluie"
                    elif details.get('snow'):
                        if details['snow'].get('heavySnow') or details['snow'].get('lightSnow'):
                            condition = "neige"

                moment = "jour"
                if data.get('daytime', {}).get('night'):
                    moment = "nuit"

                resultats.append({
                    'nom_fichier': nom_fichier.replace('.json', '.bin'),
                    'condition_meteo': condition,
                    'moment': moment
                })
        except Exception as e:
            print(f"Erreur sur {nom_fichier}: {e}")

    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['nom_fichier', 'condition_meteo', 'moment']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in resultats:
            writer.writerow(row)

    print(f"Terminé ! Ton inventaire est prêt : {output_csv}")

if __name__ == "__main__":
    extraire_meteo_stf()