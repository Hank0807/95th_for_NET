import pandas as pd
import sys
import numpy as np
import datetime
import time
import re
import os

file_time = time.strftime("%Y-%m", time.localtime())
print ('file_time = ', file_time)


##########################################################
#
# Read the 95th log of the NNM monitor, and process data to CSV formate
#
##########################################################
df = pd.read_csv('/NNM_action/log/' + file_time + '.log')
data = df.groupby(['hostname', 'interface']).sum().sort_values(['duration'], ascending=False)
# print('data = ', data)
data.to_csv('/NNM_action/log/temp.csv', header=1)


##########################################################
#
# count the time with the same device and interface.
#
##########################################################
csv_data = []
ans_value = 0
count = 0
with open('/NNM_action/log/temp.csv', 'r+', encoding='UTF-8') as f:
    for line in f:
        count += 1
        if count == 1:
            continue
        # print('line = ', line, end='')
        pattern = '[0-9]+$'''
        ans = re.findall(pattern, line)
        # print('ans = ', ans[0])
        ans_value = int(ans[0])/1000
        # print('ans_index = ', ans.index('723721'))
        ans_str = str(datetime.timedelta(seconds=int(ans_value)))
        # print('ans_str = ', ans_str)
        csv_data.append(ans_str + '\t ====> ' + line.strip())


##########################################################
#
# record in the %date%-monitor.csv for history
# record in the monitor.csv for watch
#
##########################################################
# print('len(csv_data) = ', len(csv_data))
# print('csv_data = ', csv_data)
with open('/NNM_action/log/' + file_time + '-monitor.csv', 'w+', encoding='UTF-8') as r:
    for line in csv_data:
        print('line = ', line)
        r.write(line + "\n")

with open('/NNM_action/log/monitor.csv', 'w+', encoding='UTF-8') as r:
    r.write('Duration month is ' + file_time + '\n\n')
    for line in csv_data:
        # print('line = ', line)
        r.write(line + "\n")


# str(datetime.timedelta(seconds=666))
test = os.popen('ls -al').read()
