import os
from kaggle.api.kaggle_api_extended import KaggleApi

def download_dataset(dataset_slug, output_dir="data"):
    api = KaggleApi()
    api.authenticate()
    path = os.path.join(output_dir, dataset_slug.replace("/", "_"))
    os.makedirs(path, exist_ok=True)
    print(f"Descargando {dataset_slug} en {path}...")
    api.dataset_download_files(dataset_slug, path=path, unzip=True)
    print("Descarga completada!")

if __name__ == "__main__":
    download_dataset("manjeetsingh/retaildataset")
    download_dataset("utkalk/large-retail-data-set-for-eda")
