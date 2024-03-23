# 封装测试数据读取方法
import pandas as pd

def read_excel(file,**kwargs):
    data_dict = []
    try:
        data = pd.to_dict('records')
    finally:
        return data_dict