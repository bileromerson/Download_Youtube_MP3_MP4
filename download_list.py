from configs import *
import os
import yt_dlp
from time import sleep
import sys

def baixar_audio(url, out_folder_artist):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            # 'outtmpl': outtmpl,
            'writethumbnail': baixar_tumbnail,
            
            # A opção 'embedthumbnail' instrui o yt-dlp a baixar a miniatura do vídeo
            'embedthumbnail': baixar_tumbnail,
            'quiet': True,
            'noprogress': not mostrar_progreso,
            'postprocessors': [{
                # Este post-processor extrai o áudio e o converte para MP3
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': Qualidade,
            }, {
                # Este post-processor usa o FFmpeg para embutir a miniatura
                'key': 'EmbedThumbnail',
            }],
            
            # O modelo de saída para o nome do arquivo
            'outtmpl': f'{out_folder_artist}/%(title)s.%(ext)s',
            'parse_metadata': {'artist': '%(artist)s'}
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:

            print('entrando na URL:',url)
            print("Baixando apenas o áudio...")
            ydl.download([url])
            print("Download e conversão para MP3 concluídos!")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    except KeyboardInterrupt:
        print('stoping...')
        sleep(1.5)
        sys.exit()

def baixar_audio_igual(url, out_folder_artist):
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
        while os.path.exists(f'{out_folder_artist}/{final_filename}.mp3'):
            final_filename = f"{sanitized_filename}_{counter}"
            # Atualiza a variável que será usada na próxima verificação
            # Você pode usar um formato como "nome_do_arquivo_1.mp3" ou "(1)nome_do_arquivo.mp3"
            counter += 1
    
        print(f"O nome do arquivo final será: '{final_filename}.mp3'")
            
        # Passo 1: Extrair informações do vídeo, focando no título e ID
        ydl_opts = {
            'format': 'bestaudio/best',
            # O modelo de saída para o nome do arquivo
            'outtmpl': os.path.join(out_folder_artist, final_filename),
            # 'outtmpl': outtmpl,
            'writethumbnail':  baixar_tumbnail,
            
            # A opção 'embedthumbnail' instrui o yt-dlp a baixar a miniatura do vídeo
            'quiet': True,
            'noprogress': not mostrar_progreso,
            'postprocessors': [{
                # Este post-processor extrai o áudio e o converte para MP3
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': Qualidade,
            },{
                # Este post-processor usa o FFmpeg para embutir a miniatura
                'key': 'EmbedThumbnail',   
            }],
        }
                
        print('Iniciando o download...')
        with yt_dlp.YoutubeDL(ydl_opts) as ydl_download:
            print('entrando na URL:',url)
            ydl_download.download([url])
        
        print("Download e conversão para MP3 concluídos!")

    except Exception as e:
        print(f"\nOcorreu um erro: {e}")
    except KeyboardInterrupt:
        print('stoping...')
        sleep(1.5)
        sys.exit()

# Loop principal para iterar sobre os artistas e suas URLs
