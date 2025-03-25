import csv
callsign_list = []
number_list = []
count_distance = 0

def Levenshtein_Distance(str1, str2):
    """
    计算字符串 str1 和 str2 的编辑距离
    :param str1
    :param str2
    :return:
    """
    matrix = [[i + j for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if (str1[i - 1] == str2[j - 1]):
                d = 0
            else:
                d = 1

            matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + d)

    return matrix[len(str1)][len(str2)]

f = csv.reader(open('flightlist_20190801_20190831.csv','r'))
for i in f:
    if i[0] not in callsign_list:
        callsign_list.append(str(i[0]))#指定列
    if i[1] not in number_list:
        number_list.append(str(i[1]))#指定列
print('reader check')

for j in callsign_list:
    for k in number_list:
        distance = Levenshtein_Distance(j, k)
        if distance <= 2:
            print(j, k)






print(Levenshtein_Distance("abc", "bd"))
