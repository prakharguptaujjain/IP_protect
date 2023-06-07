"""This module is used to create or delete cron jobs for the blocklists_downloader program."""

import os
import platform
import subprocess
import json
from datetime import datetime, timedelta

CONFIG = './configurations/cron_config.json'

def create_cron():
    # Check from config file if the user wants to automatically update the firewall rules
    with open(CONFIG) as f:
        data = json.load(f)

    if data['auto_download_blocklists']:
        path_blocklists_downloader = os.path.curdir + "/utils/blocklists_downloader/main.py"

        # Check the type of OS
        os_name = platform.system()

        if os_name == "Linux":
            cron_frequency_hours = data.get('cron_frequency_hours', 24)
            first_start_time = data.get('first_cron_start_time', "00:00 AM")
            # Calculate the start time for the first cron job
            start_time = datetime.strptime(first_start_time, "%I:%M %p")
            current_time = datetime.now()
            time_diff = start_time - current_time
            if time_diff.days < 0:
                start_time += timedelta(days=1)

            software_directory = os.getcwd()

            # Create a cron job on Linux for blocklist downloader
            blocklist_command = f'(crontab -l ; echo "{start_time.minute+1} {start_time.hour} */{cron_frequency_hours} * * python3 {path_blocklists_downloader} {software_directory}") | crontab -'
            subprocess.call(blocklist_command, shell=True)
            print("Blocklist downloader cron job created successfully!")

        #######[Support for Windows and MacOS are under development]########
        # elif os_name == "Windows":
        #     # Create a scheduled task on Windows
        #     command = f'schtasks /create /tn "Python Script Task" /tr "python {path_blocklists_downloader}" /sc daily /mo {num_days} /st 23:59'
        #     subprocess.call(command, shell=True)
        #     print("Blocklist downloader scheduled task created successfully!")
        # else:
        #     print("Unsupported operating system.")
        #     exit()

    if data['auto_download_tor_exit_nodes_ips']:
        path_tor_ip_geoloc_detect = os.path.curdir + "/utils/tor_ip_geoloc_detect/main.py"

        # Check the type of OS
        os_name = platform.system()

        if os_name == "Linux":
            cron_frequency_hours = data.get('cron_frequency_hours', 24)
            first_start_time = data.get('first_cron_start_time', "00:00 AM")
            # Calculate the start time for the first cron job
            start_time = datetime.strptime(first_start_time, "%I:%M %p")
            current_time = datetime.now()
            time_diff = start_time - current_time
            if time_diff.days < 0:
                start_time += timedelta(days=1)

            software_directory = os.getcwd()

            # Create a cron job on Linux for blocklist downloader
            tor_exit_nodes_ips_command = f'(crontab -l ; echo "{start_time.minute+2} {start_time.hour} */{cron_frequency_hours} * * python3 {path_tor_ip_geoloc_detect} {software_directory}") | crontab -'
            subprocess.call(tor_exit_nodes_ips_command, shell=True)
            print("Tor IP geolocation detector cron job created successfully!")

        #######[Support for Windows and MacOS are under development]########
        # elif os_name == "Windows":
        #     # Create a scheduled task on Windows
        #     command = f'schtasks /create /tn "Python Script Task" /tr "python {path_blocklists_downloader}" /sc daily /mo {num_days} /st 23:59'
        #     subprocess.call(command, shell=True)
        #     print("Blocklist downloader scheduled task created successfully!")
        # else:
        #     print("Unsupported operating system.")
        #     exit()

    if data['auto_update_firewall_with_IP']:
        if os_name == "Linux":
            cron_frequency_hours = data.get('cron_frequency_hours', 24)
            first_start_time = data.get('first_cron_start_time', "00:00 AM")
            # Calculate the start time for the first cron job
            start_time = datetime.strptime(first_start_time, "%I:%M %p")
            current_time = datetime.now()
            time_diff = start_time - current_time
            if time_diff.days < 0:
                start_time += timedelta(days=1)

            # Get the parent of the parent directory location
            software_directory = os.getcwd()

            # Specify the script location relative to the grandparent directory
            firewall_updater_location = os.path.join(software_directory, 'utils', 'firewall_updater', 'main.py')

            # Create a cron job on Linux
            firewall_command = f'(crontab -l ; echo "{start_time.minute+3} {start_time.hour} */{cron_frequency_hours} * * python3 {firewall_updater_location} {software_directory}") | crontab -'
            subprocess.call(firewall_command, shell=True)
            print("Firewall updater cron job created successfully!")

        #######[Support for Windows and MacOS are under development]########
        # elif os_name == "Windows":
        #     # Create a scheduled task on Windows
        #     command = f'schtasks /create /tn "Python Script Task" /tr "python {path_firewall_updater}" /sc daily /mo {num_days} /st 00:00'
        #     subprocess.call(command, shell=True)
        #     print("Firewall updater scheduled task created successfully!")
        # else:
        #     print("Unsupported operating system.")
        #     exit()


def del_grep_cronjobs():
    """This module greps the cronjobs containing 'main.py' and prints them and asks the user to enter the number of the cronjob to delete"""
    choice='-1'
    while(choice!='0'):
        # clear screen
        os.system('clear')
        output = os.popen('crontab -l | grep "main.py"').read().strip().split('\n')
        print("Cronjobs containing 'main.py':\n")
        print("No.")
        jobs_cnt = 0
        for i, cronjob in enumerate(output):
            print(f" {i+1}  -> {cronjob}")
            jobs_cnt += 1
        print("To exit deletion menu enter 0")
        choice = input("Enter the number of the cronjob you want to delete: ")
        if(choice == '0'):
            return
        if int(choice)>jobs_cnt or int(choice)<0:
            print("Invalid choice!")
            input("Press any key to continue...")
            continue
        os.system("crontab -l | sed '{}d' | crontab -".format(choice))
        print("Cronjob deleted successfully!")

def del_all_related_crons():
    """This module deletes all the cronjobs created by this module"""
    # Get the current user's crontab
    crontab_output = subprocess.check_output("crontab -l", shell=True).decode("utf-8")
    
    # Patterns to search for
    patterns = [
        "blocklists_downloader/main.py",
        "tor_ip_geoloc_detect/main.py",
        "firewall_updater/main.py"
    ]

    for pattern in patterns:
        try:
            grep_output=subprocess.check_output(f'crontab -l | grep "{pattern}"', shell=True).decode("utf-8")
            if(grep_output==''):
                continue
            cron_command = f'(crontab -l | grep -v "{pattern}") | sudo crontab -'
            subprocess.call(cron_command, shell=True)
            print(f"Old Cronjobs of '{pattern}' deleted successfully!")
        except :
            pass

if __name__ == "__main__":
    # Check if the script is run with sudo
    if os.geteuid() != 0:
        print("This script requires root privileges. Please run with sudo.")
        exit(1)
    del_all_related_crons()
    create_cron()
    # del_grep_cronjobs()