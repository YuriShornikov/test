import requests

TOKEN = 'y0_AgAAAAAFm3q_AADLWwAAAADUOsbp0lkJ6SxXQZ2CjaM-Ph2t1xcJiwM'

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
        res = requests.put(folder_url, params=params, headers=self.get_headers())
        return res

if __name__ == '__main__':
    uploader = Yandex(TOKEN)
    create = uploader.create_folder('new_file')
    print(create)



import unittest

class TestYandex(unittest.TestCase):
    def SetUp(self):
        print('SetUp')

    def tearDown(self):
        print('tearDown')

    def test_create_folder(self):
        self.assertRegex(create, '[201]', msg=None)

unittest.main()