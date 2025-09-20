import yt_dlp
import shutil
import os

# Pedir al usuario la URL del video
url = input("Pegá la URL de YouTube: ")

# Detectar carpeta Descargas del usuario
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

# Detectar la ruta de ffmpeg automáticamente
ffmpeg_path = shutil.which("ffmpeg")
if ffmpeg_path is None:
    raise RuntimeError("ffmpeg no está instalado o no está en el PATH")

# Opciones de descarga
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