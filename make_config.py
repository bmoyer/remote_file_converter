#!/usr/bin/env python3

import clientsettings

if __name__ == '__main__':
    server_ip = input("Remote server IP addr: ")
    server_user = input("User login: ")
    remote_folder = input("Remote folder (i.e, path to server-side clone of this repo): ")

    settings = clientsettings.ClientSettings("config.ini")
    settings.server_ip = server_ip
    settings.server_user = server_user
    settings.remote_folder = remote_folder

    try:
        settings.write()
    except Exception as e:
        print("Failed to create config file: " + str(e))

    print("Wrote config file to " + settings.filename)
