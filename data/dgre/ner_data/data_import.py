import json
import random

input_file_path = 'data_train.jsonl'
train_output_file_path = 'train.jsonl'
dev_output_file_path = 'dev.jsonl'

# 读取输入文件中的所有记录
with open(input_file_path, 'r', encoding='utf-8') as file:
    data = [json.loads(line) for line in file]

# 计算80%的训练数据和20%的验证数据数量
total_records = len(data)
train_size = int(total_records * 0.8)
dev_size = total_records - train_size

# 随机抽取训练数据和验证数据
random.shuffle(data)
train_data = data[:train_size]
dev_data = data[train_size:]

# 将训练数据写入到 train.json1 文件中
with open(train_output_file_path, 'w', encoding='utf-8') as file:
    for record in train_data:
        file.write(json.dumps(record, ensure_ascii=False) + '\n')

# 将验证数据写入到 dev.json1 文件中
with open(dev_output_file_path, 'w', encoding='utf-8') as file:
    for record in dev_data:
        file.write(json.dumps(record, ensure_ascii=False) + '\n')