import unittest
from API_ya import Yandex
from TOKEN import TOKEN



class TestYandex(unittest.TestCase):

    def test_find_folder(self):
        self.assertTrue(Yandex(TOKEN).find_folder('new_file') == 200)


unittest.main()