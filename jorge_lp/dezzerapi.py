import requests

def get_top_artists():
    # Endpoint de la API de Deezer para obtener los artistas más escuchados
    url = "https://api.deezer.com/chart/0/artists"

    # Hacer la solicitud
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        
        # Obtener la lista de los 6 artistas más escuchados
        top_artists = data.get("data", [])[:6]
        
        # Devolver solo el nombre y la imagen de cada artista
        artists_info = [
            {"name": artist.get("name"), "picture": artist.get("picture")}
            for artist in top_artists
        ]
        return artists_info
    else:
        print(f"Error al obtener los datos: {response.status_code}")
        return []
