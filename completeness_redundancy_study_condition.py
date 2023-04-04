import pandas as pd 
import matplotlib.pyplot as plt 


df = pd.read_table('SGB15132_bin_data.tsv',header= 0)
df2 = pd.read_table('SGB15132_metadata.tsv',header= 0)

####### completeness
min_completeness = df['completeness'].min()
avg_completeness = df['completeness'].mean()
max_completeness = df['completeness'].max()
print('{} \t {} \t {}'.format('min','avg','max'))
print('{} \t {} \t {}'.format(min_completeness,avg_completeness,max_completeness))

df.plot(kind='bar', x= 'bin', y='completeness')
plt.ylim(95,100)
plt.legend()
plt.title('completeness of MAGs')
plt.savefig('completeness_distribution.png')
plt.show()
plt.close()
 
############ redundancy
min_redundancy = df['redundancy'].min()
avg_redundancy = df['redundancy'].mean()
max_redundancy = df['redundancy'].max()

print('{} \t {} \t {}'.format('min','avg','max'))
print('{} \t {} \t {}'.format(min_redundancy,avg_redundancy,max_redundancy))


############ Study condition 

total = df2['study_condition'].count()
stud_cond = df2['study_condition'].value_counts() / total
mylabels = ['control', 'hypertension','AS','adenoma','pre-hypertension','cirrhosis']
myexplode = [0.2, 0, 0, 0, 0, 0]

plt.pie(stud_cond,labels= mylabels, explode = myexplode, shadow = True)
plt.show()
plt.savefig('Study_condition.png')
plt.close()




