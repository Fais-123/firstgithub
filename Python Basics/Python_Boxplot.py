from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

#Load dataset
kashti=sns.load_dataset("titanic")
kashti

sns.boxplot(x="survived",y="age",showmeans=True,meanprops={"marker":"*","markeredgecolor":"red","markersize":"12"},data=kashti)
#Show labels
plt.xlabel("How many survived"),
plt.ylabel("age(years"),
plt.title("Box Plot for survived People on Titanic",size=10,weight="bold")


plt.show()



