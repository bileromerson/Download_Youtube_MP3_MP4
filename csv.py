import yt_dlp
import os
import csv


from configs import out_folder, artists_urls
artist = list(artists_urls.keys())[0]  # Get the first artist name
artist_output_folder = f'{out_folder}/{artist}'

print(artist_output_folder)


try:
    ydl_opts = {
        'outtmpl': f'{artist_output_folder}/%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

except Exception as e:
    print(f"Ocorreu um erro: {e}")