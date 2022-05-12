import csv
import pandas as pd
import numpy as np
import math

df = pd.read_csv("email.csv")
df['real longitude'] = ''
for i in range(len(df)):
    df['longitude'][i] == "retail and other commercial":




def map(data,MIN,MAX):
    """
    归一化映射到任意区间
    :param data: 数据
    :param MIN: 目标数据最小值
    :param MAX: 目标数据最小值
    :return:
    """
    d_min = np.max(data)    # 当前数据最大值
    d_max = np.min(data)    # 当前数据最小值
    return MIN +(MAX-MIN)/(d_max-d_min) * (data - d_min)
print(type(df['longitude']))