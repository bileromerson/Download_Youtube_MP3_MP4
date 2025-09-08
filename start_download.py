from configs import out_folder, artists_urls, allow_duplicate_downloads 
from download_list import *
import time
import os
import sys
try:
    print('Escolha o formato de download: \n   [1] MP3\n   [2] MP4\n')
    choice = input('INPUT>> ')
    for artist, urls in artists_urls.items():
        # Define o caminho da pasta para o artista, usando o diretório de saída
        artist_output_folder = f'{out_folder}/{artist}'
        os.makedirs(artist_output_folder, exist_ok=True)
        print(f"--- Iniciando downloads para {artist} ---")
        # Adicione este loop para iterar sobre CADA URL na lista 'urls'

        for url in urls:
            if choice == '1':
                if allow_duplicate_downloads == False:
                    baixar_audio(url, artist_output_folder)
                elif allow_duplicate_downloads == True:
                    baixar_audio_igual(url, artist_output_folder)
                else:
                    print(f'[ERRO] var permitir_downloads_iguais = {allow_duplicate_downloads}. invalid text')
                    sys.exit()
            elif choice == '2':
                if allow_duplicate_downloads == False:
                    baixar_video(url, artist_output_folder)
                elif allow_duplicate_downloads == True:
                    baixar_video_igual(url, artist_output_folder) 
                else:
                    print(f'[ERRO] var permitir_downloads_iguais = {allow_duplicate_downloads}. invalid text')
                    sys.exit()

        print(f"--- Todos os downloads para {artist} foram processados. ---")
except KeyboardInterrupt:
    print('\nstoping', end='', flush=True)
    for _ in range(3):  # 3 pontos = 1500ms, ajuste se quiser mais tempo
        print('.', end='', flush=True)
        time.sleep(0.5)
    print()  # quebra de linha ao final
    sys.exit()