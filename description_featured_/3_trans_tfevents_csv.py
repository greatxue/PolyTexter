import os
import csv
from tensorboard.backend.event_processing import event_accumulator

# 指定包含 .tfevents 文件的目录路径
logdir = '/home/wenhao/Project/greatxue/polyTexter/proj/lfs/checkpoints/description_norm_241022/model_0/trainer_logs/version_0/events.out.tfevents.1729627942.maxwell.cs.unc.edu'
output_csv = 'output.csv'

# 加载事件文件
event_acc = event_accumulator.EventAccumulator(logdir)
event_acc.Reload()  # 解析事件文件

# 获取所有标量的标签（例如 'train_loss', 'val_accuracy' 等）
tags = event_acc.Tags()['scalars']

# 打开一个 CSV 文件写入标量数据
with open(output_csv, mode='w', newline='') as file:
    writer = csv.writer(file)
    # 写入 CSV 文件头：Step, 标签, 值
    writer.writerow(['step', 'tag', 'value'])
    
    # 遍历所有标量标签并导出数据
    for tag in tags:
        scalar_events = event_acc.Scalars(tag)
        for event in scalar_events:
            # 每个事件记录包含步骤（step）、标签（tag）和标量值（value）
            writer.writerow([event.step, tag, event.value])

print(f"Scalars data exported to {output_csv}")