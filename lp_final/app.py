from flask import Flask, render_template
import requests

app = Flask(__name__)

# Endpoint de la API de Deezer para obtener los artistas más escuchados
url = "https://api.deezer.com/chart/0/artists"

# API de Last.fm para obtener las 4 canciones más escuchadas
LASTFM_API_KEY = "05284d5e90ad5ad116c3b2e50916d0c3"
LASTFM_BASE_URL = "http://ws.audioscrobbler.com/2.0/"

def get_global_top_tracks(limit=4):
    """
    Obtiene las 4 canciones más escuchadas globalmente en Last.fm, junto con las URL de las canciones.
    """
    params = {
        "method": "chart.getTopTracks",
        "api_key": LASTFM_API_KEY,
        "format": "json",
        "limit": limit
    }
    response = requests.get(LASTFM_BASE_URL, params=params)
    data = response.json()
    
    if 'tracks' in data and data['tracks']['track']:
        global_top_tracks = []
        for track in data['tracks']['track']:
            name = track['name']
            artist = track['artist']['name']
            url = track['url']  # URL de la canción
            global_top_tracks.append({"name": name, "artist": artist, "url": url})
        return global_top_tracks
    else:
        return None

# Ruta para la página principal
@app.route('/')
def index():
    # Hacer la solicitud a la API de Deezer
    response = requests.get(url)
    top_artists = []

    if response.status_code == 200:
        data = response.json()
        # Obtener la lista de los 6 artistas más escuchados
        top_artists = data.get("data", [])[:6]
    else:
        print(f"Error al obtener los datos de Deezer: {response.status_code}")
    
    # Obtener las 4 canciones más escuchadas globalmente
    top_tracks = get_global_top_tracks()

    return render_template('index.html', top_artists=top_artists, top_tracks=top_tracks)

if __name__ == '__main__':
    app.run(debug=True)
