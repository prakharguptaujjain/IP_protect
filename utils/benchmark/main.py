import os
import json
import subprocess

CONFIG='./configurations/bechmark_config.json'


def benchmarker():
    #Download Benchmark
    print("Downloading Benchmark. Please wait (this might take a while)")
    exit_code = os.system("bash ./utils/benchmark/installer.sh")
    if exit_code != 0:
        print("Failed to install benchmark.")
        exit(1)
    else:
        print(f"\033[1mBenchmark installed successfully.\033[0m")

    # Do benchmark
    bench_value = subprocess.check_output("sysbench cpu --cpu-max-prime=20000 --time=5 run | grep 'events per second' | awk '   {print $NF}'", shell=True)
    
    #create config file if it doesn't exist
    if not os.path.exists(CONFIG):
        with open(CONFIG, 'w') as f:
            json.dump({'benchmark':{}}, f)

    # Load the configuration from the .json file
    with open(CONFIG, 'r') as f:
        data = json.load(f)
        
    # Set benchmark value in config file
    data['benchmark']['bench_value'] = bench_value.decode('utf-8').strip()
    with open(CONFIG, 'w') as f:
        json.dump(data, f)
    print(f"\033[1mBenchmark value set to: ", bench_value.decode('utf-8').strip())

if __name__ == "__main__":
    benchmarker()