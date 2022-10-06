import datetime
import os
import time
import numpy as np
import csv

csvpath = os.getcwd() + '/csv_datas/'

if not os.path.exists(csvpath):
    os.mkdir(csvpath)

dt_now = datetime.datetime.now()

csv_data = []

for n in range(0, 3, 1):

    dt_now = datetime.datetime.now()

    dt_now_str = dt_now.strftime('%Y/%m/%d %H:%M:%S')

    # print(dt_now_str)
    file = []
    file = [dt_now_str, 1, 2, 3]
    # print(file)
    csv_data.append(file)

    print(csv_data)
    time.sleep(1)

with open(csvpath + 'csv_data' + '.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)



