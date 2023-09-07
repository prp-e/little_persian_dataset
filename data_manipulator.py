import os
import pandas as pd

raw_file_name = "raw_data.txt"
train_file_name = "train.txt"
val_file_name = "val.txt"
vocab_file_name = "vocab.txt"

input_data = pd.read_csv('tasnim.csv')

input_data_list = []

for row in input_data.iterrows():
    datum = row[1]['body']
    datum = str(datum)
    input_data_list.append(datum)

resulting_text = '\n'.join(input_data_list)

raw_file = open(raw_file_name, 'w', encoding='utf-8')
raw_file.write(resulting_text)
raw_file.close()

print("Raw data has been written successfully.")

vocab = set(resulting_text)

vocab_file = open(vocab_file_name, 'w', encoding='utf-8')

for c in vocab:
    vocab_file.write(c + '\n')

vocab_file.close()

print("Vocab context window has been written successfully.")

split_index = int(0.9 * len(resulting_text))

train_split = resulting_text[:split_index]
val_split = resulting_text[split_index:]

train_file = open(train_file_name, 'w', encoding='utf-8')
train_file.write(train_split)
train_file.close()

print("Training data has been written successfully.")