
import sys
from pathlib import Path
import cloudinary
import cloudinary.api
import cloudinary.uploader
from cloudinary.api import Error


import socket
REMOTE_SERVER = "www.google.com"
def is_connected(hostname):
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    host = socket.gethostbyname(hostname)
    # connect to the host -- tells us if the host is actually
    # reachable
    s = socket.create_connection((host, 80), 2)
    return True
  except:
     pass
  return False



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

# recursive loop for all images in folder to upload
def parse_folder (folder):
    for pth in folder.iterdir():
        if pth.suffix != '':
            images_to_upload.append(pth)
        else:
            parse_folder(pth)

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



if is_connected(REMOTE_SERVER):

    parse_folder(images_path)
    parse_folder(thumbs_path)

    images_to_upload.sort()


    for img in images_to_upload:
        upload_img(img)

    print "~~~~~~~~~~"
    for fail in failed_uploads:
        print fail
