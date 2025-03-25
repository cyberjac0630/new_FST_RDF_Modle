import csv

count_list = []
count_sum = 0

f = csv.reader(open('flightlist_20190801_20190831.csv','r'))
for i in f:
    if i[0] not in count_list:
        # print(i[0])
        count_list.append(i[0])#指定列
        count_sum = count_sum + 1

print(count_sum)
