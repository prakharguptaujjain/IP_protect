"""
This module is used to benchmark the system. It is used to get the benchmark value of the system and save it in the config file ,if a microprocessor is using this software to protect themself from malicious IP, so this benchmark value can be used to trim the blocklists to a certain value so that the microprocessor can work efficiently.
"""

import os
import json
import subprocess

CONFIG = './configurations/benchmark_config.json'


def benchmarker():
    # Download Benchmark
    print("Downloading Benchmark. Please wait (this might take a while)")
    exit_code = os.system("bash ./utils/benchmark/installer.sh")
    if exit_code != 0:
        print("Failed to install benchmark.")
        exit(1)
    else:
        print(f"\033[1mBenchmarking your device.\033[0m")

    # Do benchmark
    bench_value = subprocess.check_output(
        "sysbench cpu --cpu-max-prime=20000 --time=5 run | grep 'events per second' | awk '   {print $NF}'",
        shell=True)

    # Create config directory if it doesn't exist
    config_dir = os.path.dirname(CONFIG)
    os.makedirs(config_dir, exist_ok=True)

    # Set benchmark value in config file
    data = {'benchmark': {'bench_value': bench_value.decode('utf-8').strip()}}
    with open(CONFIG, 'w') as f:
        json.dump(data, f)

    # Set file permissions for regular user access
    os.chmod(CONFIG, 0o644)

    print(f"\033[1mBenchmark value set to: ", bench_value.decode('utf-8').strip())


if __name__ == "__main__":
    benchmarker()