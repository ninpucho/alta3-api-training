#!/usr/bin/env python3

import os
import paramiko

FOLDER = "/home/student/filestocopy/"

def main():

    t = paramiko.Transport('10.10.2.3', 22)

    t.connect(username="bender", password="alta3")

    sftp = paramiko.SFTPClient.from_transport(t)
    print(os.listdir(FOLDER))
    for x in os.listdir(FOLDER):
        if not os.path.isdir(FOLDER + x):
            sftp.put(FOLDER + x, "/tmp/" + x)
            print(FOLDER + x)

    sftp.close()

main()
