from configs import out_folder, artists_urls, allow_duplicate_downloads 
from download_list import download
import os
import sys
import time 

try:
    print('Escolha o formato de download: \n   [1] MP3\n   [2] MP4\n')
    choice = input('INPUT>> ')

    for artist, urls in artists_urls.items():
        # Define o caminho da pasta para o artista, usando o diretório de saída
        artist_output_folder = f'{out_folder}/{artist}'
        os.makedirs(artist_output_folder, exist_ok=True)
        print(f"----- Iniciando downloads para {artist} -----")

        for url in urls:
            print(f"--- mais um de {artist} ---")
            download(url, artist_output_folder, choice)
        print(f"--- Todos os downloads para {artist} foram processados. ---")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

except KeyboardInterrupt:
    for _ in range(3):
        print('.', end='', flush=True)
        time.sleep(0.5)
    print()
    sys.exit()