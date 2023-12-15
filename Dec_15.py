#!/usr/bin/env python
# coding: utf-8

# # Tuples
# 

# In[10]:


## Declaration 
## Tuples are immutable they cant change their value
t=(1,2,3,'abc',3.5)
print(t)
t[3:5]


# In[12]:


t1=((1,2,3),(4,5,6))
print(t1[0][2])


# In[ ]:


# format()
# capitalize()
# isalnum()
# isalpha()
# islower()
# isupper()
# lower()
# upper()
# isnumeric()
# count(value,start,stop)
# find(value,start,stop) ## If it doesnt exits in string returns -1 
# index(value,start,stop)## If it doesnt exits in string returns error
# split(separator,maxsplit) ## Default space
# strip()## Default space
#       Strip method removes any characters from the begining and the end of the string 
# translate()
#   maketrans('what to transform','with what' , 'what to remove')
# """


# ## Iteration

# In[14]:


for i in t:
    print(i)
print()
for i in range(len(t)):
    print(t[i])


# In[23]:


## We can concatenation
t1=(1,2,3,4)
t2=(1,2,3,3)
t=t1+t2
print(t)


# In[24]:


## comparing Two tuples
print(t1<t2)


# In[33]:


a=(1,2,3)
b=('a','b','c')## String and int can't be compared
print(a<b)
print(ord('#'))## ord returns asci value of charcter


# In[42]:


a=(1,2)
b=(0,0,3)
print(a<b)
print(ord('A'))


# In[43]:


print('A'<'65')


# ## Tuple Method

# In[49]:


# 1)count()
# 2)index()

help(tuple.count)

help(str.count)
help(tuple.index)


# In[78]:


s="abcaaa"
print(s.count('a'))
t=('a','t','t','t')
t[1]=0
print(t)
print(t.count('t'))


# In[62]:


help(tuple)
# underscore vada functiomns magic functions che ene call na karva pade e pote aai jai


# In[63]:


help(str)


# In[66]:


tup=(1,2,3)
del(tup)


# In[71]:


t1=((1,2,3),(3,4))
t=t1+tuple('abc')
print(t)


# In[72]:


"""WAP to find the sum of odd and even numbers in a tuple"""
t=(1,2,3,4,5,6,7,8,9,10)
even_sum=odd_sum=0
for i in range(len(t)):
    if t[i]%2==0:
        even_sum+=t[i]
    else:
        odd_sum+=t[i]
print("EVEN",even_sum)
print("ODD",odd_sum)


# #    UNIT-5   MUTABLE DATA STRUCTURES

# ### Lists
# 
# 

# In[77]:


# lists are exactly like array
# lists are mutable l[]=empty list

# 1.They are ordered index=0,1 or -1 -2 etc
# 2.Slicing possible
# 3.Also allows duplicates just like tuples
# 4.MUTABLE we can change a particular value in list

l=[1,2,3,'abc',True,3.5]
print(l)
l[2]=5
print(l)
li=list((1,2,3,4))
print(li)


# In[ ]:


Lists Methods/Functions

1.append()
2.clear()
3.copy()
4.count()
5.index() # Returns error 
6.extend() # we can add tuples also and added as individual element 
7.insert(pos,elmnt) pos=position elmnt=element
8.remove(index) 
9.reverse() # index ma element ni value pass karvani reverses the list [l.sort(reverse=True)]
10.sort(reverse,key) #reverse-dec ma sort karva Key-used to sort it using length of string 
11.pop(pos) # Position apya vagar pop karisu to last element remove thase


# In[82]:


l=[1,2,3]
l.append(4)
print(l)
l.append([1,2,3,6,7,8])
print(l)


# In[4]:


l1=[1,2,3]
print(l1)
l1.clear()
print(l1)
l3=[]
print(l3)


# In[87]:


l=[1,2,3]
l2=l[:] # here [:] means slice change nai thai
l3=l.copy()
l[1]=4
print(l)
print(l2)
print(l3)


# In[127]:


l=[1,2,3,1,2,3,4,1,1,1]
l.count(1)


# In[93]:


l.index(4)


# In[120]:


l=[1,2,3]
l.extend([4]) #agar khali 4 add kaarie emnem then nai thai extend but append etle add thase
l.append(5)
print(l)


