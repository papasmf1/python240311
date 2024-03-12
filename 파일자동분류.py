import os
import shutil

# 다운로드 폴더 경로 설정
download_folder = r'C:\Users\student\Downloads'

# 목적지 폴더 설정
destination_folders = {
    'images': r'C:\Users\student\Downloads\images',
    'data': r'C:\Users\student\Downloads\data',
    'docs': r'C:\Users\student\Downloads\docs',
    'archive': r'C:\Users\student\Downloads\archive'
}

# 폴더가 없는 경우 생성
for folder_path in destination_folders.values():
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# 파일 유형에 따라 이동
for filename in os.listdir(download_folder):
    if filename.endswith(('.jpg', '.jpeg')):
        shutil.move(os.path.join(download_folder, filename), destination_folders['images'])
    elif filename.endswith(('.csv', '.xlsx')):
        shutil.move(os.path.join(download_folder, filename), destination_folders['data'])
    elif filename.endswith(('.txt', '.doc', '.pdf')):
        shutil.move(os.path.join(download_folder, filename), destination_folders['docs'])
    elif filename.endswith('.zip'):
        shutil.move(os.path.join(download_folder, filename), destination_folders['archive'])

