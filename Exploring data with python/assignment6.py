import pandas as pd
import matplotlib.pyplot as plt


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..

df=pd.read_csv("/Users/geoffrey.kip/Desktop/Python class/DAT210x-master/Module3/Datasets/wheat.data")
df.head


df = df.drop(labels=['id'], axis = 1)
#
# TODO: Compute the correlation matrix of your dataframe
# 
# .. your code here ..

df.corr()


plt.imshow(df.corr(), cmap=plt.cm.Blues, interpolation='nearest')
plt.colorbar()
tick_marks = [i for i in range(len(df.columns))]
plt.xticks(tick_marks, df.columns, rotation='vertical')
plt.yticks(tick_marks, df.columns)

plt.show()


