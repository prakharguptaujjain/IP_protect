#!/bin/bash

# Check if sysbench is already installed
if ! command -v sysbench &>/dev/null; then
    # Check sudo permission
    if [ "$EUID" -ne 0 ]; then 
        echo -e "\e[91mPlease run as root\e[0m"
        exit 1
    fi
    
    # Install benchmark
    if sudo apt-get install sysbench -y; then
        echo "Installation successful"
    else
        echo "Installation failed"
        exit 1
    fi
else
    echo "Benchmark already installed. Skipping installation."
fi
