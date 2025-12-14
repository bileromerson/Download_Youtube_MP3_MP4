
from configs import *
import os
import yt_dlp  
import time
import sys

#  --------------------- THIS IS ONLY ONE TEST FUNCTION TO GENERAL DOWNLOADS FOR ONE CODE MORE FAST AND LEGIBLE  ---------------------

def download(url, artist_output_folder, choice):
    try:
        if allow_duplicate_downloads:
                ydl_info_opts = {
                    'skip_download': True,
                    'quiet': True,
                    'noprogress': True,
                    'nologger': True,
                }
                with yt_dlp.YoutubeDL(ydl_info_opts) as ydl_info:
                    info = ydl_info.extract_info(url, download=False)
                    video_title = info.get('title', 'video_sem_titulo')
                    sanitized_filename = "".join(c for c in video_title if c.isalnum() or c in (' ', '.', '_', '-')).strip()
                
                # Inicia o contador para a verificação
                counter = 1
                final_filename = f"{sanitized_filename}"
            
                # Loop para verificar se o arquivo já existe e adicionar um contador se necessário
                while os.path.exists(f'{artist_output_folder}/{final_filename}'):
                    final_filename = f"{sanitized_filename}_{counter}"
                    # Atualiza a variável que será usada na próxima verificação
                    # Você pode usar um formato como "nome_do_arquivo_1.mp3" ou "(1)nome_do_arquivo.mp3"
                    counter += 1
            
                print(f"O nome do arquivo final será: '{final_filename}.mp3'")
    # --------------------- configs ---------------------
    
        ydl_opts = {}

        mp4_opts = {
            'format': f'bestvideo[height<={video_quality}][fps<={fps}]+bestaudio[abr>={audio_quality}]/best',
            'noprogress': not show_progress,
            'quiet': True,
            'nologger': True,
             'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',  # converte para mp4
            }],
            'writethumbnail': download_thumbnail,
            'outtmpl': os.path.join(artist_output_folder, final_filename + '.%(ext)s') if allow_duplicate_downloads else f'{artist_output_folder}/%(title)s.%(ext)s', # se downloads duplicados permitidos entao troca o nome, caso contrario nao
        }

        mp3_opts = {
            'format': f'bestaudio[abr>={audio_quality}]/best', # qualidade
            'noprogress': not show_progress,
            'quiet': True,
            'nologger': True,
            # extrai o áudio e o converte para MP3
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                }],
            'writethumbnail': download_thumbnail,
            'outtmpl': os.path.join(artist_output_folder, final_filename + '.%(ext)s') if allow_duplicate_downloads else f'{artist_output_folder}/%(title)s.%(ext)s', # se downloads duplicados permitidos entao troca o nome, caso contrario nao
        }
        if choice == '1':  # MP3 Download
            ydl_opts.update(mp3_opts)
        elif choice == '2':  # MP4 Download
            ydl_opts.update(mp4_opts)
        else:
            print("Escolha inválida. Por favor, selecione 1 para MP3 ou 2 para MP4.")
            return

        if download_thumbnail:
            ydl_opts['postprocessors'].append({'key': 'EmbedThumbnail',})
        if Metadata:
            ydl_opts['postprocessors'].append({'key': 'FFmpegMetadata',})
        # --------------------- DOWNLOAD ---------------------        
       
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:

            print('entrando na URL:',url)
            print("Baixando apenas o áudio...")
            ydl.download([url])
            print("Download e conversão para MP3 concluídos!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    except KeyboardInterrupt:
        print('\nstoping', end='', flush=True)
        for _ in range(3):  # 3 pontos = 1500ms, ajuste se quiser mais tempo
            print('.', end='', flush=True)
            time.sleep(0.5)
        print()  # quebra de linha ao final
        sys.exit()
