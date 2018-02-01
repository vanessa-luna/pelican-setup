
import sys
import os
from pathlib import Path
import cloudinary
import cloudinary.api
import cloudinary.uploader
from cloudinary.api import Error
from blog_conf import THUMBNAIL_SIZES


# Cloudinary settings using python code. Run before pycloudinary is used.
cloudinary.config(
  cloud_name = 'vanessa-luna',
  api_key = '856643335657531',
  api_secret = 'pnAJM1ejPcM2HSZn4L7vaN217Pc'
)

images_path = Path.cwd() / '..' / '.output' / 'images'
thumbs_path = Path.cwd() / '..' / '.output' / 'thumb'

images_to_upload = []
failed_uploads = []






def upload_img(img):
    str_pth = str(img)
    index = str_pth.find('output/') + 7
    public_id = str_pth[index:-4] # filename without extension

    try:
        result = cloudinary.uploader.upload(str_pth,
            public_id = public_id,
            overwrite = False
        )
        overwritten =  "exists" if result['existing'] else "uploaded"
        print public_id + " - " + overwritten
    except cloudinary.api.Error as err:
        failed_uploads.append({"error": err, "path":img})
        print public_id + " - failed"




def upload (images):
    for img in images:
        if (img.suffix != "html" or img.suffix != "mp4"):
            upload_img(img)

    print "~~~~~~~~~~"
    for fail in failed_uploads:
        print fail



def get_thumbnails(folder):
    files = []
    for size in THUMBNAIL_SIZES:
        files += (thumbs_path / size / folder.stem).glob("*.*")
    return files





import socket
def is_connected():
  hostname = "www.google.com"
  try:
    host = socket.gethostbyname(hostname)
    s = socket.create_connection((host, 80), 2)
    return True
  except:
     pass
  return False


  

if is_connected():

    def _getmtime(entry):
        return entry.stat().st_ctime

    folders_in_images = [Path(images_path)]
    for item in Path(images_path).iterdir():
        if item.is_dir():
            folders_in_images.append (item)

    folders_in_images = sorted(folders_in_images, key=_getmtime, reverse=True)

    images_to_upload = []
    for f in folders_in_images:
        images_to_upload += f.glob("*.*")
        images_to_upload += get_thumbnails(f)

    upload(images_to_upload)
