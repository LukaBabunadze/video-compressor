import subprocess
import os

def compress_video(input_path, output_path):
    if not os.path.exists(input_path):
        raise FileNotFoundError("Input video not found")

    command = [
        "ffmpeg",
        "-i", input_path,
        "-map", "0",
        "-c:v", "libx265",
        "-preset", "fast",   
        "-crf", "29",          
        "-c:a", "aac",
        "-b:a", "96k",      
        "-movflags", "+faststart",
        output_path
    ]

    subprocess.run(command, check=True)

compress_video("input.mov", "compressed.mp4")
