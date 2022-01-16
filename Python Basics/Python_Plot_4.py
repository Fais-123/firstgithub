import seaborn as sns
import matplotlib.pyplot as plt
from numpy import mean


#load dataset


sns.set_style(style=None , rc=None)

kashti=sns.load_dataset("titanic")


#Draw line plot
sns.barplot(x="class",y="fare",hue="sex",data=kashti,estimator=mean)
plt.show()