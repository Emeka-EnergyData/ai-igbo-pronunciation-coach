from pathlib import Path

def save_audio(audio, filename):
    save_folder = Path("assets/user_recordings")
    
    save_folder.mkdir(parents=True, exist_ok=True)
    file_path = save_folder / filename
    
    with open(file_path, "wb") as file:
        file.write(audio["bytes"])
    return str(file_path)