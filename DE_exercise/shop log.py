import csv
from faker import Faker
import random

fake = Faker()

num_records = 100

product_names = ['bananas','coconuts','oranges','sugar_candy','peaches','apricots','drinks']

file_path = "D:\Python\DE\shop_log.csv"

with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)   
    writer.writerow(['product_name', 'quantity', 'price', 'date'])
    
    for _ in range(num_records):        
        product_name = random.choice(product_names)        
        quantity = random.randint(10, 500)
        price = random.randint(5, 100)
        timestamp = fake.date_this_month().isoformat()
        
        writer.writerow([product_name, quantity, price, timestamp])

print(f"Сгенерировано {num_records} записей и сохранено в {file_path}")