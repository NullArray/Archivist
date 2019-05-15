from pyupload.uploader import *
import click

uploader_classes = {
    "catbox": CatboxUploader,
    "mixtape": MixTapeUploader,
    "uguu": UguuUploader,
    "fileio": FileioUploader
}


@click.command()
@click.option('--host', default='catbox', help='catbox/mixtape/uguu/fileio')
@click.argument('name')
def upload(host, name):
    uploader_class = uploader_classes[host]
    uploader_instance = uploader_class(name)
    result = uploader_instance.execute()
    print("Your link : {}".format(result))


if __name__ == "__main__":
    upload()
