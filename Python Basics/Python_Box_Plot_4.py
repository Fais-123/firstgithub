import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")
#By using different datset name tips realted to hotel data
tips=sns.load_dataset("tips")
#print(tips)
#print(tips.describe())
#how to manage individual color fro each hue?
#By using palette we did that here.
sns.boxplot(x="tip",y="day",data=tips,hue="smoker",orient="h",palette={"Yes":"yellow","No":"pink"})
plt.show()