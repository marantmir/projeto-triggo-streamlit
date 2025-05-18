import pandas as pd
import os
import kagglehub

def load_data():
    # Baixar dataset automaticamente
    path = kagglehub.dataset_download("olistbr/brazilian-ecommerce")
    print(f"Dataset baixado em: {path}")

    # Carregar todos os CSVs na pasta
    all_files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.csv')]

    dfs = {}
    for file in all_files:
        filename = os.path.basename(file).replace(".csv", "")
        try:
            dfs[filename] = pd.read_csv(file)
            print(f"✅ Carregado: {filename}")
        except Exception as e:
            print(f"❌ Erro ao carregar {filename}: {e}")

    return dfs
