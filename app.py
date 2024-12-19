from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    try:
        # Obtém o link do formulário
        video_url = request.form['url']
        
        # Cria o objeto YouTube
        yt = YouTube(video_url)
        
        # Seleciona a melhor stream (MP4 com áudio)
        stream = yt.streams.filter(file_extension='mp4', progressive=True).get_highest_resolution()
        
        # Baixa o vídeo para um diretório temporário
        download_path = stream.download(output_path='downloads/')
        
        # Envia o arquivo para o usuário
        return send_file(download_path, as_attachment=True)
    
    except Exception as e:
        return f'Ocorreu um erro: {e}'

if __name__ == '__main__':
    # Certifique-se de que o diretório "downloads" exista
    os.makedirs('downloads', exist_ok=True)
    app.run(debug=True)