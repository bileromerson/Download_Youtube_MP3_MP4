import csv
import yt_dlp
from urllib.parse import urlparse, parse_qs
from configs import artists_urls  # Certifique-se de que este módulo existe

# -------- extrai ID do YouTube ----------
def get_video_id(url):
    parsed = urlparse(url)
    if "youtu.be" in parsed.netloc:
        return parsed.path[1:]
    params = parse_qs(parsed.query)
    return params.get("v", [None])[0]

# -------- pega IDs da base / playlists ----------
def coletar_ids():
    print("Expandindo playlists...")
    todos_ids = set()
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
    }

    for artista, urls in artists_urls.items():
        for url in urls:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                try:
                    info = ydl.extract_info(url, download=False)
                    if 'entries' in info:  # É uma playlist
                        ids = [get_video_id(e['webpage_url']) for e in info['entries'] if e.get('webpage_url')]
                    else:  # É vídeo único
                        vid = get_video_id(info['webpage_url'])
                        ids = [vid] if vid else []
                    todos_ids.update(ids)
                except Exception as e:
                    print(f"Erro ao processar {url}: {e}")
                    continue
    return todos_ids

# -------- pega IDs do CSV ----------
def ler_csv(caminho):
    ids = set()
    with open(caminho, encoding='utf-8-sig') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            vid = get_video_id(linha['url'])
            if vid:
                ids.add(vid)
    return ids

# -------- EXECUÇÃO ----------
config_ids = coletar_ids()
csv_ids = ler_csv('csvs/Alone.csv')

iguais = config_ids & csv_ids
so_no_csv = csv_ids - config_ids
so_na_base = config_ids - csv_ids

print("\n📊 RELATÓRIO\n")
print("Base:", len(config_ids))
print("CSV:", len(csv_ids))
print("Iguais:", len(iguais))
print("Só no CSV:", len(so_no_csv))
print("Só na base:", len(so_na_base))

print("\n🔥 Músicas no CSV que NÃO estão na sua base:\n")
for vid in so_no_csv:
    print(f"https://youtube.com/watch?v={vid}")