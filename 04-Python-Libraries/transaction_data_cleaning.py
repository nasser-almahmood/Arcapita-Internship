import re
import datetime
import pandas as pd
df = pd.read_csv("transactions.csv")
new_df = df.dropna()
drop_ind = []
dic = {}

pattern = r'(?P<year>\d{4})[/-](?P<month>\d{2})[/-](?P<day>\d{2})'
           
for index, row in new_df.iterrows():

    match = re.match(pattern, row['date'])
    if not match:
        drop_ind.append(index)
        continue

    date = match.groupdict()

    if int(date['year']) < 1999 or int(date['year']) > 2025:
        drop_ind.append(index)
        continue
    if int(date['month']) < 1 or int(date['month']) > 12:
        drop_ind.append(index)
        continue
    if int(date['day']) < 1 or int(date['day']) > 31:
        drop_ind.append(index)
        continue
    try:
        if float(row['price']) <= 0 or int(row['qty']) < 0:
            drop_ind.append(index)
            continue
    except:
        drop_ind.append(index)
        continue

# for index, row in new_df.iterrows():
#     if 


new_df = new_df.drop(drop_ind)

# for row in new_df:




    # print("Row Index:", index)
    # print("Name: ",row['price'])
    # print("-" * 20)