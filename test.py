

from flask import Flask, Response, render_template, request
import youtube_dl

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('front.html')

@app.route('/audio_stream', methods=['POST'])
def audio_stream():
    print("audio_stream called")
    url = request.form['url']
    # Your code to stream audio from the URL goes here
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        song_info = ydl.extract_info(url, download=False)
        audio_url = song_info['url']
    return Response(audio_url, mimetype='audio/mpeg')
    #return 'Audio stream started'

if __name__ == '__main__':
    app.run(debug=True)