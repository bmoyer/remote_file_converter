#!/usr/bin/env python3

import urllib.request
import argparse
import subprocess
import os


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="Image URL to download", required=True)
    parser.add_argument("-f", "--format", help="Format to convert image to")
    parser.add_argument("-s", "--scale", help="Scaling to apply to image (1%-100%)", default="100")
    args = parser.parse_args()
    return args


def convert_image(url, format, scale):
    info = { 'filename': None, 'reduced_by': None, 'error': None }

    orig_fname = url[url.rfind("/")+1:]
    try:
        urllib.request.urlretrieve(url, orig_fname)
    except Exception as e:
        info['error'] = "Failed to download file: " + str(e)
        return info

    new_fname = orig_fname
    if format is not None:
        ext = os.path.splitext(orig_fname)[1][1:]
        new_fname = new_fname.replace(ext, format)

    orig_size = os.path.getsize(orig_fname)
    try:
        command = "convert {0} -resize {1}% {2}".format(orig_fname, scale, new_fname)
        subprocess.check_output(command, shell=True)
    except subprocess.CalledProcessError as e:
        info['error'] = "Failed to convert file: " + e.output.decode('utf-8')
        return info

    if new_fname != orig_fname:
        os.remove(orig_fname)

    new_size = os.path.getsize(new_fname)

    reduced_by = "%.3f" % float(new_size/orig_size)
    info['filename'] = os.path.abspath(new_fname)
    info['reduced_by'] = reduced_by
    return info
    

def main():
    args = get_args()
    result = convert_image(args.url, args.format, args.scale)
    print(result)


if __name__ == '__main__':
    main()

