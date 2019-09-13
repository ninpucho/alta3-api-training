#!/usr/bin/env python3

import os
import paramiko
import argparse

FOLDER = "/home/student/filestocopy/"

def sftpmover(dir2move, sftpsessionobj):
    for x in os.listdir(dir2move):
        if not os.path.isdir(dir2move + x):
            sftpsessionobj.put(dir2move + x, "/tmp/" + x)

def main():

    t = paramiko.Transport('10.10.2.3', 22)

    t.connect(username="bender", password="alta3")

    sftp = paramiko.SFTPClient.from_transport(t)


    sftpmover(args.moveme, sftp)

    sftp.close()
    t.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("moveme", help="Directory with files to move")
    args = parser.parse_args()
    main()

