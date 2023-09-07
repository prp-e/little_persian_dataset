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
