from flask import Flask, render_template, request, jsonify
from spotifyapi import get_top_tracks_by_genre
from lastfmapi import get_artist_info, get_top_tracks, get_top_album, get_global_top_tracks_html
import dezzerapi  # Importamos el archivo de Deezer

app = Flask(__name__)

@app.route("/")
def home():
    # Obtener las canciones más populares globalmente desde Last.fm
    global_top_tracks = get_global_top_tracks_html(limit=4)
    
    # Obtener los artistas más populares desde Deezer
    top_artists = dezzerapi.get_top_artists()  # Llamamos a la función del archivo Deezer
    
    return render_template("index.html", global_top_tracks=global_top_tracks, top_artists=top_artists)

@app.route("/artist", methods=["POST"])
def artist():
    # Obtener el nombre del artista desde el formulario
    artist_name = request.form.get("artist_name")
    
    if not artist_name:
        return jsonify({"error": "Debe ingresar un nombre de artista."})

    # Obtener información del artista desde la API de Last.fm
    biography, listeners = get_artist_info(artist_name)
    top_tracks = get_top_tracks(artist_name)
    top_album = get_top_album(artist_name)

    # Enviar los datos como respuesta JSON
    return jsonify({
        "artist": artist_name,
        "biography": biography,
        "listeners": listeners,
        "top_tracks": top_tracks,
        "top_album": top_album
    })

@app.route("/genre", methods=["POST"])
def genre():
    # Obtener el género desde el formulario
    genre_name = request.form.get("genre_name")
    
    if not genre_name:
        return jsonify({"error": "Debe ingresar un género."})

    # Obtener las canciones principales del género desde la API de Spotify
    genre_data = get_top_tracks_by_genre(genre_name)

    return jsonify(genre_data)

if __name__ == "__main__":
    app.run(debug=True)
    
    
