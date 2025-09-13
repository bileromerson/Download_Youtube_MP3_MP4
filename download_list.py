from configs import *
import os
import yt_dlp
import time
from time import sleep
import sys



def baixar_audio(url, artist_output_folder):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'noprogress': not show_progress,
            'postprocessors': [{
                # Este post-processor extrai o áudio e o converte para MP3
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': quality,
            }],
            'writethumbnail': download_thumbnail,
            'outtmpl': f'{artist_output_folder}/%(title)s.%(ext)s',
        }
        
        if Metadata:
            ydl_opts['postprocessors'].append({'key': 'FFmpegMetadata',})
        if download_thumbnail:
            ydl_opts['postprocessors'].append({'key': 'EmbedThumbnail',})
        
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

def baixar_audio_igual(url, artist_output_folder):
    try:
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
        while os.path.exists(f'{artist_output_folder}/{final_filename}.mp3'):
            final_filename = f"{sanitized_filename}_{counter}"
            # Atualiza a variável que será usada na próxima verificação
            # Você pode usar um formato como "nome_do_arquivo_1.mp3" ou "(1)nome_do_arquivo.mp3"
            counter += 1
    
        print(f"O nome do arquivo final será: '{final_filename}.mp3'")
            
        # Passo 1: Extrair informações do vídeo, focando no título e ID
        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'noprogress': not show_progress,
            'postprocessors': [{
                # Este post-processor extrai o áudio e o converte para MP3
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': quality,
            }],
            # A opção 'embedthumbnail' instrui o yt-dlp a baixar a miniatura do vídeo
            'writethumbnail':  download_thumbnail,
            # O modelo de saída para o nome do arquivo
            'outtmpl': os.path.join(artist_output_folder, final_filename + '.%(ext)s'),
        }
        if download_thumbnail:
            ydl_opts['postprocessors'].append({'key': 'EmbedThumbnail',})
        if Metadata:
            ydl_opts['postprocessors'].append({'key': 'FFmpegMetadata',})

        print('Iniciando o download...')
        with yt_dlp.YoutubeDL(ydl_opts) as ydl_download:
            print('entrando na URL:',url)
            ydl_download.download([url])
        
        print("Download e conversão para MP3 concluídos!")

    except Exception as e:
        print(f"\nOcorreu um erro: {e}")
    except KeyboardInterrupt:
        print('\nstoping', end='', flush=True)
        for _ in range(3):  # 3 pontos = 1500ms, ajuste se quiser mais tempo
            print('.', end='', flush=True)
            time.sleep(0.5)
        print()  # quebra de linha ao final
        sys.exit()

def baixar_video(url, artist_output_folder):
    try:
        # Define o formato de vídeo baseado na qualidade desejada
        ydl_opts = {
            'format': f'bestvideo[height<={quality}]+bestaudio/best/best',
            'quiet': True,
            'noprogress': not show_progress,
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',  # converte para mp4
            }],
            'writethumbnail': download_thumbnail,
            # O modelo de saída para o nome do arquivo
            'outtmpl': f'{artist_output_folder}/%(title)s.%(ext)s',
        }
        if download_thumbnail:
            ydl_opts['postprocessors'].append({'key': 'EmbedThumbnail',})
        if Metadata:
            ydl_opts['postprocessors'].append({'key': 'FFmpegMetadata',})

        print('entrando na URL:', url)
        print(f"Baixando vídeo na qualidade até {quality}p...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download e conversão para MP4 concluídos!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    except KeyboardInterrupt:
        print('\nstoping', end='', flush=True)
        for _ in range(3):  # 3 pontos = 1500ms, ajuste se quiser mais tempo
            print('.', end='', flush=True)
            time.sleep(0.5)
        print()  # quebra de linha ao final
        sys.exit()

def baixar_video_igual(url, artist_output_folder):
    try:
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
        while os.path.exists(f'{artist_output_folder}/{final_filename}.mp4'):
            final_filename = f"{sanitized_filename}_{counter}"
            # Atualiza a variável que será usada na próxima verificação
            # Você pode usar um formato como "nome_do_arquivo_1.mp4" ou "(1)nome_do_arquivo.mp4"
            counter += 1
        print(f"O nome do arquivo final será: '{final_filename}.mp4'")
            # Define o formato de vídeo baseado na qualidade desejada
        ydl_opts = {
            'format': f'bestvideo[height<={quality}]+bestaudio/best/best',
            'quiet': True,
            'nologger': True,
            'noprogress': not show_progress,
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',  # converte para mp4
            }, {
                'key': 'EmbedThumbnail',
            }],
            'writethumbnail': download_thumbnail,
            # O modelo de saída para o nome do arquivo
            'outtmpl': os.path.join(artist_output_folder, final_filename)
        }
        if download_thumbnail:
            ydl_opts['postprocessors'].append({'key': 'EmbedThumbnail',})
        if Metadata:
            ydl_opts['postprocessors'].append({'key': 'FFmpegMetadata',})

        print('entrando na URL:', url)
        print(f"Baixando vídeo na qualidade até {quality}p...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download e conversão para MP4 concluídos!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    except KeyboardInterrupt:
        print('\nstoping', end='', flush=True)
        for _ in range(3):  # 3 pontos = 1500ms, ajuste se quiser mais tempo
            print('.', end='', flush=True)
            time.sleep(0.5)
        print()  # quebra de linha ao final
        sys.exit()

