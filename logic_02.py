#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np


# In[16]:


# arrays IDs
red = [('r'+str(x)) for x in range(9)]
blue = [('b'+str(x)) for x in range(9)]
white = [('w'+str(x)) for x in range(9)]
green = [('g'+str(x)) for x in range(9)]
yellow = [('y'+str(x)) for x in range(9)]
orange = [('o'+str(x)) for x in range(9)]


# In[17]:


colours = [red, blue, white, green, yellow, orange]
for item in colours: print(item)


# In[18]:


# creating each face from cube
face_blue = np.array([(blue[0], blue[1], blue[2]), 
                      (blue[3], blue[4], blue[5]),
                      (blue[6], blue[7], blue[8])])

face_red = np.array([(red[0], red[1], red[2]), 
                     (red[3], red[4], red[5]), 
                     (red[6], red[7], red[8])])

face_white = np.array([(white[0], white[1], white[2]), 
                       (white[3], white[4], white[5]), 
                       (white[6], white[7], white[8])])

face_green = np.array([(green[0], green[1], green[2]), 
                       (green[3], green[4], green[5]), 
                       (green[6], green[7], green[8])])

face_yellow = np.array([(yellow[0], yellow[1], yellow[2]), 
                        (yellow[3], yellow[4], yellow[5]), 
                        (yellow[6], yellow[7], yellow[8])])

face_orange = np.array([(orange[0], orange[1], orange[2]), 
                        (orange[3], orange[4], orange[5]), 
                        (orange[6], orange[7], orange[8])])


# In[23]:


def girar(face):
    np.rot90(face)
    # backup
    saved_w1 = face_white[0, 0]
    saved_w2 = face_white[0, 1]
    saved_w3 = face_white[0, 2]
    
    saved_r1 = face_red[0, 0]
    saved_r2 = face_red[1, 0]
    saved_r3 = face_red[2, 0]
    
    saved_y1 = face_yellow[2, 0]
    saved_y2 = face_yellow[2, 1]
    saved_y3 = face_yellow[2, 2]
    
    saved_o1 = face_orange[0, 2]
    saved_o2 = face_orange[1, 2]
    saved_o3 = face_orange[2, 2]
    
    # giro dos quinas/cantos
    
    face_white[0, 0] = saved_o1
    face_white[0, 1] = saved_o2 
    face_white[0, 2] = saved_o3

    face_red[0, 0] = saved_w3
    face_red[1, 0] = saved_w2
    face_red[2, 0] = saved_w1

    face_yellow[2, 0] = saved_r1
    face_yellow[2, 1] = saved_r2
    face_yellow[2, 2] = saved_r3

    face_orange[0, 2] = saved_y1
    face_orange[1, 2] = saved_y2
    face_orange[2, 2] = saved_y3
    


# In[ ]:





# In[20]:


print(face_blue, '\n')
print(face_red, '\n')
print(face_orange, '\n')
print(face_white, '\n')
print(face_yellow)


# In[21]:


girar(face_blue)


# In[22]:


print(face_blue, '\n')
print(face_red, '\n')
print(face_orange, '\n')
print(face_white, '\n')
print(face_yellow)


# In[ ]:




