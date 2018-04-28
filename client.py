#!/usr/bin/env python3

import subprocess
import argparse
import ast
import os

import clientsettings


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="Image URL to download", required=True)
    parser.add_argument("-f", "--format", help="Format to convert image to", default="jpg")
    parser.add_argument("-s", "--scale", help="Scaling to apply to image (1%-100%)", default="100")
    args = parser.parse_args()

    return args


def remote_download(settings, url, format, scale):
    remote_exec = os.path.join(settings.remote_folder, "converter.py")
    script = "{0} -u {1} -f {2}".format(remote_exec, url, format)
    if scale != "100":
        script += " -s {0}".format(args.scale)
    
    command = "ssh {0}@{1} '{2}'".format(settings.server_user, settings.server_ip, script)
    remote_result = subprocess.check_output(command, shell=True).decode('utf-8').strip()
    return ast.literal_eval(remote_result)


def copy_file_from_server(settings, remote_file):
    command = "rsync -avz --remove-source-files {0}@{1}:{2} .".format(settings.server_user, settings.server_ip, remote_file)
    subprocess.check_output(command, shell=True)


def main(args):
    server_config = clientsettings.ClientSettings("config.ini")
    server_config.load()
    download_result = remote_download(server_config, args.url, args.format, args.scale)

    if download_result['error'] is None:
        copy_file_from_server(server_config, download_result['filename'])
        print("Reduced by: {0}".format(download_result['reduced_by']))
    else:
        print("Server returned error: " + download_result['error'])


if __name__ == '__main__':
    args = get_args()
    main(args)