# In[121]:



l.insert(1,0)
print(l)


# In[126]:


a=l.pop()
print(a)
print(l)
l.remove(1)
print(l)


# In[138]:


l=[1,2,3,1,2,3,4]
print(l[::-1])
l1=[2,3,5,4]
l1.reverse()
print(l1)


# In[84]:


help(list)


# In[8]:


# """WAP to accept i and j from the user as matrix rows and colums and wap to add the two matrixes"""
# i=int(input("Enter number of rows :"))
# j=int(input("Enter number of colums :"))
# l1=[]
# l2=[]
# print("enter elements of MAT -1")
# for a in range(i*j):
#     x=int(input("Enter  element of matrix 1 :"))
#     l1.append(x)

# print("enter elements of MAT -2")
# for a in range(i*j):
#     x=int(input("Enter  element of matrix 1 :"))
#     l2.append(x)
# print("ADDED matrix")
# l3=[]
# for i in range(len(l1)):
#     x=l1[i]+l2[i]
#     l3.append(x)

# print("ADDED: ",l3)

AA 1-D MA THAYO MATRIX NAI BANYO AA
   
    


# In[18]:


r=int(input("Enter number of rows :"))
c=int(input("Enter number of colums :"))
mat1=[]
mat2=[]
print("MAT-1")
for i in range(r):
    mat1.append([])
    for j in range(c):
        el=int(input("Insert element "))
        mat1[i].append(el)
print("MAT-2")
for i in range(r):
    mat2.append([])
    for j in range(c):
        el=int(input("Insert element "))
        mat2[i].append(el)
mat3=[]
for i in range(r):
    mat3.append([])
    for j in range(c):
        el=mat1[i][j]+mat2[i][j]
        mat3[i].append(el)


print(mat1)
print(mat2)
print(mat3)
for i in range(r):
    print()
    for j in range(c):
        print(mat3[i][j],end="  ")


# In[1]:


l=[4,2,5,6,1,3]
l.sort()
print(l)


# In[3]:


l=[1,5,9,7,4,2,3]
l.sort(reverse=True)
print(l)


# In[5]:


cars=['Volvo','kia','Hyundai','BMW','Audi','VM']
# Length wise sort karva Func banai ne key ma value apvani
def fun(e):
    return len(e)
cars.sort(reverse=True,key=fun)
print(cars)


# ## List Comprehension

# In[ ]:





# In[7]:


fruits=['apple','bananas','cherry','kiwi','mango']
newlist=[]
for x in fruits:
    if 'a' in x:
        newlist.append(x)
print(newlist)


# In[8]:


newlist=[x for x in fruits if 'a' in x] #[x-variable for x in fruits-loop  if 'a' in x-condition] ---List comprehension 
print(newlist)


# ## Data Structures and Dictionaries

# In[ ]:


1. Key value pairs
Dictionary-ordered since cersion 3.7


Functions:
    1.
    2.
    3.


# In[15]:


D={'a':123,'b':245,'c':567,'a':222}
d=dict(name='john',age=35,height=6.4)
print(D)
print(d)
D['b']=333
print(D)


# In[90]:


help(dict)


# In[19]:


## Iteration
D={'a':123,'b':245,'c':567,'a':222}
for i in D:
    print(i)
    print(D[i])
D={'a':[10,20,30,40],'b':{'a':20,'d':30,'c':40}}
print(D['a'][1])
print(D['b']['d'])


# In[35]:


s="This is a string. It shows that this string is iterable."
s=s.lower()
print(s)
mytable=s.maketrans('','','.,?,!')
s=s.translate(mytable)
print(s)
a=s.split(" ")
print(a)
word_count={}
for word in s.split():
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
print(word_count)



    
    


# In[39]:


D={'a':20,'b':30,'c':40}
print(D)
D.clear()
print(D)


# In[44]:


D={'a':20,'b':30,'c':40}
a=D.copy()
print(a)


# In[75]:


D={'a':20,'b':30,'c':40}
s=D.get('m',50) # returns none when key not foun
print(s)
print(D)


# In[85]:


help(dict.values)


# In[50]:


D={'a':20,'b':30,'c':40}
D.keys()#a set-like object providing a view on D's keys


