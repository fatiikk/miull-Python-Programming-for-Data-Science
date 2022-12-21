import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

df.iloc[0:3]
df.loc[0:3]

#df.iloc[0:3, "age"]
df.iloc[0:3, 0:3]
df.loc[0:3, "age"]
col_names = ["age", "embarked", "alive"]
df.loc[0:3, col_names]

#-----------------------------------------------------

import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

#50den büyük olanlar yaş
df[df["age"]>50].head()

df[df["age"]>50]["age"].count()

#yaşı 50 den büyük kişilerin classi nedir

df.loc[df["age"] > 50, ["age", "class"]].head()
#yaşı 50 den büyük erkek
df.loc[(df["age"] > 50) & (df["sex"] == "male"),
        ["age", "class","sex"]].head()


