import seaborn as sns
import matplotlib.pyplot as plt


#load dataset(iris dataset contain info about flowers)
phool=sns.load_dataset("iris")
#print(phool)

#Change figure
plt.figure(figsize=(5,5))

#Draw Bar plot
sns.barplot(x="species",y="petal_length",data=phool)

plt.show()