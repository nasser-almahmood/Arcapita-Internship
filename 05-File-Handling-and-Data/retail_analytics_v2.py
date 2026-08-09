import csv
import os
data_all = []
cleaned_data = []
unique_orders = []
unique_customers = []
unique_custs = []
last_maxc = []
minmax =[]

frequency = []

skipped = 0
loaded = 0
csv_path = os.path.join(os.path.dirname(__file__), "retail.csv")

with open(csv_path, 'r', newline='', encoding='utf-8') as csv_file:
    read = csv.reader(csv_file)
    next(read)  # Skip header
    for row in read:
        try:
            date = list(row[1].split('-'))
            row[1] = date
            data_all.append(row)
        except Exception:
            skipped += 1
            continue
for row in data_all:
    try:
        if (
            len(row[0]) == 4 
            and len(row[1][0]) == 4 
            and len(row[1][1]) == 2 
            and 0 < int(row[1][1]) <= 12 
            and len(row[1][2]) == 2 
            and 0 < int(row[1][2]) <= 31 
            and float(row[4]) > 0 
            and int(row[5]) >= 1
            ):
            loaded += 1
            cleaned_data.append(row)
        else:
            skipped += 1
            continue
    except:
         skipped += 1
         continue


print(cleaned_data)