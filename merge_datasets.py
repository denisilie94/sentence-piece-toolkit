import json
import pandas as pd

from tqdm import tqdm


ccnet_input_files = [

]

n_cultura_x_files = 64
output_file = './data/data_all.txt'

for input_file in tqdm(ccnet_input_files):
    print(input_file)

    with open(input_file, 'r') as in_file:
        with open(output_file, 'a') as out_file:
            for line in in_file:
                data = json.loads(line)
                data = data['raw_content']
                out_file.write(data)
 
for idx_cultura_x_file in tqdm(range(n_cultura_x_files)):
    input_file = f'./data/cultura-x/ro_part_{idx_cultura_x_file:05}.parquet'
    df = pd.read_parquet(input_file, engine='pyarrow')

    with open(output_file, 'a') as out_file:
        for index, row in df.iterrows():
            text = row['text']
            out_file.write(text)   
