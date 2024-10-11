import requests
import pandas as pd
import gzip
import io

# Fonction téléchargement du fichier compressé
def data_request(input):
    # Base URL
    response = requests.get("https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/adresses-92.csv.gz")
    
    # Requête des données
    if response.status_code == 200:
        # Décompresser le fichier
        with gzip.open(io.BytesIO(response.content), 'rt') as f:
            data = pd.read_csv(f, sep=";")
        data_filtered = data[data["code_insee"] == input].to_dict(orient="records")
    else:
        data_filtered = {"error": response.status_code}

    return data_filtered