import csv

count_list = []
count_sum = 0

f = csv.reader(open('flightlist_20190801_20190831.csv','r'))

with open('demo.csv', 'w',encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')

    for i in f:
        if count_sum < 1002:
            writer.writerow(i)
            count_sum = count_sum + 1

