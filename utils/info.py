import yt_dlp

def obter_info_video(url):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'extract_flat': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            # Retorna um dicionário com tudo sobre o link
            return ydl.extract_info(url, download=False)
        except Exception as e:
            print(f"Erro ao obter informações: {e}")
            return None

def processar_dados(info):
    """Exemplo de como navegar no dicionário 'info'"""
    if not info:
        return

    # Se for playlist, 'entries' conterá a lista de vídeos
    if 'entries' in info:
        nome = info.get('title')
        qtd_videos = len(info.get('entries', []))
        print(f"Playlist Detectada: {nome} ({qtd_videos} vídeos)")
    else:
        # Se for vídeo único
        titulo = info.get('title')
        canal = info.get('uploader')
        duracao = info.get('duration') # em segundos
        print(f"Vídeo: {titulo} | Canal: {canal} | Duração: {duracao}s")

def tem_audio_dublado(info):
    """Verifica se existem múltiplas faixas de áudio (dublagem)"""
    formats = info.get('formats', [])
    # Filtra formatos que possuem tag de idioma e são apenas áudio
    idiomas = set(f.get('language') for f in formats if f.get('language'))
    print(list(idiomas) if idiomas else ["Original"])
    return list(idiomas) if idiomas else ["Original"]

def listar_legendas_disponiveis(info):
    """
    Analisa o dicionário de informações e mostra o que o vídeo oferece.
    """
    if not info:
        return

    # 1. Legendas enviadas por humanos (Manuais)
    manuais = info.get('subtitles', {})
    
    # 2. Legendas geradas por IA (Automáticas/Traduzidas)
    automaticas = info.get('automatic_captions', {})

    print(f"\n--- Legendas para: {info.get('title')} ---")
    
    if manuais:
        print(f"Manuais encontradas: {', '.join(manuais.keys())}")
    else:
        print("Nenhuma legenda manual disponível.")

    if automaticas:
        # Mostramos apenas as 5 primeiras para não encher a tela, 
        # já que o YouTube oferece tradução para quase todas as línguas.
        idiomas = list(automaticas.keys())
        print(f"Automáticas/Traduções disponíveis ({len(idiomas)} idiomas): {', '.join(idiomas[:5])}...")
    
    print("-" * 40)

# processar_dados(obter_info_video('https://www.youtube.com/watch?v=qFsj6KL8_nU'))

# tem_audio_dublado(obter_info_video('https://www.youtube.com/watch?v=qFsj6KL8_nU'))

listar_legendas_disponiveis(obter_info_video('https://www.youtube.com/watch?v=qFsj6KL8_nU'))
