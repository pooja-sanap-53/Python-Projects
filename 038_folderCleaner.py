# Folder Cleaner using Python 

import os 

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
        
def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")

files = os.listdir()
files.remove("038_folderCleaner.py")

# to create folders
createIfNotExist('Images')
createIfNotExist('Docs')
createIfNotExist('Presentations')
createIfNotExist('Subtitles')
createIfNotExist('Media')
createIfNotExist('Others')

# to sort files
# Images
imgExts = [".png", ".jpg", ".jpeg", "gif"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

# Dcouments
docExts = [".txt", ".docx", ".pdf", ".doc"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

# Presentations
pptExts = [".pptx"]
ppts = [file for file in files if os.path.splitext(file)[1].lower() in pptExts]

# Subtitles
subtitleExts = [".vtt"]
stts = [file for file in files if os.path.splitext(file)[1].lower() in subtitleExts]

# Media
mediaExts = [".mp4", ".mp3", "flv"]
medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]


others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in mediaExts) and (ext not in subtitleExts) and (ext not in pptExts) and (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
        others.append(file)


# to move files in respective folders
move('Images', images)
move('Docs', docs)
move('Presentations', ppts)
move('Subtitles', stts)
move('Media', medias)
move('Others', others)
