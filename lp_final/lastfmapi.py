import requests

API_KEY = "05284d5e90ad5ad116c3b2e50916d0c3"  # Sustituye con tu clave de API de Last.fm
BASE_URL = "http://ws.audioscrobbler.com/2.0/"

def get_artist_info(artist_name):
    """
    Obtiene la biografía del artista en español y su número de oyentes en Last.fm.
    """
    params = {
        "method": "artist.getinfo",
        "artist": artist_name,
        "api_key": API_KEY,
        "format": "json",
        "lang": "es"  # Solicitar la biografía en español
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    if 'artist' in data:
        biography = data['artist']['bio']['summary']
        listeners = data['artist']['stats']['listeners']
        return biography, listeners
    else:
        return None, None

def get_top_tracks(artist_name, limit=10):
    """
    Obtiene las canciones más escuchadas del artista (hasta un máximo de limit).
    """
    params = {
        "method": "artist.gettoptracks",
        "artist": artist_name,
        "api_key": API_KEY,
        "format": "json",
        "limit": limit
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    if 'toptracks' in data and data['toptracks']['track']:
        top_tracks = [track['name'] for track in data['toptracks']['track']]
        return top_tracks
    else:
        return None

def get_top_album(artist_name):
    """
    Obtiene el álbum más famoso del artista.
    """
    params = {
        "method": "artist.gettopalbums",
        "artist": artist_name,
        "api_key": API_KEY,
        "format": "json"
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    if 'topalbums' in data and data['topalbums']['album']:
        top_album = data['topalbums']['album'][0]['name']
        return top_album
    else:
        return None

# Ejemplo de uso
if __name__ == "__main__":
    artist_name = "Coldplay"  # Sustituye con el nombre del artista que desees
    
    biography, listeners = get_artist_info(artist_name)
    top_tracks = get_top_tracks(artist_name)
    top_album = get_top_album(artist_name)
    
    print(f"Artista: {artist_name}")
    print(f"Biografía: {biography}")
    print(f"Oyentes en Last.fm: {listeners}")
    print("10 canciones más escuchadas:")
    if top_tracks:
        for i, track in enumerate(top_tracks, start=1):
            print(f"  {i}. {track}")
    print(f"Álbum más famoso: {top_album}")