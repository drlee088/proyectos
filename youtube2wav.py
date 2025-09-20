# drlee
# python para ejecutar local en terminal
# Usa yt-dlp y ffmpeg
# Asegurate de tener ambos instalados
# pip install yt-dlp
# brew install ffmpeg



import yt_dlp
import shutil
import os


url = input("Pegá la URL de YouTube: ")


downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")


ffmpeg_path = shutil.which("ffmpeg")
if ffmpeg_path is None:
    raise RuntimeError("ffmpeg no está instalado o no está en el PATH")


ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(downloads_folder, "%(title)s.%(ext)s"),
    'ffmpeg_location': ffmpeg_path,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
    }],
}

# Descargar el video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Descarga completada. Revisá tu carpeta Descargas.")
