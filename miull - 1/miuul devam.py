[salary * 2 for salary in salaries]

[salary * 2 for salary in salaries if salary < 3000]

[salary * 2 if salary < 3000 else salary * 0 for salary in salaries]

[salary * 2 if salary < 3000 else salary * 0 for salary in salaries]

students = ["jhon", "mark", "venessa"]

students_no = ["jhon", "venessa"]

[student.lower() if student in students_no else student.upper() for student in students]


dict = {"a" :1,
        "b" :2,
        "c" :3,}

{k.upper(): v ** 2 for (k, v) in dict.items()}

numbers = range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2

{n : n ** 2 for n in numbers if n % 2 == 0}



import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns
A= []
for col in df.columns:
    print(col.upper())
    A.append(col.upper())
df.columns = A

[col for col in df.columns if "INS" in col]

["FLAG_" + col for col in df.columns if "INS" in col]

df.columns = ["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns ]


import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

num_cols = [col for col in df.columns if df[col].dtype != "O"]
soz = {}
agg_list = ["mean", "min", "max", "sum"]

for col in num_cols:
    soz[col] = agg_list

new_dict2 = {col: agg_list for col in num_cols}
df[num_cols].head()

df[num_cols].agg(new_dict2)


