#kategorik değişken : sütün. countplot, barplot
# Sayısal değişken : histogram , boxplot
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 750)
df = sns.load_dataset("titanic")
df.head()

df["sex"].value_counts().plot(kind="bar")
plt.show()


# SAYISAL


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 750)
df = sns.load_dataset("titanic")
df.head()

plt.hist(df["age"])
plt.show()

plt.boxplot(df["fare"])
plt.show()

# ÖZELLİKLERİ
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 750)

x = np.array([1, 8])
y = np.array([0,150])

plt.plot(x,y)
plt.show()

plt.plot(x,y, "o")
plt.show()


# marker

y = np.array([13,28,11,100])
plt.plot(y, marker="o")
plt.show()

# line

y = np.array([13,28,11,100])
plt.plot(y, linestyle="dashdot")
plt.show()

# multiple lines

x = np.array([23,18,31,10])
y = np.array([13,28,11,100])
plt.plot(x)
plt.plot(y)
plt.show()

# isimlendirme

plt.title (" bu ana başlık OLACAK ")
plt.xlabel(" X ekseninin isimlendirmesi ")
plt.ylabel( " Y ekseni isimlendirmesi ")

#subplot

plt.subplot(1,2,1)
plt.title ( " 1 GRAFİK ")
plt.plot(x,y)

plt.subplot(1,2,2)
plt.title ( " 2 GRAFİK ")
plt.plot(x,y)