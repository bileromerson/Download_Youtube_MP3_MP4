

# from utils.info import*
from configs import*
import yt_dlp
import time
import sys

def download(url, folder, choice):
    try:

    # --------------------- configs ---------------------
    
        ydl_opts = {
            'sleep_interval': 5,          # Espera 5 segundos entre cada download
            'max_sleep_interval': 10,     # Pode esperar até 10 segundos se o YouTube reclamar
            # 'sleep_interval_subtitles': 2,
            'noprogress': not show_progress,
            'quiet': False,
            'nologger': False,
            'writethumbnail': download_thumbnail,
            'writesubtitles':True,
            'writeautomaticsub': True, # mais
            # 'subtitlesformat': 'srt/vtt/best',
            'subtitleslangs': ['en'],
            'outtmpl': f'{folder}/%(title)s.%(ext)s',
        }

        mp4_opts = {
            # 'skip_download': True,
            'format': f'bestvideo[height<={video_quality}][fps<={fps}]+bestaudio[abr<={audio_quality}][language*={audio_lenguege}]/best',
            'already_have_subtitle': False,
            'postprocessors': [
            {
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            },
        #     {
        #         'key': 'FFmpegSubtitlesConvertor',
        #         'format': 'srt',
        #     },
        #     {
        #     'key': 'FFmpegEmbedSubtitle',
        #     'already_have_subtitle': False,
        #     },{
        #     'key': 'FFmpegMetadata',
        #     'add_metadata': True,
        # }
        ],
        }

        mp3_opts = {
            # 'skip_download': True,
            'format': f'bestaudio[abr<={audio_quality}][language*={audio_lenguege}]/best',

            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }],
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
        # if have_subtitle:
        #     ydl_opts['postprocessors'].append({'key': 'FFmpegEmbedSubtitle',})
        
        
        # --------------------- INFOS ---------------------

        # --------------------- DOWNLOAD ---------------------

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        
            if choice == '1':
                print("Baixando apenas o Audio...")
            elif choice == '2':
                print("Baixando Video...")

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
