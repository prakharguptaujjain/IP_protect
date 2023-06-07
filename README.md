# IP_protect
## Keeps you away from malicious IPs
#### [Currently only supports Linux]

```                                                               
 ██▓ ██▓███      ██▓███   ██▀███   ▒█████  ▄▄▄█████▓▓█████  ▄████▄  ▄▄▄█████▓
▓██▒▓██░  ██▒   ▓██░  ██▒▓██ ▒ ██▒▒██▒  ██▒▓  ██▒ ▓▒▓█   ▀ ▒██▀ ▀█  ▓  ██▒ ▓▒
▒██▒▓██░ ██▓▒   ▓██░ ██▓▒▓██ ░▄█ ▒▒██░  ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒▓█    ▄ ▒ ▓██░ ▒░
░██░▒██▄█▓▒ ▒   ▒██▄█▓▒ ▒▒██▀▀█▄  ▒██   ██░  ▒██▒ ░ ░▒████▒▒ ▓███▀ ░  ▒██▒ ░ 
░██░▒██▒ ░  ░   ▒██▒ ░  ░░██▓ ▒██▒░ ████▓▒░  ▒██▒ ░ ░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░   
 ▒ ░░▒ ░        ░▒ ░       ░▒ ░ ▒░  ░ ▒ ▒░     ░     ░ ░  ░  ░  ▒       ░    
 ▒ ░░░          ░░         ░░   ░ ░ ░ ░ ▒    ░         ░   ░          ░      
 ░                          ░         ░ ░              ░  ░░ ░               
                                                           ░       
```

### How to install
Run below command to download the software
```
git clone https://github.com/prakharguptaujjain/IP_protect.git
cd IP_protect
```
Run ```python3 setup.py``` to configure the software. If you want default settings then skip this step.

Run ```sudo deploy.sh``` to deploy the software.

## Features
- This software works by blocking malicious IPs from accessing your device or DDoSing your device.
- Download IPs from specified location from web
- Download IPs from a trusted source at ```https://mcfp.felk.cvut.cz/publicDatasets/CTU-AIPP-BlackList/Latest/AIP-Alpha-latest.csv```
- Download IPs from Offline sources
- Download tor exist nodes IPs
- Delete old IPs from list automatically
- Has a feature to Whitelist IP
- Benchmarking feature to reduce the number of IPs added on low end devices
- Automatically adds IPs to the firewall
