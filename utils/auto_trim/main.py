"""
For microprocessor, the number of blocklists can be too large to be processed by the cpu.
So this module trims the blocklists to a certain value (using benchmark module)so that the microprocessor can work efficiently.
Total IP to be added to the firewall = bench_value * trimmed_value_constant
"""

import json
import os 

CONFIG_BENCHMARK='configurations/benchmark_config.json'
CONFIG_AUTOTRIM='configurations/auto_trim_config.json'


def trim():
    # check if auto_trim is enabled
    with open(CONFIG_AUTOTRIM) as f:
        data_auto_trim = json.load(f)
    if data_auto_trim['auto_trim'] == False:
        return
    
    with open(CONFIG_BENCHMARK) as f:
        data_benchmark = json.load(f)
    
    TRIMMED_VALUE_CONSTANT = data_auto_trim['trimmed_value_constant']
    bench_value = float(data_benchmark['benchmark']['bench_value'])

    TRIMMED_CNT = int(bench_value*TRIMMED_VALUE_CONSTANT)
    
    #blocklists folder
    csvs_folders = './data'

    total_files = 0
    for root, dirs, files in os.walk(csvs_folders):
        for file in files:
            if file.endswith('.csv'):
                csv_dir = os.path.join(root, file)
                total_files += 1

    TRIMMED_CNT_PER_FILE=int(TRIMMED_CNT/total_files)
    for root, dirs, files in os.walk(csvs_folders):
        for file in files:
            if file.endswith('.csv'):
                csv_dir = os.path.join(root, file)
                # Trim csv file
                with open(csv_dir, 'r') as f:
                    lines = f.readlines()
                    trimmed_lines = lines[:TRIMMED_CNT_PER_FILE]

                with open(csv_dir, 'w') as f:
                    f.writelines(trimmed_lines)

                line_count = len(trimmed_lines)
                print(f"File: {csv_dir}, Line Count: {line_count}")

if __name__=='__main__':
    trim()