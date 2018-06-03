import argparse
import csv
import json
import yaml

parser = argparse.ArgumentParser()
parser.add_argument('--format', help='Downloaded file format',
                    default=csv)
args = parser.parse_args()
file_format = args.format

file_name = "ratings.list.gz."
with open(file_name + "txt", 'r') as f:
    file_content = f.read()

if file_format == 'csv':
    with open(file_name + "csv", 'w') as f:
        writer = csv.writer(f)
        writer.writerow(file_content)

if file_format == 'json':
    with open(file_name + "json", 'w') as f:
        json.dump(file_content, f)

if file_format == 'yaml':
    with open(file_name + "json", 'w') as f:
        yaml.dump(file_content, f)
