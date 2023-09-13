from flask import Flask, jsonify
from flask_cors import CORS
from models.playlist import Playlist
from models.lecture import Lecture
from models.speaker import Speaker
from models.album import Album

app = Flask(__name__, static_folder='../frontend')
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/lecture/<string:lecture_id>', methods=['GET'])
def get_lecture_by_id(lecture_id):
    try:
        lecture = Lecture.get_by_id(lecture_id)
        return jsonify(lecture.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

@app.route('/speaker/<string:speaker_id>', methods=['GET'])
def get_speaker_by_id(speaker_id):
    try:
        speaker = Speaker.get_by_id(speaker_id)
        return jsonify(speaker.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404
    
    
@app.route('/playlist/<string:playlist_id>', methods=['GET'])
def get_playlist_by_id(playlist_id):
    try:
        playlist = Playlist.get_by_id(playlist_id)
        return jsonify(playlist.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404
    
    
    
@app.route('/album/<string:album_id>', methods=['GET'])
def get_album_by_id(album_id):
    try:
        album = Album.get_by_id(album_id)
        return jsonify(album.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404
    
if __name__ == '__main__':
    app.run(debug=True)