#!/usr/bin/env python
# coding: utf-8

# # Python: List & Generator Comprehensions - Illustrations

# You can also get this tutorial and run it on your laptop:
# 
#     git clone https://github.com/kshitijzutshi/Python-comprehensions.git
# 
# Install IPython and Jupyter:
# 
# with [conda](https://www.anaconda.com/download):
# 
#     conda install ipython jupyter
# 
# with pip:
# 
#     # first, always upgrade pip!
#     pip install --upgrade pip
#     pip install --upgrade ipython jupyter
# 
# Start the notebook in the tutorial directory:
# 
#     cd ipython-in-depth
#     jupyter notebook
# 
# 

# In[ ]:


nums = [1,2,3,4,5,6,7,8,9,10]


# In[ ]:


# I want 'n' for each 'n' in nums
my_list=[n for n in nums]
print(my_list)


# In[ ]:


# I want 'n*n' for each 'n' in nums
my_list=[n*n for n in nums]
print(my_list)


# In[ ]:


# Using a map + lambda
my_list = map(lambda n: n*n, nums)
print my_list


# In[ ]:


# I want 'n' for each 'n' in nums if 'n' is even
my_list=[n for n in nums if n%2==0]
print(my_list)


# In[ ]:


# Using a filter + lambda
my_list = filter(lambda n: n%2 == 0, nums)
print my_list


# In[ ]:


# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
my_list=[(letter,num) for letter in 'abcd' for num in range(4)]
print(my_list)


# In[ ]:


# Dictionary Comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# zip function in python creates a tuple in a list for the given lists as arguments in the zip(list1,list2) function
print zip(names, heros)


# In[ ]:


# I want a dict{'name': 'hero'} for each name,hero in zip(names, heros)
my_dict={name:hero for name,hero in zip(names,heros)}
print(my_dict)


# In[ ]:


# If name not equal to Clark
my_dict={name:hero for name,hero in zip(names,heros) if name!='Clark'}
print(my_dict)


# In[ ]:


# Set Comprehensions
nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
my_set = set()
for n in nums:
    my_set.add(n)
print my_set


# In[ ]:


my_set={n for n in nums}
print(my_set)


# In[ ]:


# Generator Expressions
# I want to yield 'n*n' for each 'n' in nums
nums = [1,2,3,4,5,6,7,8,9,10]

def gen_func(nums):
    for n in nums:
        yield n*n

my_gen = gen_func(nums)

for i in my_gen:
    print i


# In[ ]:


my_gen=(n for n in  nums)
for i in my_gen:
    print i


# In[ ]:




