"""
This script gets IP address of Tor exists nodes
(Under development) It can also check whether an IP is a vpn one and can also identify its geolocation
(Under development)It can also make blocklist_ip data more advanced by adding columns like Tor, VPN, Country
"""

import os
import csv
import glob
import requests
import gzip
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

def download_tor_ips():
    """
    Download a list of Tor exit nodes IP addresses
    """
    url = "https://check.torproject.org/cgi-bin/TorBulkExitList.py"
    response = requests.get(url)
    ips = []
    for line in response.text.splitlines():
        if not line.startswith("#"):
            ips.append(line.strip())
    return ips


def is_tor(ip, TOR_IPS):
    """
    Check if an IP belongs to Tor
    """
    if ip in TOR_IPS:
        return True
    return False

def is_vpn(ip):
    """
    Check if an IP belongs to a VPN provider


    NOT USABLE AS EVERY SITE HAS ONLY SOME FREE LIMITS, NEED TO SETUP OWN DATABASE FOR VPN IP OR FIND SOME OPEN SOURCE ONE
    """


def get_geolocation(ip):
    """Get geolocation of an IP address
    
    NOT USABLE AS EVERY SITE HAS ONLY SOME FREE LIMITS, NEED TO SETUP OWN DATABASE FOR VPN IP OR FIND SOME OPEN SOURCE ONE
    """


def process_file(file_path,output_subdir_path):
    """
    Add columns to the latest .csv.gz file in the directory and save it as a new .csv.gz file with "advanced" suffix
    """
    TOR_IPS=download_tor_ips()

    with gzip.open(file_path, 'rt') as f_in, \
        gzip.open(os.path.join(output_subdir_path, os.path.basename(file_path)[:-7] + "_advanced.csv.gz"), 'wt', newline='') as f_out:

        #create duplicate f_in
        f_in2 = gzip.open(file_path, 'rt')
        reader = csv.DictReader(f_in2)

        ATTACKER_CSV_FORMAT=False
        IP_SCORE_CSV_FORMAT=False

        #header is [attacker]
        for col in reader.fieldnames:
            if('attacker' in col):
                ATTACKER_CSV_FORMAT=True

        #header is [Number,IP address,Rating]
        for col in reader.fieldnames:
            if("# Top IPs" in col):
                IP_SCORE_CSV_FORMAT=True
        
        if ATTACKER_CSV_FORMAT:
            reader = csv.DictReader(f_in)
            rows = list(reader)
            fieldnames = reader.fieldnames
            fieldnames.insert(1, 'Tor')
            
        if IP_SCORE_CSV_FORMAT:
            next(f_in, None)
            reader = csv.DictReader(f_in)
            rows= list(reader)
            fieldnames = reader.fieldnames
            fieldnames.insert(2, 'Tor')

        #intialize the writer
        writer = csv.DictWriter(f_out, fieldnames=fieldnames)
        writer.writeheader()

        with tqdm(total=len(rows), desc=f"Processing {os.path.basename(file_path)}", unit=" rows") as pbar:
            for row in rows:
                if ATTACKER_CSV_FORMAT:
                    ip = row['attacker']
                    tor = is_tor(ip,TOR_IPS)
                if IP_SCORE_CSV_FORMAT:
                    ip = row['IP address']
                    tor = is_tor(ip,TOR_IPS)
                row['Tor'] = tor
                writer.writerow(row)
                pbar.update(1)



def get_advance_csv():
    """
    Create an advanced version of the CSV file with the following columns:
    - Tor
    - VPN
    - Country
    """
    # Get the input folder path
    input_folder = os.path.join(os.getcwd(), "data", "output")
    
    #Create the output folder if it doesn't exist
    if not os.path.exists(os.path.join(os.getcwd(), "data", "output_advanced")):
        os.makedirs(os.path.join(os.getcwd(), "data", "output_advanced"))
    
    # Iterate over all subdirectories in the input folder(i.e. over all the models directories)
    for subdir in os.listdir(input_folder):
        input_subdir_path = os.path.join(input_folder, subdir)
        if os.path.isdir(input_subdir_path):
        
            # create the advanced subdir if it doesn't exist
            if not os.path.exists(os.path.join(os.getcwd(), "data", "output_advanced", subdir)):
                os.makedirs(os.path.join(os.getcwd(), "data", "output_advanced", subdir))
                
            output_subdir_path = os.path.join(os.getcwd(), "data", "output_advanced", subdir)

            #skip if input_subdir_path is empty
            if not os.listdir(input_subdir_path):
                continue

            # Find the latest created file in the input_subdir directory
            files = glob.glob(os.path.join(input_subdir_path, "*.csv.gz"))
            if files:
                latest_file = max(files, key=os.path.getctime)
            else:
                continue

            #file path
            input_file_path = os.path.join(input_subdir_path, latest_file)
            
            #check if the file is already processed
            if os.path.exists(os.path.join(output_subdir_path, os.path.basename(input_file_path)[:-7] + "_advanced.csv.gz")):
                print(f"File {os.path.basename(input_file_path)[:-7] + '_advanced.csv.gz'} already exists directory. Skipping...")
                continue

            # # Process each file using multithreading
            # with ThreadPoolExecutor() as executor:
            #     futures = [executor.submit(process_file, input_file_path,output_subdir_path) for latest_file in files]
            #     for future in tqdm(as_completed(futures), total=len(futures), desc=f"Processing {subdir}", unit=" files"):
            #         pass

            process_file(input_file_path,output_subdir_path)

def tor_exit_nodes():
    """
    Get the list of Tor exit nodes
    """
    TOR_IPS = download_tor_ips()
    
    # save in ./data/tor_exits/tor_exits_nodes.txt
    OUTPUT_DIR = os.path.join(os.getcwd(), "data", "tor_exits")
    if(not os.path.exists(OUTPUT_DIR)):
        os.makedirs(OUTPUT_DIR)
    with open(os.path.join(os.getcwd(), "data", "tor_exits", "tor_exits_nodes.txt"), "w") as f:
        for ip in TOR_IPS:
            f.write(ip + "\n")


if __name__ == "__main__":
    tor_exit_nodes()