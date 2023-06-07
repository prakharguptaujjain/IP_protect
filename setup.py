import time
import os
import json
from termcolor import colored
import configparser


def LOGO():
    """
    This function prints the logo of the project
    """
    frames = [
        '''
    / \\
    | |
    | |
    \\_/
    ''',
        '''
    $$$$$$\\ $$$$$$$\\  
    \\_$$  _|$$  __$$\\ 
      $$ |  $$ |  $$ |
      $$ |  $$$$$$$  |
      $$ |  $$  ____/ 
      $$ |  $$ |      
    $$$$$$\\ $$ |      
    \\______|\\__|      
    ''',
        '''              
                  ____         ____    
                / __ \\____   / __ 
         ___    U|  _"\\ u    U|  _"\\ u 
        |_"_|   \\| |_) |/    \\| |_) |/ 
         | |     |  __/       |  __/   
       U/| |\\u   |_|          |_|      
    .-,_|___|_,-.||>>_        ||>>_    
     \\_)-' '-(_/(__)__)      (__)__)   
    ''',
        '''
      __  ____    ____  ____ 
     (  )(  _ \\  (  _ \\(  _ \\
      )(  ) __/   ) __/ )   /
     (__)(__)    (__)  (__\\_)
    ''',
        '''
     ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
     ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌     ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌
         ▐░▌     ▐░▌       ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌
         ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌
         ▐░▌     ▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌
         ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ ▐░▌       ▐░▌
         ▐░▌     ▐░▌               ▐░▌          ▐░▌     ▐░▌  ▐░▌       ▐░▌
     ▄▄▄▄█░█▄▄▄▄ ▐░▌               ▐░▌          ▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄█░▌
    ▐░░░░░░░░░░░▌▐░▌               ▐░▌          ▐░▌       ▐░▌▐░░░░░░░░░░░▌
     ▀▀▀▀▀▀▀▀▀▀▀  ▀                 ▀            ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀ 
    ''',
        '''
     ___   _______    _______  ______    _______  _______ 
    |   | |       |  |       ||    _ |  |       ||       |
    |   | |    _  |  |    _  ||   | ||  |   _   ||_     _|
    |   | |   |_| |  |   |_| ||   |_||_ |  | |  |  |   |  
    |   | |    ___|  |    ___||    __  ||  |_|  |  |   |  
    |   | |   |      |   |    |   |  | ||       |  |   |  
    |___| |___|      |___|    |___|  |_||_______|  |___|  
    ''',
        '''
      _____ _____    _____  _____   ____ _______ ______ 
     |_   _|  __ \  |  __ \|  __ \ / __ \__   __|  ____|
       | | | |__) | | |__) | |__) | |  | | | |  | |__   
       | | |  ___/  |  ___/|  _  /| |  | | | |  |  __|  
      _| |_| |      | |    | | \ \| |__| | | |  | |____ 
     |_____|_|      |_|    |_|  \_\\____/  |_|  |______|
    ''',
        '''
      ___________         ________  ________      ____   __________ __________   ____   
    `MM`MMMMMMMb.       `MMMMMMMb.`MMMMMMMb.   6MMMMb  MMMMMMMMMM `MMMMMMMMM  6MMMMb/ 
     MM MM    `Mb        MM    `Mb MM    `Mb  8P    Y8 /   MM   \  MM      \ 8P    YM 
     MM MM     MM        MM     MM MM     MM 6M      Mb    MM      MM       6M      Y 
     MM MM     MM        MM     MM MM     MM MM      MM    MM      MM    ,  MM        
     MM MM    .M9        MM    .M9 MM    .M9 MM      MM    MM      MMMMMMM  MM        
     MM MMMMMMM9'        MMMMMMM9' MMMMMMM9' MM      MM    MM      MM    `  MM        
     MM MM               MM        MM  \M\   MM      MM    MM      MM       MM        
     MM MM               MM        MM   \M\  YM      M9    MM      MM       YM      6 
     MM MM               MM        MM    \M\  8b    d8     MM      MM      / 8b    d9 
    _MM_MM_             _MM_      _MM_    \M\_ YMMMM9     _MM_    _MMMMMMMMM  YMMMM9  
    ''',
    '''                                                                             
     ██▓ ██▓███      ██▓███   ██▀███   ▒█████  ▄▄▄█████▓▓█████  ▄████▄  ▄▄▄█████▓
    ▓██▒▓██░  ██▒   ▓██░  ██▒▓██ ▒ ██▒▒██▒  ██▒▓  ██▒ ▓▒▓█   ▀ ▒██▀ ▀█  ▓  ██▒ ▓▒
    ▒██▒▓██░ ██▓▒   ▓██░ ██▓▒▓██ ░▄█ ▒▒██░  ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒▓█    ▄ ▒ ▓██░ ▒░
    ░██░▒██▄█▓▒ ▒   ▒██▄█▓▒ ▒▒██▀▀█▄  ▒██   ██░  ▒██▒ ░ ░▒████▒▒ ▓███▀ ░  ▒██▒ ░ 
    ░██░▒██▒ ░  ░   ▒██▒ ░  ░░██▓ ▒██▒░ ████▓▒░  ▒██▒ ░ ░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░   
     ▒ ░░▒ ░        ░▒ ░       ░▒ ░ ▒░  ░ ▒ ▒░     ░     ░ ░  ░  ░  ▒       ░    
     ▒ ░░░          ░░         ░░   ░ ░ ░ ░ ▒    ░         ░   ░          ░      
     ░                          ░         ░ ░              ░  ░░ ░               
                                                               ░       
    '''
    ]

    # Clear the console screen
    def clear(): return os.system('cls' if os.name == 'nt' else 'clear')
    for frame in frames:
        clear()  # Clear the console before displaying the next frame
        print(frame)
        time.sleep(0.5)


