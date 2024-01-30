import os
import glob
import json


input_dir = './wiki-data'
output_file = 'romanian_wiki_text.txt'

with open(output_file, 'w', encoding='utf-8') as outfile:
    files = glob.glob(os.path.join(input_dir, '**'), recursive=True)
    files = [file for file in files if os.path.isfile(file)]
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as infile:
            for line in infile:
                try:
                    json_data = json.loads(line)
                    text = json_data['text']
                    outfile.write(text + '\n')
                except json.JSONDecodeError:
                    continue

print("Merging completed.")
