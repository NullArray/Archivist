import sys
import requests
import mimetypes
from os import path
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor


class Uploader:
    def __init(self, filename, file_host_url):
        self.filename = filename
        self.file_host_url = file_host_url

    @staticmethod
    def _progress_bar(monitor):
        progress = int(monitor.bytes_read/monitor.len*20)
        sys.stdout.write("\r[{}/{}] bytes |".format(monitor.bytes_read, monitor.len))
        sys.stdout.write("{}>".format("=" * progress))
        sys.stdout.write("{}|".format(" " * (20-progress)))
        sys.stdout.flush()

    def _multipart_post(self, data):
        encoder = MultipartEncoder(fields=data)
        monitor = MultipartEncoderMonitor(encoder, callback=self._progress_bar)
        r = requests.post(self.file_host_url,
                          data=monitor,
                          headers={'Content-Type': monitor.content_type})
        return r

    def _mimetype(self):
        _, extension = path.splitext(self.filename)
        if extension == '':
            extension = '.txt'
        mimetypes.init()
        try:
            return mimetypes.types_map[extension]
        except KeyError:
            return 'plain/text'

    def execute(self):
        raise NotImplementedError()