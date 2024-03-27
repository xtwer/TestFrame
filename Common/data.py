# 封装测试数据读取方法
import pandas as pd

def read_excel(file,**kwargs):
    data_dict = []
    try:
        data = pd.read_excel(file,**kwargs)
        data_dict = data.to_dict('records')
    except Exception as e:
        # 如果发生异常，打印错误信息并返回空列表
        print(f"An error occurred: {e}")
    finally:
        return data_dict

# 调用写好的方法,打印数据:
sheet1 = read_excel('测试data.xlsx')
sheet2 = read_excel('测试data.xlsx',sheet_name='Sheet2')
print(sheet1)
print(sheet2)