# YouTube Audio and Video Downloader

![Status Badge](https://img.shields.io/badge/status-Active-brightgreen)
![License Badge](https://img.shields.io/badge/license-MIT-orange)

## 📄 a simple download of MP3 or MP4 music lists in python, made to be simple to use and practical

This project is a Python script designed to download audio and video from YouTube (videos or playlists) and convert them to the MP3 or MP4 format. It's ideal for organizing your media library by saving the files into separate folders by artist, as defined in a configuration file.

The script uses the powerful `yt-dlp` library to perform the downloads, allowing for a high level of customization and reliability.

## ✨ Features

- **Downloads media from YouTube URLs**: Supports both video and playlist URLs.
- **MP3 and MP4 Conversion**: Converts downloaded files to either MP3 or MP4 format based on your choice.
- **Organization by Artist**: Saves media files into folders named after the artist, according to your configuration.
- **Duplicate Download Control**: Offers two options for handling files that already exist:
    - **Standard Mode (`allow_duplicate_downloads = False`)**: Skips the download if a file already exists in the destination folder, avoiding unnecessary duplication.
    - **Multiple Mode (`allow_duplicate_downloads = True`)**: Appends a counter to the end of the filename (e.g., `filename_1.mp3`) to allow for multiple downloads of the same title.
- **Thumbnails**: Option to download and embed the video thumbnail into the media file.
- **Quality Control**: Allows you to set the desired audio or video quality, recommended(e.g., `320` for MP3 or `720` for MP4).
- **Easy Configuration**: All download options, like quality and URLs, are centrally managed in the `configs.py` file.

## ⚙️ Requirements

To run this script, you need to have **Python 3.13** and **FFmpeg** installed on your machine.

### 🐍 Python 3.13
- Check your Python version with the command:
```bash
python --version