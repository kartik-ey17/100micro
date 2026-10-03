from pathlib import Path

folder = Path("disorg")

images = [".jpg" , ".jpeg" , ".gif" , ".png" , ".svg"]
videos = [".mp4" , ".mov"]
programming = [".cpp" , ".py" , ".java" , ".go" , ".js" , ".jsx" , ".ts" , ".html" , ".css"]
data = [".sql" , ".db" , ".json" , ".csv"]
documents = [".pdf" , ".docx" , ".txt"]
sounds = [".mp3" , ".wav"]

images_folder = folder / "Images"
videos_folder = folder / "Videos"
programs_folder = folder / "Programs"
data_folder = folder / "Data"
docs_folder = folder / "Documents"
sounds_folder = folder / "Sounds"

images_folder.mkdir(exist_ok=True)
videos_folder.mkdir(exist_ok=True)
programs_folder.mkdir(exist_ok=True)
data_folder.mkdir(exist_ok=True)
docs_folder.mkdir(exist_ok=True)
sounds_folder.mkdir(exist_ok=True)

for item in folder.iterdir():
    file = Path(item)
    ext = file.suffix.lower()
    print(file)
    print(ext)
    if ext in images:
        destination = folder / "Images" / file.name
        file.rename(destination)
    elif ext in videos:
        destination = folder / "Videos" / file.name
        file.rename(destination)
    elif ext in programming:
        destination = folder / "Programs" / file.name
        file.rename(destination)
    elif ext in data:
        destination = folder / "Data" / file.name
        file.rename(destination)
    elif ext in documents:
        destination = folder / "Documents" / file.name 
        file.rename(destination) 
    elif ext in sounds:
        destination = folder / "Sounds" / file.name
        file.rename(destination)
    else:
        print("misc")