from pyupload.uploader.base import Uploader


class CatboxUploader(Uploader):
    def __init__(self, filename):
        self.filename = filename
        self.file_host_url = "https://catbox.moe/user/api.php"

    def execute(self):
        file = open(self.filename, 'rb')
        try:
            data = {
                'reqtype': 'fileupload',
                'userhash': '',
                'fileToUpload': (file.name, file, self._mimetype())
            }
            response = self._multipart_post(data)
        finally:
            file.close()

        return response.text
