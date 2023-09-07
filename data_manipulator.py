import os
import pandas as pd

raw_file_name = "raw_data.txt"
train_file_name = "train.txt"
val_file_name = "val.txt"
vocab_file_name = "vocab.txt"

input_data = pd.read_csv('tasnim.csv')

input_data_list = []

for row in input_data.iterrows():
    input_data_list.append(row[1]['body'])

input_data_strs = []

for row in input_data_list:
    input_data_strs.append(str(row))

resulting_text = '\n'.join(input_data_strs)

raw_file = open(raw_file_name, 'w', encoding='utf-8')
raw_file.write(resulting_text)
raw_file.close()

print("Raw data has been written successfully.")