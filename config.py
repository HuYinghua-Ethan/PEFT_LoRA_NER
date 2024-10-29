# -*- coding: utf-8 -*-

"""
配置参数信息
"""

Config = {
    "model_path": "model_output",
    "schema_path": "./ner_data/schema.json",
    "train_data_path": "ner_data/train",
    "valid_data_path": "ner_data/test",
    "vocab_path":"chars.txt",
    "max_length": 100,
    "hidden_size": 256,
    "num_layers": 2,
    "epoch": 30,
    "batch_size": 16,  # 16
    "optimizer": "adam",
    "learning_rate": 1e-3,   # 1e-3 / 1e-5
    "dropout": 0.1,
    "use_crf": False,
    "class_num": 9,
    "tuning_tactics":"lora_tuning",  # 大模型微调策略 lora_tuning/p_tuning/prompt_tuning/prefix_tuning
    "bert_path": r"D:\2024 AILearning\BaDou_Course\Practical_Project\lora+bert+ner\bert-base-chinese"
}

