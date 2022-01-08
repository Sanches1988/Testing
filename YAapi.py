import requests

TOKEN = ''

class YandexDiskAPI:

    def __init__(self, TOKEN):
        self.token = TOKEN

    def create_folder(self, path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        params = {'path': path}

        response = requests.put(url, params=params, headers=headers)
        return response.status_code

if __name__ == '__main__':
    yandex = YandexDiskAPI(TOKEN)
    print(yandex.create_folder('test'))