import os
import requests
import unittest
from random import choice
from string import ascii_letters
from pyupload.uploader import *


def generate_random_file_content():
    result = ''
    for _ in range(30):
        result += choice(ascii_letters)

    return result


class TestUploadMethods(unittest.TestCase):
    def setUp(self):
        self.content = generate_random_file_content()
        self.filename = 'testfile'
        with open(self.filename, 'w') as f:
            f.write(self.content)

    def tearDown(self):
        os.remove(self.filename)

    def compare(self, url):
        r = requests.get(url)
        self.assertEqual(r.text, self.content)

    def test_catbox(self):
        uploader = CatboxUploader(self.filename)
        result = uploader.execute()
        self.compare(result)

    def test_uguu(self):
        uploader = UguuUploader(self.filename)
        result = uploader.execute()
        self.compare(result)

    def test_fileio(self):
        uploader = FileioUploader(self.filename)
        result = uploader.execute()
        self.compare(result)

    def test_mixtape(self):
        uploader = MixTapeUploader(self.filename)
        result = uploader.execute()
        self.compare(result)


if __name__ == "__main__":
    unittest.main()