# In[57]:


D={'a':20,'b':30,'c':40}
D.pop('F')# if key not found then keyError Occurs
print(D)


# In[87]:


D={'a':20,'b':30,'c':40}
D.popitem()# if item passed then TypeError Ocuurs


# In[89]:


D={'a':20,'b':30,'c':40}
z=D.setdefault('f',60)
print(z)
print(D)


# In[84]:


D={'a':20,'b':30,'c':40}
D.update({1:'maths'})
print(D)


# In[86]:


D={'a':20,'b':30,'c':40}
D.values()


# In[91]:


D={'a':20,'b':30,'c':40}
x=D.values()
D['a']=30
print(D)
print(x)


# In[8]:


l=[]

while True:
    e=input('Enter a number or stop :')
    if e=='stop':
        break
    else:
        l.append(e)
print(l)
D={}
for i in l:
    if i not in D:
        D[i]=[i]
        #D[i].append(i)
    else:
        D[i].append(i)
    print(D)
l1=list(D.items())
def func(t):
    return len(t[1])
l1.sort(reverse=True,key=func)
d1=dict(l1)
print(d1)


# # SETS

# In[ ]:


# Duplication not allowed
# Unchangable 
# Unordered
# Half muttable
# Frozenset: u cant add or remove completely immutable


# In[17]:


s={1,3,5,6,4,7,8,9}
print(s)
s[0]=5
se=set((1,2,3,4,5))
se


# In[10]:


myset=frozenset([1,3,4,5])
myset.add(5)


# In[69]:


x={1,2,3}
y={1,2,3}
print(x.issubset(y))
print(y.issuperset(x))
print(x.union(y))
print(x.intersection(y))
print(y.difference(x))
print(y.symmetric_difference(x))
print(x.copy())
x.add(1)
y.remove(4)
print(x)
print(y)


# In[23]:


help(set)


# In[41]:


# WAP to check if a string contains all unique characters.
s='aabcd'
x=set((s))
if len(x)==len(s):
    print("All are unique")
else:
    print("NOO")
print(x)


# In[ ]:


317 WAP to change the first half of the String into upper case
320 wap to check if 2 strings are balanced or not S1 and S2 are balanced 
if all the characters of s1 are s2 charcters podition 
doent matter
325 WAp to shift decimal digits  n places to the left wrapping the extra digits around if shift is
grater than num of digits then rev the string


# In[68]:


s='Jeel'
b=tuple(s)
print(b)
a=len(s)
c=(a//2)
q=[]
for i in range (0,c):
    q.append(b[i].upper())
print(q)
for i in range(c,len(s)):
     q.append(b[i])
print(q)
qw=''
for i in range (len(s)):
    qw+=(q[i])
print(qw)
    


# In[80]:


s1='jeel'
s2='pala'
set1=set(s1)
set2=set(s2)
s=''
if len(s1)==len(s2):
    print("balanced")
else:
    
    print("Not balance")
#         for i in range(len(s1)):
#             q=set1.difference(set2)
#             print(q)
#             s+=q[i]

            
        
    


# In[ ]:


325 WAp to shift decimal digits  n places to the left wrapping the extra digits around if shift is
grater than num of digits then rev the string


# In[ ]:


# 327 : min 8 char 
#     atleast one from a-to z
#     atleast one from A to Z
#     atleast one from 0-9
#     one special char _ or @ or $
    

while True:
    
    flag_li=False
    flag_d=flag_u=flag_l=flag_sp=False
   
    pwd=input("Enter the Pass  : ")
    if len(pwd)>=8:
        flag_li=True
        
    
    for i in range(len(pwd)):
        if pwd[i]=='@' or pwd[i]=='_' or pwd[i]=='$':
            flag_sp=True
        if pwd[i].isdigit()==True:
            flag_d=True
        if pwd[i].isupper()==True:
            flag_u=True
        if pwd[i].islower()==True:
            flag_l=True
#     print(flag_li)
#     print(flag_d)
#     print(flag_u)
#     print(flag_l)
#     print(flag_sp)
    if flag_li and flag_d and flag_u and flag_l and flag_sp:
        
        print("Pass Verified")
    else:
          print("Enter valid pass")
        
        


# In[ ]:


QB:330
    

