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
    with open(args.connectfile, "r") as f:
        for line in f:
            print(line)
            print(line.split(" "))
            t = paramiko.Transport(line.split(" ")[0], 22)
            t.connect(username=line.split(" ")[1].rstrip("\n"), password="alta3")

            sftp = paramiko.SFTPClient.from_transport(t)
            sftpmover(args.moveme, sftp)

            sftp.close()
            t.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("moveme", help="Directory with files to move")
    parser.add_argument("connectfile", help="File with a list of connections")
    args = parser.parse_args()
    main()

