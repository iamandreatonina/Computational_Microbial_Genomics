import pandas as pd 
import matplotlib.pyplot as plt
from statistics import mean

dic = {}
with open('dataframe_input.tsv') as file:
    for line in file.readlines():
        val = line.split(':')
        if val[0] == 'dataframe_input.tsv':
            continue
        elif val[0] not in dic:
            dic[val[0]] = list()
            dic[val[0]].append(int(val[1].rstrip()))
        else:
            dic[val[0]].append(int(val[1].rstrip()))
### the first values rappresent hypothetical proteins, the seconds are the CDS and the thirds are non hypothetical proteins (so knowns proteins)
# the key are the MAGs of our uSGB

df = pd.DataFrame.from_dict(dic,orient='index',columns = ['hypothetical proteins','CDS','knowns protein'])

## PRINTS

print('{}'.format('\nhypothetical proteins'))
print('max : {}\t avg : {}\t min : {}'.format(df['hypothetical proteins'].min(), round(df['hypothetical proteins'].mean(),1), df['hypothetical proteins'].max()))


print('{}'.format('\nCDS'))
print('max : {}\t avg : {}\t min : {}'.format(df['CDS'].min(), round(df['CDS'].mean(),1), df['CDS'].max()))


print('{}'.format('\nknown protein'))
print('max : {}\t avg : {}\t min : {}'.format(df['knowns protein'].min(), round(df['knowns protein'].mean(), 1), df['knowns protein'].max()))


## PLOT

df.plot(kind = 'line')
plt.xticks(ticks= range(32),labels= range(32),rotation = 90)
plt.show()
plt.legend()
plt.close()