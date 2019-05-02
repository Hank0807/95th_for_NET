import pandas as pd
import sys
import numpy as np
import datetime
import re

df = pd.read_csv('/Users/admin/Downloads/2019-04.csv')
data = df.groupby(['hostname', 'interface']).sum().sort_values(['duration'], ascending=False)
# print('data = ', data)
data.to_csv('/Users/admin/Downloads/test.csv', header=1)

csv_data = []
ans_value = 0
count = 0
with open('/Users/admin/Downloads/test.csv', 'r+', encoding='UTF-8') as f:
    for line in f:
        count += 1
        if count == 1:
            continue
        print('line = ', line, end='')
        pattern = '[0-9]+$'''
        ans = re.findall(pattern, line)
        print('ans = ', ans[0])
        ans_value = int(ans[0])/1000
        # print('ans_index = ', ans.index('723721'))
        ans_str = str(datetime.timedelta(seconds=int(ans_value)))
        print('ans_str = ', ans_str)
        csv_data.append(line.strip() + ' ====> ' + ans_str)
# print('len(csv_data) = ', len(csv_data))
print('csv_data = ', csv_data)
with open('/Users/admin/Downloads/test_result.csv', 'w+', encoding='UTF-8') as r:
    for line2 in csv_data:
        print('line2 = ', line2)
        r.write(line2 + "\n")


# str(datetime.timedelta(seconds=666))