import pandas as pd 
import matplotlib.pyplot as plt 


df = pd.read_table('SGB15132_bin_data.tsv',header= 0)

df.plot(kind='bar', x= 'bin', y='completeness')
plt.ylim(95,100)
plt.legend()
plt.title('completeness of MAGs')
plt.savefig('completeness_distribution.png')
plt.show()
plt.close()

