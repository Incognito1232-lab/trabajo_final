import requests

# Endpoint de la API de Deezer para obtener los artistas más escuchados
url = "https://api.deezer.com/chart/0/artists"

# Hacer la solicitud
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    
    # Obtener la lista de los 6 artistas más escuchados
    top_artists = data.get("data", [])[:6]
    
    # Mostrar los nombres y URLs de las imágenes
    print("Top 6 artistas más escuchados en Deezer:")
    for i, artist in enumerate(top_artists, start=1):
        name = artist.get("name")
        picture = artist.get("picture")
        print(f"{i}. {name} - Imagen: {picture}")
else:
    print(f"Error al obtener los datos: {response.status_code}")
