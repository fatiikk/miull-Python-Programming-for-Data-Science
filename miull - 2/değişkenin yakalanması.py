import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")
df.head()
df.info()

#docstring

def grab_col_names(dataframe, cat_th=10, car_th=20):
    """


    Parameters
    ----------
    dataframe : dataframe
        değişken isimleri alınmak istenen dataframe
    cat_th: int, float:
        numerik fakat kategorik olan

    car_th: int, float:
        kategorik fakat kardinal olan

    Returns
    -------
    cat_cols : list
    num_cols : list
    cat_but_car : list

    Notes
    -------


    """
    cat_cols = [col for col in df.columns if str(df[col].dtypes in ["category", "object", "bool"])]
    num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int","float"]]
    cat_but_car = [col for col in df.columns if
                   df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    num_cols = [col for col in df.columns if df[col].dtypes in ["int","float"]]
    num_cols = [col for col in num_cols if col not in cat_cols]

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f"cat_cols: {len(cat_cols)}")
    print(f"num_cols: {len(num_cols)}")
    print(f"cat_but_car: {len(cat_but_car)}")
    print(f"num_but_cat: {len(num_but_cat)}")

    return cat_cols, num_cols, cat_but_car

grab_col_names(df)