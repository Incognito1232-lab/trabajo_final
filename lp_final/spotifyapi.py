import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Configuración de las credenciales
client_id = 'b415dbb34fcc444090fcb5f8d80b035f'
client_secret = '5e94387d48cf4f2e9ffe88bb0859cb2b'
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Función para obtener las 10 canciones más populares de un género
def get_top_tracks_by_genre(genre_name):
    try:
        resultado_busqueda = sp.search(q='genre:' + genre_name, type='track', limit=10)
        if resultado_busqueda['tracks']['items']:
            canciones = [
                track['name'] + " - " + track['artists'][0]['name']
                for track in resultado_busqueda['tracks']['items']
            ]
            return {"genre": genre_name, "tracks": canciones}
        else:
            return {"error": "No se encontraron canciones para el género especificado."}
    except Exception as e:
        return {"error": str(e)}
    
    
    
    
def get_top_albums():
    try:
        # Realizamos una búsqueda de álbumes populares en Spotify
        results = sp.search(q='*', type='album', limit=50)
        
        if results['albums']['items']:
            # Filtramos los 10 primeros álbumes
            albums = []
            for album in results['albums']['items'][:10]:
                albums.append({
                    "name": album['name'],
                    "artist": album['artists'][0]['name'],
                    "release_date": album['release_date'],
                    "album_url": album['external_urls']['spotify'],
                    "cover_image": album['images'][0]['url'] if album['images'] else None
                })
            return {"albums": albums}
        else:
            return {"error": "No se encontraron álbumes populares."}
    except Exception as e:
        return {"error": str(e)}

