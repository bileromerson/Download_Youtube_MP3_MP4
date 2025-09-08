from configs import out_folder, list, permitir_downloads_iguais
from download_list import baixar_audio, baixar_audio_igual
import os
import sys

for artista, urls in list.items():
    # Define o caminho da pasta para o artista, usando o diretório de saída
    caminho_pasta_artista = f'{out_folder}/{artista}'
    os.makedirs(caminho_pasta_artista, exist_ok=True)
    print(f"--- Iniciando downloads para {artista} ---")
    # Adicione este loop para iterar sobre CADA URL na lista 'urls'
    for url in urls:
        if permitir_downloads_iguais == False:
            baixar_audio(url, caminho_pasta_artista)
        elif permitir_downloads_iguais == True:
            baixar_audio_igual(url, caminho_pasta_artista)
        else:
            print(f'[ERRO] var permitir_downloads_iguais = {permitir_downloads_iguais}. invalid text')
            sys.exit()
    print(f"--- Todos os downloads para {artista} foram processados. ---")
    