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
    credz = [
            {"un": "bender", "ip": "10.10.2.3"},
            {"un": "zoidberg", "ip": "10.10.2.5"},
            {"un": "fry", "ip": "10.10.2.4"},
            ]
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")


    
    for cred in credz:
        sshsession = paramiko.SSHClient()
        sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print(f"connecting to... {cred.get('un')}@{cred.get('ip')}")
        sshsession.connect(hostname=cred.get("ip"), username=cred.get("un"), pkey=mykey)

        sftpsession = sshsession.open_sftp()

        sftpsession.put("slurm.cola", "/home/" + cred.get("un") + "/slurm.kola")

        working_dir = sftpsession.listdir()

        print("files in the local home directory:")
        for onefile in working_dir:
            if "." not in onefile[0]:
                print(onefile)

    sftpsession.close()
    sshsession.close()




if __name__ == '__main__':
    main()

