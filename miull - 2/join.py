import numpy as np
import pandas as pd

m = np.random.randint(1,30, size=(5,3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99

pd.concat([df1, df2])


pd.concat([df1, df2], ignore_index=True)

#merge

df3 = pd.DataFrame({"employees": ["john", "dennis", "mark"],
                    "group": ["accounting", "engineering", "engineering"]})
df4 = pd.DataFrame({"employees": ["john", "dennis", "mark"],
                    "start": [2010,2002,2008]})

pd.merge(df3, df4)
