import numpy as np

#%%

a = np.array([1,2,3,4,5,6])
print(a)

#%%

b = np.array([1,2,3,4,5,6])
print(b)

print(a+b)

#%%
list1 = [1,2,3,4,5,6]
print(list1)

#%%
list2 = [1,2,3,4,5,6]
print(list2)

print(list1+list2)

#%%

temp = np.array([10,20,30,50])

temp_fer = temp* 1.8 +32
print(temp_fer)

#%%
print(a.shape)

#%%

m1 = np.array([[1,2,3],
              [5,6,7]])

m2 = np.array([[4,5,6],
              [1,2,3]])

print(m1)
print(m2)

print(m1+m2)

#%%

m3 = m1+m2
m4 = m1-m2
m5 = m1*m2
m6 = m1/m2

print(m3)
print(m4)
print(m5)
print(m6)

#%%


m1 = np.array([[1,2,3],
              [5,6,7]])


m7 = m1[0,:]
print(m7)

#%%

# slice the last row and last two colomn

m8 = m1[-1,-2:]
print(m8)

#%%

m9 = np.array([[1,2,3,4],
               [50,56,95,8],
               [100,3,20,65]])

bool_idx = (m9 % 2 == 0)

print(bool_idx)

print(m9[bool_idx])
#%%

print(m9[m9 % 2 == 0])

#%%


print(np.add(m1,m2))

print(np.subtract(m1,m2))
print(np.multiply(m1,m2))
print(np.divide(m1,m2))

print(np.sqrt(m1))



#%%

x = np.array([[1,2],
              [3,4]])

y = np.array([[5,6],
              [7,8]])

print(x.dot(y))

#%%
print(np.dot(x,y))
print(x@y)
print(np.matmul(x,y))

#%%

def matrix_mul(x,y):
    result = np.array([[0,0],[0,0]])
    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                result[i][j] += x[i][k] * y[k][j]
    return result

print(matrix_mul(x, y))

#%%

v1 = np.array([1,2,3]) #i +2j + 3k
v2 = np.array([-1,3,-2]) #-i -3j +2k

print(np.dot(v1,v2))

#%%

j = np.array([[1,2],
              [3,4],
              [5,6]])
print(np.dot(v1,j))

j_trans = np.transpose(j)
print(np.dot(j_trans,v1))

#%%

d1 = np.arange(29)
print(d1)
print(np.average(d1))


#%%

d2 = np.arange(12).reshape(4,3)
print(d2)

#%%
print(np.average(d2, axis = 0)) # col wise
print(np.average(d2, axis = 1)) # row wise


#%%

print(np.sum(d2))

#%%
print(np.sum(d2, axis = 0))
print(np.sum(d2, axis = 1))

#%%
z = np.zeros((3,3))

print(z)

ran = np.random.rand(3,3)
print(ran)
#%%
z1 = np.linspace(1, 100,10).reshape(5,2)
print(z1)

#%%
z2 = np.eye(4)
print(z2)

#%%


d2 = np.arange(12).reshape(4,3)


v3 = np.array([10,20,30])
Z = d2+v3
print(Z)


#%%

v3 = np.array([10,20,30,40])
Z = np.transpose(d2)+v3
print(Z)

#%%

import matplotlib.pyplot as plt

#%%
x = np.array([10,15,20])
y = np.array([5,9,7])

plt.plot(x,y,"ro")

plt.xlabel('x-axix')
plt.ylabel('Frequency')

plt.title("hello")

#%%
x1 = np.arange(6)
print(x1)

freq = np.linspace(20,50,6)
print(freq)

ticklable = ['ban', 'ind', 'pak', 'sir', 'mal', 'jap']
plt.bar(x1, freq, tick_label = ticklable, width=0.8)

plt.xlabel('x-axix')
plt.ylabel('Frequency')

plt.title("bar chart")
plt.show()