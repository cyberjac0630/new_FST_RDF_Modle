import csv

count_list = []
count_sum = 0

f = csv.reader(open('flightlist_20190801_20190831.csv','r'))
for i in f:
    if len(i) > 5:
        if i[4] not in count_list and i[5] != '':
            print(i[5])
            count_list.append(i[5])#指定列
            count_sum = count_sum + 1

print(count_sum)
