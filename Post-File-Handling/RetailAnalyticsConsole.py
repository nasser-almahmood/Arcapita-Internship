
import csv
data_all = []
cleaned_data = []
unique_orders = []
unique_customers = []
unique_custs = []
last_maxc = []
minmax =[]

frequency = []
unique_customers_dict = {}

monetary = {}

skipped = 0
loaded = 0
with open('./retail.csv', 'r') as csv_file:
    
    read = csv.reader(csv_file)
    next(read)
    head = True
    count = 0
    for row in read:
            try:
                date = list(row[1].split('-'))
                row[1] = date
                data_all.append(row)
            except:
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

unique_customers = []
revenue = 0
uorders = 0
ucustomers = 0
aov = 0
for row in cleaned_data:
    try:
        revenue += float(row[4]) * float(row[5])
        if row[0] not in unique_orders:
            uorders += 1
            unique_orders.append(row[0]) 
        if row[2] not in unique_customers:
            ucustomers += 1
            unique_customers.append(row[2])
    except:
        continue
aov = round(revenue / uorders, 2)
revenue = round(revenue, 2)
        


def back():
    backs = True
    while backs == True:
        print('\n- Click ENTER to get back to MAIN MENU -\n')
        back = input()
        if back == '':
            backs = False
        else:
            backs = True

def load_csv():
    print('\n---------------------------')
    print('Loaded', loaded, 'rows :)')
    print('Skipped', skipped, 'rows :(')
    print('---------------------------\n')

def KPIs():
    print('\n---------------------------------------')
    print(' KPIs:')
    print('---------------------------------------')
    print('Revenue:    ', revenue)
    print('Orders:     ', uorders)
    print('Customers:  ', ucustomers)
    print('AOV:        ', aov)
    print('---------------------------------------\n')

def compare_dates(date1, date2):
    if date1[0] > date2[0]:
        return date1
    elif date1[0] < date2[0]:
        return date2
    else:
        if date1[1] > date2[1]:
            return date1
        elif date1[1] < date2[1]:
            return date2
        else:
            if date1[2] > date2[2]:
                return date1
            else:
                return date2

def rfm():
# max dates for each customer
    a = ''
    for row in cleaned_data:
        if row[2] not in unique_custs:
            a = row[2]
            unique_custs.append({a: [int(row[1][0]), int(row[1][1]), int(row[1][2])]})
    for i in unique_customers:
        cmax = None
        for j in unique_custs:
            if not(i in j.keys()):
                continue
            if cmax == None:
                cmax = j[i]
                continue
            cmax = compare_dates(cmax, j[i])
        last_maxc.append([i, cmax])

# reference date
    max_date = None
    for row in cleaned_data:
        if max_date == None:
            max_date = row[1]
            continue
        max_date = compare_dates(max_date, row[1])
    max_date[2] = int(max_date[2]) + 1
    max_date[2] = str(max_date[2])

    
# now date for each customer + getting the diff between ref and said date and adding it to minmax list
    for row in last_maxc:
        now = int(row[1][0]) * 365 + int(row[1][1]) * 12 + int(row[1][2])
        ref = int(max_date[0]) * 365 + int(max_date[1]) * 12 + int(max_date[2]) + 1
        diff = ref - now
        minmax.append([row[0], diff])

    count = 0

    for item in unique_customers:
        # unique_customers_dict.append({item: []})
        unique_customers_dict[item] = []
        monetary[item] = []

    for customer in unique_customers_dict.keys() :
        for item in cleaned_data:
            if item[2] != customer:
                continue
            if item[0] not in unique_customers_dict[customer]:
                unique_customers_dict[customer].append(item[0])
    
    for customer in monetary.keys() :
        counts = 0
        for item in cleaned_data:
            if item[2] != customer:
                continue
            if item[2] not in monetary.keys():
                counts += float(item[4]) * float(item[5])
                monetary[customer].append(round(count, 2))
            else:
                counts += float(item[4]) * float(item[5])
                monetary[customer] = round(counts, 2)
