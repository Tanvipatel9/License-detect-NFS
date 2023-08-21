'''
This file contains code that does through all of
the shared folders of the clients and calls
the run() function from nfs_license_plate_ocr.py 
if any of the directories are updated to perform ocr
'''


import nfs_license_plate_ocr as ocr
import time
import os
from pathlib import Path

directory = Path('/mnt/nfs_share/')
file_set = set()

# infinite loop 
while True:
    # list of the sub directories (share_vm4 etc.) within nfs_share
    client_lst = os.listdir(directory)

    # for each invidival sub directory in the shared directory (nfs_share)
    for client in client_lst:
        # path to the sub directory
        client_dir = directory/client
        # list of all photos in the sub dir
        photo_lst = os.listdir(client_dir)
        
        # for each photo in sub dir
        for photo in photo_lst:
            # path to an individual photo in sub dir
            photo_path = client_dir / photo
            # perform ocr only if not performed earlier
            if photo_path not in file_set:
                time.sleep(0.5)
                ocr.run(photo_path)
                # add processed photo to set so it is not processed again
                file_set.add(photo_path)
        
    time.sleep(0.5)
            