class CONFIGS:
    CONFIG_FILES = {
        'blocklists_downloader': './configurations/blocklists_downloader_config.ini',
        'firewall_updater': './configurations/firewall_updater_config.json',
        'auto_trim': './configurations/auto_trim_config.json',
        'benchmark': './configurations/benchmark_config.json',
        'cron': './configurations/cron_config.json',
        'tor_ip_geoloc_detect': './configurations/tor_ip_geoloc_detect_config.json',
        '0': 'go_back'
    }

    @staticmethod
    def show_all_configs():
        """
        This function prints all the configuration files and their contents
        """
        for name, file_path in CONFIGS.CONFIG_FILES.items():
            if(name != '0'):
                CONFIGS.print_config(file_path, name)

    @staticmethod
    def print_config(file_path, name=""):
        print()
        print(colored("#################", "red"))
        if(name != ""):
            print(colored(name, "blue"))

        def print_key_value(key, value):
            if isinstance(value, dict):
                for k, v in value.items():
                    print_key_value(f"{key}.{k}", v)
            else:
                if isinstance(value, bool):
                    print(f"{key}: {colored(str(value), 'yellow')}")
                else:
                    print(f"{key}: {colored(str(value), 'yellow')}")

        try:
            with open(file_path, "r") as file:
                print("File Name:", colored(file_path, attrs=["bold"]))
                content = file.read()

                # Detect file type based on the extension
                if file_path.endswith(".json"):
                    try:
                        config = json.loads(content)
                        for key, value in config.items():
                            print_key_value(key, value)
                    except json.JSONDecodeError:
                        print(content)

                elif file_path.endswith(".ini"):
                    config = configparser.ConfigParser()
                    config.optionxform = str  # Preserve case sensitivity
                    config.read_string(content)
                    for section in config.sections():
                        print(colored(f"[{section}]", "cyan"))
                        for key, value in config.items(section):
                            if value.startswith(";"):
                                key_value = colored(
                                    f"{key}", "yellow") + colored(" =", "magenta") + colored(f" {value}", "magenta")
                                print(key_value)
                            else:
                                key_value = colored(
                                    f"{key} =", "yellow") + colored(f" {value}", "yellow")
                                print(key_value)
            print(colored("#################", "red"))

        except FileNotFoundError:
            print(colored("File not found.\n", "red"))

    @staticmethod
    def explain_script(script_name):
        script_explanation = {
            'tor_ip_geoloc_detect': 'This script gets IP address of Tor exists nodes(Under development) \nIt can also check whether an IP is a vpn one and can also identify its geolocation(Under development)\nIt can also make blocklist_ip data more advanced by adding columns like Tor, VPN, Country',
            'benchmark': """This module is used to benchmark the system. It is used to get the benchmark value of the system and save it in the config file ,if a microprocessor is using this software to protect themself from malicious IP, so this benchmark value can be used to trim the blocklists to a certain value so that the microprocessor can work efficiently.""",
            'firewall_updater': """This module adds the IPs in the Blacklisted_IP from data folder and exclude the whitelisted_ips into the firewall""",
            'auto_trim': """For microprocessor, the number of blocklists can be too large to be processed by the cpu.\nSo this module trims the blocklists to a certain value (using benchmark module)so that the microprocessor can work efficiently.\nTotal IP to be added to the firewall = bench_value * trimmed_value_constant""",
            'blocklists_downloader': """This is a script to retrieve the latest blocklists from the online sources and as well as latest created blocklists from the offline sources and save it to OUTPUT_DIR (Retrieved_blocklists)\nWe already provide a blocklists from online source which is at https://mcfp.felk.cvut.cz/publicDatasets/CTU-AIPP-BlackList/Latest/AIP-Alpha-latest.csv (you can visit it and change from the options that best suits you)\nPlease check the format of config file (config.ini) and change it according to your needs""",
            'cron': """This module is used to create or delete cron jobs for the blocklists_downloader program."""
        }
        return script_explanation.get(script_name, 'Explanation not found.')

    @staticmethod
    def edit_config():
        show_nums = {
            '0': 'go back',
            '1': 'tor_ip_geoloc_detect',
            '2': 'benchmark',
            '3': 'firewall_updater',
            '4': 'auto_trim',
            '5': 'blocklists_downloader',
            '6': 'cron'
        }
        selected_number = '-1'
        while selected_number != '0':
            def clear(): return os.system('cls' if os.name == 'nt' else 'clear')
            clear()
            print("Please select a script to learn about:")
            for number, script_name in show_nums.items():
                print(colored(f"{number} ", "yellow"), end="")
                print(colored(f"{script_name}", "red"))
            selected_number = '-1'
            selected_number = input(
                "Enter the number corresponding to the script (Enter 0 to go back): ")
            if selected_number not in show_nums.keys():
                print("Invalid script number.")
                selected_number = input(
                    "Enter the number corresponding to the script (Enter 0 to go back): ")
            elif selected_number == '0':
                return 0
            else:
                script_name = show_nums[selected_number]
                explanation = CONFIGS.explain_script(script_name)
                print(colored(f"\n{script_name}", "yellow"), end="")
                print(" - Functionality Explanation:")
                print(colored(explanation, "green"))

                show_config_choice = input(
                    "Do you want to see the configuration file for this script? (Y/N)(Enter 0 to go back):")
                while show_config_choice.upper() not in ['Y', 'N', '0']:
                    print("Invalid input.")
                    show_config_choice = input(
                        "Do you want to see the configuration file for this script? (Y/N)(Enter 0 to back):")

                if show_config_choice == '0':
                    return
                if show_config_choice.upper() == 'Y':
                    CONFIGS.print_config(CONFIGS.CONFIG_FILES[script_name])

                config_choice = input(
                    "Do you want to set configurations for this script? (Y/N)(Enter 0 to back):")
                while config_choice.upper() not in ['Y', 'N', '0']:
                    print("Invalid input.")
                    config_choice = input(
                        "Do you want to set configurations for this script? (Y/N)(Enter 0 to go back):")

                if config_choice == '0':
                    return

                if config_choice.upper() == 'Y':
                    config_file = CONFIGS.CONFIG_FILES[script_name]
                    CONFIGS.set_config(config_file)

    @staticmethod
    def set_config(config_file):
        # print("Please edit the configuration file as required.")
        # open config file
        os.system(f"nano {config_file}")
        print(colored("Configuration file saved successfully!", "green"))
        input(colored("Press any key to continue...", "blue"))
        print()


