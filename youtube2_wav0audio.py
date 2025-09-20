import yt_dlp
import shutil
import os

# Pedir al usuario la URL del video
def download_youtube(url, output_path, download_audio=True):
    """Descarga un video de YouTube y lo convierte a WAV si download_audio es True,
    de lo contrario, descarga el video en el mejor formato disponible.
    """
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
    # Opciones de descarga para audio
audio_ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(downloads_folder, "%(title)s.%(ext)s"),
        'ffmpeg_location': ffmpeg_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
        }],
    }

    #Opciones de descarga para video
video_ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(downloads_folder, "%(title)s.%(ext)s"),
    }

# Descargar el video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Descarga completada. Revisá tu carpeta Descargas.")

# Preguntar al usuario si quiere descargar audio o video
option = input("¿Deseas descargar audio (a) o video (v)? (a/v): ").lower()

if option == 'a':
    ydl_opts = audio_ydl_opts
elif option == 'v':
    ydl_opts = video_ydl_opts
else:
    print("Opción inválida. Se descargará el audio por defecto.")
    ydl_opts = audio_ydl_opts

#Descargar el video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Descarga completada. Revisá tu carpeta Descargas.")