# #medianr
    sum = 0
    count = 0
    for diffs in minmax:
        sum += int(diffs[1])
        count += 1
    medianr = sum / count

# medianf
    sum = 0
    count = 0
    for diffs in unique_customers_dict.values():
        sum += len([customer[0]])
        count += 1
    medianf = sum / count
# medianm
    sum = 0
    count = 0
    for diffs in monetary.values():
        sum += diffs
        count += 1
    medianm = round(sum / count, 2)
    
    
    print('\n-----------------------------------------------------------')
    print('              Referance Date:', max_date[0]+'-'+max_date[1]+'-'+max_date[2])
    print('-----------------------------------------------------------')
    print('Customer  R  F  M   Recency  Frequency  Monetary  Segment')
    spacea = 0
    spaceb = 0
    spacec = 0
    _111 = 0
    _110 = 0
    _101 = 0
    _100 = 0
    _011 = 0
    _010 = 0
    _001 = 0
    _000 = 0
    for customer in minmax:
        freq = len(unique_customers_dict[customer[0]]) 
        mon = monetary[customer[0]]
        spacea = 7 - len(str(customer[1]))
        spacesa = ' ' * spacea
        spaceb = 7 - len(str(freq))
        spacesb = ' ' * spaceb
        spacec = 9 - len(str(mon))
        spacesc = ' ' * spacec

       
        r = '0'
        f = '0'
        m = '0'
        if medianr >= customer[1]:
            r = '1'
        if medianf >= freq:
            f = '1'
        if medianm >= mon:
            m = '1'
        rfm_ = r+f+m
        if rfm_ == '111':
            _111 += 1
        if rfm_ == '110':
            _110 += 1
        if rfm_ == '101':
            _101 += 1
        if rfm_ == '100':
            _100 += 1
        if rfm_ == '011':
            _011 += 1
        if rfm_ == '010':
            _010 += 1
        if rfm_ == '001':
            _001 += 1
        if rfm_ == '000':
            _000 += 1

        print(customer[0],'    ',r,'',f,'', m,        '    ',customer[1],spacesa, freq, spacesb, mon, spacesc, rfm_)
    print('------------------------------------------------------------\n')
    print('--------------------------------------------------------------------')
    print('                      RFM Segment Counts:')
    print('--------------------------------------------------------------------')
    print('RFM Counts                  Insight')
    print("111  ",_111,"    [ Best customers (recent, frequent, high spend) :) ]")
    print("110  ",_110,"    [ Loyal but low spenders ]")
    print("101  ",_101,"    [ Big spenders but not frequent ]")
    print("100  ",_100,"    [ Recent but low frequency and spend ]")
    print("011  ",_011,"    [ Frequent and high spenders, but not recent ]")
    print("010  ",_010,"    [ Frequent only ]")
    print("001  ",_001,"    [ High spenders only ]")
    print("000  ",_000,"    [ At-risk (not recent, not frequent, low spend) :( ]")
    print('--------------------------------------------------------------------\n')

# def tops():


##### 'order_id': 0, 'date': 1, 'customer_id': 2, 'product': 3, 'price': 4, 'qty': 5 #####
run = True
while run == True:
    print('\n-------------------------------------------')
    print('        Retail Analytics Console')
    print('-------------------------------------------')
    print('(1) Load CSV')
    print('(2) KPIs (Revenue, Orders, Customers, AOV)')
    print('(3) RFM segmentation (per customer)')
    print('(4) Top products (by qty and by revenue) - Under construction -')
    print('(5) Basket pairs (support, confidence, lift) - Under construction -')
    print('(6) Monthly summary + dimple forecast - Under construction -')
    print('(7) Export reports (CSV) - Under construction -')
    print('(8) Exit\n')

    menu = input('~ ')

    if menu == '1':
        load_csv()
        print(cleaned_data)
        back()
        

    if menu == '2':
        KPIs()
        back()
        


    if menu == '3':
        rfm()
        back()

    # if menu == '4':



    # if menu == '5':


    # if menu == '6':


    # if menu == '7':


    if menu == '8':
        run = False