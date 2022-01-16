#Steps Involved In Data Visualization
#Step 1. Import libraries
import seaborn as sns
import matplotlib.pyplot as plt

#Step 2. Set Theme
sns.set_theme(style="ticks", color_codes=True)

#Step3. Import data set. We can also import our own data.
kashti=sns.load_dataset("titanic")
#print(kashti)
#Here,we load dataset(titanic) from seaborn library.

#Step4. Plot Basics Graph here(Count plot for 1 variable)
p=sns.countplot(x="sex", data=kashti)
#count plot is used to show frequency of variables like gender(male,female).
plt.show()

#Step5. Plot Basics Graph here(Count plot for 2 variable)
p=sns.countplot(x="sex", data=kashti,hue="class")
p.set_title("Count Plot for 2 variables")
plt.show()