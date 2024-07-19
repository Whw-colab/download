import threading
import requests
import os

class Downloader:
    def __init__(self, target_folder):
        self.target_folder = target_folder

    def download(self, url, file_name):
        self._download(url, file_name)
    def _download(self, url, file_name):
        file_path = os.path.join(self.target_folder, file_name)
        if not os.path.exists(self.target_folder):
            os.makedirs(self.target_folder)
        response = requests.get(url, stream=True)#采用分块下载文件，每次从服务器中读取固定大小的文件
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):#用于生成文件的内容块，每个块的大小为1024字节
                if chunk:
                    f.write(chunk)
        print(f'Download completed: {file_name}')

    def thread(self, url, file_name):
        threading.Thread(target=self._download, args=(url, file_name)).start()

if __name__ == "__main__":
    downloader = Downloader("../download_files/folder")
    urls = ["https://i0.hippopx.com/photos/683/318/324/wolf-wolves-snow-wolf-landscape-preview.jpg",
            "https://i0.hippopx.com/photos/320/918/427/sky-clouds-sunlight-dark-preview.jpg"]
    filenames = ["wolf.jpg","sky.jpg"]

    for url, filename in zip(urls, filenames):
        downloader.thread(url, filename)