def goodbye():
    """This function prints a goodbye message"""
    print("################################")
    print("GOODBYE! (English)")
    print("ADIOS! (Spanish)")
    print("AU REVOIR! (French)")
    print("TCHAU! (Portuguese)")


def init():
    print("Welcome to the IP Protect project!")
    print("####STAY PROTECTED####")
    print()
    print()
    options = {'0': 'exit', '1': 'show_all_configs', '2': 'edit_config',
               '3': 'contribute', '4': 'report_bug', '5': 'learn_about_admin','6': 'save all changes and exit'}
    selected_number = '-1'
    ask_for_press_any_key = False
    while selected_number != '0':
        print("Please select an option:")
        for number, option in options.items():
            print(colored(f"{number} ", "yellow"), end="")
            print(colored(f"{option}", "red"))
        selected_number = input(
            "Enter the number corresponding to the option:")

        def clear(): return os.system('cls' if os.name == 'nt' else 'clear')
        clear()
        if selected_number not in options.keys():
            print("Invalid option number.")
            selected_number = input(
                "Enter the number corresponding to the option:")
        elif selected_number == '0':
            return
        else:
            option = options[selected_number]
            if option == 'exit':
                goodbye()
                exit()
            elif option == 'show_all_configs':
                def clear(): return os.system('cls' if os.name == 'nt' else 'clear')
                clear()
                CONFIGS.show_all_configs()
            elif option == 'edit_config':
                def clear(): return os.system('cls' if os.name == 'nt' else 'clear')
                clear()
                if(CONFIGS.edit_config()==0):ask_for_press_any_key=True
            elif option == 'contribute':
                def clear(): return os.system('cls' if os.name == 'nt' else 'clear')
                clear()
                print(colored(
                    "Please visit below link, understand the code and contribute to the project using Pull Request option.", "yellow"))
                print(colored("https://github.com/prakharguptaujjain/IP_protect", "red"))
            elif option == 'report_bug':
                def clear(): return os.system('cls' if os.name == 'nt' else 'clear')
                clear()
                print(
                    colored("Please visit below link and report you issue there.", "yellow"))
                print(
                    colored("https://github.com/prakharguptaujjain/IP_protect/issues/new", "red"))
            elif option == 'learn_about_admin':
                def clear(): return os.system('cls' if os.name == 'nt' else 'clear')
                clear()
                print(colored("HEY THERE I AM PRAKHAR GUPTA!", "yellow"))
                print(colored(
                    "PURSUING B.TECH IN ARTIFICIAL INTELLIGENCE AND DATA SCIENCE FROM IIT JODHPUR", "red"))
                print(colored(
                    "Check my LinkedIn profile : https://www.linkedin.com/in/prakharguptaujjain/", "yellow"))
            elif option == 'save all changes and exit':
                print(colored("Saving all changes and exiting...", "green"))
                print(colored("All changes saved successfully!", "green"))
                print(colored("To deploy the changes, please run the following command:", "yellow"),end="")
                print(colored("sudo deploy.sh", "red"))
                goodbye()
                exit()
        print()
        if(not ask_for_press_any_key):input(colored("Press any key to continue...", "blue"))
        def clear(): return os.system('cls' if os.name == 'nt' else 'clear')
        clear()


if __name__ == '__main__':
    def clear(): return os.system('cls' if os.name == 'nt' else 'clear')
    clear()
    LOGO()
    init()
    goodbye()
