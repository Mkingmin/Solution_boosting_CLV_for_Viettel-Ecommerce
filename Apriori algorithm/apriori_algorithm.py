#import librabries
import IPython
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

## Nhập các file chi tiết đơn hàng và item
df = pd.read_csv("order_details.csv")
df_item = pd.read_csv("items.csv")

# Tạo bảng đến số lượng sản phẩm trên một order
df_order = df.groupby('order_id')['id'].count().reset_index()
df_order = df_order[df_order['id']>1]

df2 = df.merge(df_order,on='order_id',how='inner')

# tạo bảng chi tiết đơn hàng với thông tin sản phẩm
df_detail = df2.merge(df_item, left_on='item_id', right_on='id', how='left')

#Build model Apriori
# import thư viện chứa thuật toán apriori
from mlxtend.frequent_patterns import association_rules, apriori
# Tạo bảng đơn hàng với các danh mục sản phẩm
transactions_str = df_detail.groupby(['order_id', 'category'])['item_id'].count().reset_index(name ='Count')
my_basket = transactions_str.pivot_table(index='order_id', columns='category', values='Count', aggfunc='sum').fillna(0)

def encode(x):
    if x<=0:
        return 0
    if x>=1:
        return 1

# applying the function to the dataset

my_basket_sets = my_basket.applymap(encode)
frequent_items = apriori(my_basket_sets, min_support = 0.01,use_colnames = True)
rules = association_rules(frequent_items, metric = "lift", min_threshold = 0.1)
rules.sort_values('confidence', ascending = False, inplace = True)
rules.sort_values('confidence', ascending=False)
rules[rules['lift']>1.4]