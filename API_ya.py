import requests
from TOKEN import TOKEN

class Yandex:
    base_host = 'https://cloud-api.yandex.net/'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'content-type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def create_folder(self, ya_path):
        folder_url = self.base_host + 'v1/disk/resources/'
        params = {'path': ya_path}
        res = requests.put(folder_url, params=params, headers=self.get_headers()).status_code
        return res

    def find_folder(self, ya_path):
        folder_url = self.base_host + 'v1/disk/resources/'
        params = {'path': ya_path}
        res = requests.get(folder_url, params=params, headers=self.get_headers()).status_code
        return res

if __name__ == '__main__':
    uploader = Yandex(TOKEN)
    create = uploader.create_folder('new_file')
    find = uploader.find_folder('new_file')




# class TestYandex(unittest.TestCase):
#
#     def test_find_folder(self):
#         self.assertTrue(Yandex(TOKEN).find_folder('new_file') == 200)