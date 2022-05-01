
import requests
URL = 'https://cloud-api.yandex.net/v1/disk/resources'
token = "AQAAAABH4ShVAADLW9rqGPx6U0DIntyUCVTH7LQ"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}

def upload_file(loadfile, savefile, replace=False):
    response = requests.get(f'{URL}/upload?path={savefile}&overwrite={replace}', headers=headers).json()
    with open(loadfile, 'rb') as file_name:
        try:
            requests.put(response['href'], files={'file':file_name})
        except KeyError:
            print(response)

upload_file(r'D:\pythonProject7\a25.png', 'a25.png')