if [ "$EUID" -ne 0 ]; then
  echo "Please run as root"
  exit 1
fi

echo "${YELLOW}Please wait while we install dependencies${RESET}"
pip install -r requirements.txt

RED=$(tput setaf 1)
GREEN=$(tput setaf 2)
YELLOW=$(tput setaf 3)
RESET=$(tput sgr0)

echo "${YELLOW}Please wait while we run the scripts${RESET}"

python3 ./utils/blocklists_downloader/main.py
python3 ./utils/tor_ip_geoloc_detect/main.py
python3 ./utils/benchmark/main.py
python3 ./utils/auto_trim/main.py
python3 ./utils/firewall_updater/main.py

sudo python3 ./utils/cron/main.py

if [ $? -eq 0 ]; then
  echo "${GREEN}Scripts have been run successfully${RESET}"
  echo "${GREEN}Software deployed successfully${RESET}"
else
  echo "${RED}An error occurred while running the scripts${RESET}"
  echo "${RED}Software deployment failed${RESET}"
  echo "${RED}Report the issue at https://github.com/prakharguptaujjain/IP_protect/issues/new ${RESET}"
fi
