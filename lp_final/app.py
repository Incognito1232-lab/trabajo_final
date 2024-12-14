from flask import Flask, render_template, request, jsonify
from spotifyapi import get_top_tracks_by_genre, get_top_albums
from lastfmapi import get_artist_info, get_top_tracks, get_top_album

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_artist', methods=['POST'])
def search_artist():
    artist_name = request.form.get('artist')
    if artist_name:
        biography, listeners = get_artist_info(artist_name)
        top_tracks = get_top_tracks(artist_name)
        top_album = get_top_album(artist_name)
        return jsonify({
            "biography": biography,
            "listeners": listeners,
            "top_tracks": top_tracks,
            "top_album": top_album
        })
    return jsonify({"error": "Debes ingresar un nombre de artista."})

@app.route('/search_genre', methods=['POST'])
def search_genre():
    genre = request.form.get('genre')
    if genre:
        tracks = get_top_tracks_by_genre(genre)
        return jsonify(tracks)
    return jsonify({"error": "Debes ingresar un nombre de género."})

@app.route('/get_top_albums', methods=['GET'])
def fetch_top_albums():
    albums = get_top_albums()
    return jsonify(albums)

if __name__ == '__main__':
    app.run(debug=True)
