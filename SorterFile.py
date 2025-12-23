import os, shutil
path = r"url of the folder to be sorted"
file_names = os.listdir(path)
folder_names = ['csv files', 'text files', 'image files', 'pdf files', 'word files', 'excel files', 'powerpoint files', 'audio files', 'video files', 'other files']
for folder_name in folder_names:
    folder_path = os.path.join(path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
for file_name in file_names:
    file_path = os.path.join(path, file_name)
    if os.path.isfile(file_path):
        ext = os.path.splitext(file_name)[1].lower()
        if ext == '.csv':
            shutil.move(file_path, os.path.join(path, 'csv files', file_name))
        elif ext == '.txt':
            shutil.move(file_path, os.path.join(path, 'text files', file_name))
        elif ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
            shutil.move(file_path, os.path.join(path, 'image files', file_name))
        elif ext == '.pdf':
            shutil.move(file_path, os.path.join(path, 'pdf files', file_name))
        elif ext in ['.doc', '.docx']:
            shutil.move(file_path, os.path.join(path, 'word files', file_name))
        elif ext in ['.xls', '.xlsx']:
            shutil.move(file_path, os.path.join(path, 'excel files', file_name))
        elif ext in ['.ppt', '.pptx']:
            shutil.move(file_path, os.path.join(path, 'powerpoint files', file_name))
        elif ext in ['.mp3', '.wav', '.aac']:
            shutil.move(file_path, os.path.join(path, 'audio files', file_name))
        elif ext in ['.mp4', '.avi', '.mkv', '.mov']:
            shutil.move(file_path, os.path.join(path, 'video files', file_name))
        else:
            shutil.move(file_path, os.path.join(path, 'other files', file_name))
