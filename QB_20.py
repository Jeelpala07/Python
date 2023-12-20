#!/usr/bin/env python
# coding: utf-8

# In[21]:


# # 409 Given a list L of size N, You need to count the number of special elements in the given list. An element is special if 
# removal of that element makes the list balanced.
# The list will be balanced if sum of even index elements is equal to the sum of odd index elements.
# Example Input
# Input 1:
# A = [2,1,6,4]
# Input 2:
# A=[5,5,2,5,8]
# Example Output
# Output 1:
# 1
# Output 2:
# 2

a=[2,1,6,4]
def F(l):
    while True:
        sum_even=0
        sum_odd=0
        for i in range(len(l)):

            if i%2==0:
                sum_even+=l[i]
            else:
                sum_odd+=l[i]
        print(sum_even)
        print(sum_odd)
def Func(L):
    special_count=0
    for i in range(len(L)):
        temp_list=L[:i]+L[i+1:]
        if F(temp_list):
            special_count+=1
            print("Orignal List :{}",L)
Func(a)
    
    


# In[35]:


r=int(input("Enter Rows"))
c=int(input("Enter Cols"))
mat1=[]
mat2=[]
for i in range(r):
    mat1.append([])
    for j in range(c):
        e=int(input("Enter Element : "))
        mat1[i].append(e)
print(mat1)
for i in range(r):
    for j in range(i+1,c):
        TEMP=mat1[i][j]
        mat1[i][j]=mat1[j][i]
        mat1[j][i]=TEMP
print(mat1)
for i in range(r):
    mat1[i].reverse()
        
print(mat1)
for i in range(r):
    print()
    for j in range(c):
        print(mat1[i][j] ,end=" ")
        
        


# In[4]:


## WAP such that if an element in m*n matrix is 0 then its entire row and element becomes zero
r=int(input("Enter Rows"))
c=int(input("Enter Cols"))
mat1=[]
rr=[]
cc=[]

for i in range(r):
    mat1.append([])
    for j in range(c):
        e=int(input("Enter Element : "))
        mat1[i].append(e)
for i in range(r):
    print()
    for j in range(c):
        print(mat1[i][j] ,end=" ")
for i in range(r):
    for j in range(c):
        if mat1[i][j]==0:
            rr.append(i)
            cc.append(j)
# print()
# print("list")
# print(rr)
# print(cc)

for n in range(len(rr)):
    for i in range(r):
        for j in range(c):
            if i == rr[n] or j == cc[n]:
                mat1[i][j] = 0

print()     
print()
for i in range(r):
    print()
    for j in range(c):
        print(mat1[i][j] ,end=" ")
        


# In[9]:


# Assume u have a methos subString which checks if one word is sunstring of another given two string s1 and s2 
# write code to check if s2 is a rotation of s1 using only one call to substring 
# Eg "WaterBottle" --- "erBottleWat"
def is_substring(string,sub):
    return string.find(sub) !=-1
def string_rotation(s1,s2):
    if len(s1)==len(s2)!=0:
        return is_substring(s1+s1,s2)
    return False
string_rotation('waterbottle','erbott')


# In[ ]:




