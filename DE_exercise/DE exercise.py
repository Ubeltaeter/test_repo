from csv import DictReader
from itertools import groupby
from operator import itemgetter
import operator

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style 

def read_sales_data(file_path):
    with open(file_path, 'r') as f:
     
        dict_reader = DictReader(f)
        list_of_dict = list(dict_reader)
        return list_of_dict

def total_sales_per_product(sales_data):
    # Списое продаж сортирован по продуктам
    sorted_data = sorted(sales_data, key=itemgetter('product_name'))    
    
    # Результирующий словарь
    result = {}
    
    # Группировка словарей по продукту
    for key, group in groupby(sorted_data, key=itemgetter('product_name')):
        # Вычисление суммы продаж по продукту
        total_product = sum(int(item['quantity']) * int(item['price']) for item in group)
        result[key] = total_product
    return result

def sales_over_time(sales_data):
    # Списое продаж сортирован по дате
    sorted_data = sorted(sales_data, key=itemgetter('date'))    
    
    # Результирующий словарь
    result = {}
    
    # Группировка словарей по продукту
    for key, group in groupby(sorted_data, key=itemgetter('date')):
        # Вычисление суммы продаж по продукту
        total_product = sum(int(item['quantity']) * int(item['price']) for item in group)
        result[key] = total_product
    return result    

my_dict = read_sales_data('D:\Python\DE\shop_log.csv')

# Максимальные значения по продукту и дню
print(max(total_sales_per_product(my_dict).items(), key=operator.itemgetter(1)))
print(max(sales_over_time(my_dict).items(), key=operator.itemgetter(1)))

# Графики распределений по дням и продуктам
plt.style.use('dark_background')
width = 0.75 
fig, (f1, f2) = plt.subplots(2)
f1.barh(total_sales_per_product(my_dict).keys(), total_sales_per_product(my_dict).values(), width, color='yellow')
f1.set_title('Общая сумма продаж по каждому продукту')
f2.barh(sales_over_time(my_dict).keys(), sales_over_time(my_dict).values(), width, color='blue')
f2.set_title('Общая сумма продаж по каждому дню')
fig.tight_layout()

plt.show()