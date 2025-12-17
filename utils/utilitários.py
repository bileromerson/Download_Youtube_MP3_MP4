

    
# verifica se o link leva a uma playlist
def is_playlist(url: str) -> bool:
    from urllib.parse import urlparse, parse_qs

    query = parse_qs(urlparse(url).query)
    return bool(query.get("list", [""])[0].strip())


# pega o id da url
def playlist_id_from_url(url: str) -> str | None:
    from urllib.parse import urlparse, parse_qs

    query = parse_qs(urlparse(url).query)
    return query.get("list", [None])[0]

# conta quantos videos tem em uma playlist
def count_playlist_pytube(url: str) -> int:
    from pytube import Playlist

    pid = playlist_id_from_url(url)
    if not pid:
        raise ValueError("URL não contém parâmetro 'list'")
    p = Playlist(url)
    return sum(1 for _ in p.video_urls)


# pega o nome da playlist
def playlist_name_pytube(url: str) -> str | None:
    from pytube import Playlist
    
    pid = playlist_id_from_url(url)
    if not pid:
        raise ValueError("URL não contém parâmetro 'list'")
    p = Playlist(url)
    try:
        return p.title
    except Exception:
        return None
    

# pega o nome do video
def video_name_pytube(url: str, raise_on_error: bool = False) -> str | None:
    from pytube import YouTube
    import requests

    # primeira tentativa: pytube
    try:
        yt = YouTube(url)
        title = yt.title if isinstance(yt.title, str) and yt.title.strip() else None
    except Exception:
        if raise_on_error:
            raise
        title = None

    if title:
        return title

    # fallback: oEmbed público do YouTube (não requer API key)
    try:
        r = requests.get("https://www.youtube.com/oembed", params={"url": url, "format": "json"}, timeout=5)
        r.raise_for_status()
        data = r.json()
        return data.get("title")
    except Exception:
        if raise_on_error:
            raise
        return None
    

# pega os titulos da playlist
def playlist_titles_pytube(url: str, skip_unavailable: bool = True) -> list[str | None]:
    """Retorna lista de títulos (None para vídeos indisponíveis)."""
    from pytube import Playlist, YouTube
    import requests

    pid = playlist_id_from_url(url)
    if not pid:
        raise ValueError("URL não contém parâmetro 'list'")
    p = Playlist(url)
    titles: list[str | None] = []
    for vid_url in p.video_urls:
        title: str | None = None

        # tentativa com pytube
        try:
            yt = YouTube(vid_url)
            t = yt.title
            if isinstance(t, str) and t.strip():
                title = t.strip()
        except Exception:
            if not skip_unavailable:
                raise
            title = None

        # fallback: oEmbed público
        if title is None:
            try:
                r = requests.get("https://www.youtube.com/oembed", params={"url": vid_url, "format": "json"}, timeout=5)
                r.raise_for_status()
                data = r.json()
                t = data.get("title")
                if isinstance(t, str) and t.strip():
                    title = t.strip()
            except Exception:
                if not skip_unavailable:
                    raise
                title = None

        titles.append(title)
    return titles

# url = "https://www.youtube.com/watch?v=E2lZ51VIJ9o&list=OLAK5uy_kv12hbd29HJuL7A_v_dpSUOcJnfQeW57Y"# onli for tests :3
# print(is_playlist(url))
# print(playlist_id_from_url(url))
# print(count_playlist_pytube(url))
# print(playlist_name_pytube(url))
# print(video_name_pytube(url))
# print(playlist_titles_pytube(url))