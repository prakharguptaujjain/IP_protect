#!/usr/bin/env python3
"""
This is a script to retrieve the latest blocklists from the online sources and as well as latest created blocklists from the offline sources and save it to OUTPUT_DIR (Retrieved_blocklists)
We already provide a blocklists from online source which is at https://mcfp.felk.cvut.cz/publicDatasets/CTU-AIPP-BlackList/Latest/AIP-Alpha-latest.csv (you can visit it and change from the options that best suits you)
Please check the format of config file (config.ini) and change it according to your needs.
"""
import requests
import os
import configparser
import time
import shutil
import gzip

RETRIEVE_FILE = "configurations/blocklists_downloader_config.ini"
OUTPUT_DIR = "./data/Retrieved_blocklists"

def get_blocklists():
    # Load the configuration from the .ini file
    config = configparser.ConfigParser()
    config.read(RETRIEVE_FILE)

    # Online pre_provided blocklists to retrieve
    url = config["pre_provided_blocklists_online"]["url"]
    filename = url.split("/")[-1]
    output_folder = os.path.join(OUTPUT_DIR, "pre_provided_blocklists_online")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    output_file = os.path.join(output_folder, filename)
    if not os.path.exists(output_file):
        response = requests.get(url)
        with open(output_file, "w") as f:
            f.write(response.text)
        print(f"Retrieved {filename} from {url}")
    else:
        print(f"{filename} already exists in {output_folder}")

    # Online blocklists to retrieve
    url_list = [url for url in config["blocklists_online"].values() if url]
    for url in url_list:
        filename = url.split("/")[-1]
        output_folder = os.path.join(OUTPUT_DIR, "blocklists_online")
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        output_file = os.path.join(output_folder, filename)
        if not os.path.exists(output_file):
            response = requests.get(url)
            with open(output_file, "w") as f:
                f.write(response.text)
            print(f"Retrieved {filename} from {url}")
        else:
            print(f"{filename} already exists in {output_folder}")

    # Offline blocklists to copy
    folder_list = [folder for folder in config["blocklists_offline_folders"].values() if folder]
    for folder in folder_list:
        files = os.listdir(folder)
        files = [f for f in files if f.endswith(".csv")]
        files = sorted(files, key=lambda f: os.path.getmtime(os.path.join(folder, f)), reverse=True)
        newest_file = files[0]
        output_folder = os.path.join(OUTPUT_DIR, "Offline")
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        output_file = os.path.join(output_folder, newest_file)
        input_file = os.path.join(folder, newest_file)
        if not os.path.exists(output_file):
            shutil.copy(input_file, output_file)
            print(f"Copied {newest_file} from {folder}")
        else:
            print(f"{newest_file} already exists in {output_folder}")


def delete_old_files():
    """
    Delete files in the OUTPUT_DIR that are older than the RETENTION_PERIOD_DAYS.
    """
    config = configparser.ConfigParser()
    config.read(RETRIEVE_FILE)
    RETENTION_PERIOD_DAYS = int(config["general"]["retention_period_days"])
    now = time.time()
    for folder in os.listdir(OUTPUT_DIR):
        for filename in os.listdir(os.path.join(OUTPUT_DIR, folder)):
            file_path = os.path.join(OUTPUT_DIR, folder, filename)
            if os.path.isfile(file_path):
                age_days = (now - os.path.getmtime(file_path)) / (24 * 3600)
                if age_days > RETENTION_PERIOD_DAYS:
                    os.remove(file_path)
                    print(f"Deleted {filename} from {folder}")


if __name__ == "__main__":
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    delete_old_files()
    get_blocklists()
