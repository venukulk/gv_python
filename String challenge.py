#!/usr/bin/env python
# coding: utf-8

# In[4]:


#1.swap case 

s="Pythonist 2"


# In[39]:


def swapcase(s):
    #print(s)
    changed_str=''
    #charlist=s.split()
    for c in s:
        #print(c)
        if c.isupper() == True:            
            #print("upper")
            c=c.lower()
            changed_str=changed_str+c
        elif c.islower() == True:
            #print("lower")
            c=c.upper()
            changed_str=changed_str+c
        else:
            changed_str=changed_str+c
    return changed_str


# In[40]:


swapcase(s)


# In[1]:


# 2. split and join line

def splitandjoin(line):
    wordsplit=line.split()
    joined_string='-'.join(wordsplit)
    return joined_string

splitandjoin("Modi is great")


# In[3]:


#What's Your Name?

def print_full_name(first, last):
    sent=f"hello {first} {last}.you are just delved into python."
    #print(sent)
    return sent
print_full_name("prabhas","kulkarni")


# In[4]:


def mutate_string(string, position, character):
    st=string[:position]+character+string[position:]
    
    return st


# In[6]:


mutate_string("fghjk",1,'p')


# In[ ]:




