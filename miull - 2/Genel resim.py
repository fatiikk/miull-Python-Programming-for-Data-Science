import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 750)
df = sns.load_dataset("titanic")
df.head()

def check_df(dataframe, head=5):
    print("##### shape ####")
    print(dataframe.shape)
    print("##### type ####")
    print(dataframe.dtypes)
    print("##### head ####")
    print(dataframe.tail(head))
    print("##### NA ####")
    print(dataframe.isnull().sum())

check_df(df)