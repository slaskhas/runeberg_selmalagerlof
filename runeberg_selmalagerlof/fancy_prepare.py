import os
import requests
import tiktoken
import numpy as np

# download the tiny strindberg dataset
input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
#if not os.path.exists(input_file_path):
#    data_url = 'https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt'
#    with open(input_file_path, 'w') as f:
#        f.write(requests.get(data_url).text)

with open(input_file_path, 'r') as f:
    data = f.read()
n = len(data)

train_data = []
val_data = []

for i in range(10):
    ix = i+1
    chunk = data[int((ix-1)*n/10):int(ix*n/10)]
    cn = len(chunk)
    train_data += chunk[:int(cn*0.9)]
    val_data += chunk[int(cn*0.9):]

train_data = "".join(train_data)
val_data = "".join(val_data)

# encode with tiktoken gpt2 bpe
enc = tiktoken.get_encoding("gpt2")
train_ids = enc.encode_ordinary(train_data)
val_ids = enc.encode_ordinary(val_data)
print(f"train has {len(train_ids):,} tokens")
print(f"val has {len(val_ids):,} tokens")

# export to bin files
train_ids = np.array(train_ids, dtype=np.uint16)
val_ids = np.array(val_ids, dtype=np.uint16)
train_ids.tofile(os.path.join(os.path.dirname(__file__), 'train.bin'))
val_ids.tofile(os.path.join(os.path.dirname(__file__), 'val.bin'))

# train has 641,641 tokens
# val has 69,892 tokens
