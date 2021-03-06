import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="ticks",color_codes=True)
titanic=sns.load_dataset("titanic")
p1=sns.countplot(x="who",hue="alone",data=titanic)
p1.set_title("Plot For Counting")
plt.show()