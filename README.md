# License-detect-NFS
TASK:
-
- A model created to showcase a practical implementation of the NFS file system
- The main task of the model is to detect a Lisence plate and out put the plate number 

REQUIREMENTS:
-

- 4 virtual machines running any operating system, preferably ubuntu
- 1 Server machine
- 3 Client machines
- all client machines must have a directory /home/<machine_name>/Desktop/car_photos containing 3 car photos

SETUP:
-

follow these instructions to install NFS server and clients:
- https://linuxhint.com/install-and-configure-nfs-server-ubuntu-22-04/
- https://www.digitalocean.com/community/tutorials/how-to-set-up-an-nfs-mount-on-ubuntu-22-04

clone the repo as follows:
- nfs_license_detect1.py and haarcascade_russian_plate_number.xml on Client 1
- nfs_license_detect2.py and haarcascade_russian_plate_number.xml on Client 2
- nfs_license_detect3.py and haarcascade_russian_plate_number.xml on Client 3
- nfs_license_plate_final.py, nfs_license_plate_ocr.py and black_screen.jpg on Server

USAGE:
-

- navigate to the directory where the repository is cloned
- change the directory paths in the code accordingly
- run the server script followed by the client scripts
  
  
  
