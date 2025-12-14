# Downloader de áudio e vídeo do YouTube

![Status Badge](https://img.shields.io/badge/status-BETA-yellow)
![License Badge](https://img.shields.io/badge/license-MIT-orange)

## 📄 um simples download de listas de músicas MP3 ou MP4 em python, feito para ser simples de usar e prático

Este projeto é um script Python desenvolvido para baixar áudio e vídeo do YouTube (vídeos ou playlists) e convertê-los para o formato MP3 ou MP4 e salvando a mídia conforme definido nas configuracoes.

O script utiliza a biblioteca `yt-dlp` para realizar os downloads, permitindo alto nível de customização e confiabilidade.

## ✨ Recursos

- **Baixa mídia de URLs do YouTube**: Suporta URLs de vídeos e listas de reprodução.
- **Conversão de MP3 e MP4**: Converte arquivos baixados para o formato MP3 ou MP4 de acordo com sua escolha.
- **Organização por Artista**: Salva arquivos de mídia em pastas com o nome do artista, de acordo com sua configuração.
- **Controle de download duplicado**: oferece opções para lidar com arquivos que já existem: [!BETA!]
    - **Modo Padrão (`allow_duplicate_downloads = False`)**: substitui o download caso já exista arquivo na pasta de destino, evitando duplicações desnecessárias. 
    - **Modo Múltiplo (`allow_duplicate_downloads = True`)**: Acrescenta um contador ao final do nome do arquivo (por exemplo, `filename_1.mp3`) para permitir vários downloads do mesmo título.
- **Miniaturas**: Opção para baixar e incorporar a miniatura do vídeo no arquivo de mídia.
- **Controle de qualidade**: Permite definir a qualidade de áudio ou vídeo desejada.
    -**Audio (`audio_quality`)**: exemplo: `audio_quality = '120'`
    -**Video (`video_quality`)**: exemplo: `video_quality = '1080'`
    -**Fps (`fps`)**: exemplo: `fps = '60'`
- **Controle de metadados**: permite incorporar seletivamente metadados (artista, título, álbum).
- **Configuração Fácil**: Todas as opções de download, como qualidade e URLs, são gerenciadas centralmente no arquivo `configs.py`.

## ⚙️ Requisitos

Para executar este script, você precisa ter **Python 3.13**, **FFmpeg** e **eyed3** instalados em sua máquina.

### 🐍 Python 3.13
- Verifique sua versão do Python com o comando:
```bash
python --versão

- **Downloads media from YouTube URLs**: Supports both video and playlist URLs.
- **MP3 and MP4 Conversion**: Converts downloaded files to either MP3 or MP4 format based on your choice.  ** 
- **Organization by Artist**: Saves media files into folders named after the artist, according to your configuration.
- **Duplicate Download Control**: Offers two options for handling files that already exist:
    - **Standard Mode (`allow_duplicate_downloads = False`)**: replace the download if a file already exists in the destination folder, avoiding unnecessary duplication.
    - **Multiple Mode (`allow_duplicate_downloads = True`)**: Appends a counter to the end of the filename (e.g., `filename_1.mp3`) to allow for multiple downloads of the same title.
- **Thumbnails**: Option to download and embed the video thumbnail into the media file.
- **Quality Control**: Allows you to set the desired audio or video quality, recommended(e.g., `320` for MP3 or `720` for MP4).
- **Metadata Control**: Allows you to selectively embed metadata (artist, title, album).
- **Easy Configuration**: All download options, like quality and URLs, are centrally managed in the `configs.py` file.

## ⚙️ Requirements

To run this script, you need to have **Python 3.13**, **FFmpeg** and **eyed3** installed on your machine.

### 🐍 Python 3.13
- Check your Python version with the command:
```bash
python --version