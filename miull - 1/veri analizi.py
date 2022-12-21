import numpy as np
a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])

# numpy hali
a = np.array([1,2,3,4])
b = np.array([2,3,4,5])
a*b

#array oluşturöa
np.array([1,2,3,4,5])
type(np.array([1,2,3,4,5]))

np.zeros(10, dtype=int)
np.random.randint(0,10,size=10)
np.random.normal(10,4,(3,4))

#array özellikleri

a = np.random.randint(10,size=5)
a.ndim
a.shape
a.size
a.dtype

#reshaping

np.random.randint(1,10, size=9)
np.random.randint(1,10, size=9).reshape(3,3)

#index seçimi

a = np.random.randint(10, size=10)
a[0]
a[0:5]
a[0] = 999

m = np.random.randint(10, size=(3, 5))

m[0,0]
m[1,1]
m[2,3]
m[2,3] = 999

m[2,3] = 2.9

m[:,0]
m[1,:]
m[0:2, 0:3]

#fancy

v = np.arange(0,30,3)
v[1]
v[4]
catch = [1,2,3]

v[catch]

#koşullu işlemler

v = np.array([1,2,3,4,5])

"""ab = []
for i in v:
    if i < 3:
        ab.append(i)
"""
v[v < 3]
v[v > 3]
v[v != 3]
v[v == 3]

#matematiksel işlemler

v = np.array([1,2,3,4,5])
v / 5
v * 5 / 10
v ** 2
v - 1

a = np.array([[1,-1],[1,1]])
b = np.array([20,10])
np.linalg.solve(a,b)

