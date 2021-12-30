#!/usr/bin/env python
# coding: utf-8

# In[83]:


import numpy as np


# In[84]:



azul = [('b'+str(x)) for x in range(10)]
verde = [('g'+str(x)) for x in range(10)]
amarelo = [('y'+str(x)) for x in range(10)]
branco = [('w'+str(x)) for x in range(10)]
vermelho = [('r'+str(x)) for x in range(10)]
laranja = [('o'+str(x)) for x in range(10)]
p = [['.......', '.......', 'branco','.......', '.......'],
            ['.......', '.......', 'amarelo','.......', '.......'],
            ['vermelho', 'verde' , 'azul', 'vermelho', 'verde'], 
            ['.......', '.......', 'branco', '.......', '.......'],
            ['.......','.......', 'amarelo', '.......', '.......']]


# In[85]:


cores = [vermelho, azul, branco, verde, amarelo, laranja]
for colour in cores:
    print(colour)
for po in p:
    print(po)


# In[86]:



face_azul = np.array([(azul[0], azul[1], azul[2]), 
                   (azul[3], azul[4], azul[5]),
                   (azul[6], azul[7], azul[8])])

face_vermelha = np.array([(vermelho[0], vermelho[1], vermelho[2]), 
                          (vermelho[3], vermelho[4], vermelho[5]), 
                          (vermelho[6], vermelho[7], vermelho[8])])
face_branca = np.array([(branco[0], branco[1], branco[2]), 
                          (branco[3], branco[4], branco[5]), 
                          (branco[6], branco[7], branco[8])])

face_verde = np.array([(verde[0], verde[1], verde[2]), 
                          (verde[3], verde[4], verde[5]), 
                          (verde[6], verde[7], verde[8])])

face_amarela = np.array([(amarelo[0], amarelo[1], amarelo[2]), 
                          (amarelo[3], amarelo[4], amarelo[5]), 
                          (amarelo[6], amarelo[7], amarelo[8])])

face_laranja = np.array([(laranja[0], laranja[1], laranja[2]), 
                          (laranja[3], laranja[4], laranja[5]), 
                          (laranja[6], laranja[7], laranja[8])])
print(face_branca)


# In[87]:


# correspondencias
# FRONTEIRAS
# amarelo
# laranja - azul - vermelho - verde - laranja
# branco
#
# QUINAS
# azul[8] = vermelho[6] = branco[2]
# azul[6] = lanraja[8] = branco[0]
# azul[2] = vermelho[0] = amarelo[8]
# azul[0] = lanraja[2] = amarelo[6]

# verde[8] = lanraja[6] = branco[6]
# verde[6] = vermelho[8] = branco[8]
# verde[2] = laranja[0] = amarelo[0]
# verde[0] = vermelho[2] = amarelo[2]

# BORDAS
# azul[1] = amarelo[7]
# azul[5] = vermelho[3]
# azul[7] = branco[1]
# azul[3] = laranja[5]

# vermelho[1] = amarelo[5]
# vermelho[7] = branco[5]
# laranja [1] = amarelo[3]
# laranja[7] = branco[3]

# verde[1] = amarelo[1]
# verde[5] = laranja[3]
# verde[7] = branco[7]
# verde[3] = vemelho[5]

# CENTRAL
# azul[4], vermelho[4], branco[4], verde[4], amarelo[4], laranja[4]


# In[88]:


def girar(face):
    np.rot90(face)
    saved_w1 = face_branca[0, 0]
    saved_w2 = face_branca[0, 1]
    saved_w3 = face_branca[0, 2]
    
    saved_r1 = face_vermelha[0, 0]
    saved_r2 = face_vermelha[1, 0]
    saved_r3 = face_vermelha[2, 0]
    
    saved_y1 = face_amarela[2, 0]
    saved_y2 = face_amarela[2, 1]
    saved_y3 = face_amarela[2, 2]
    
    saved_o1 = face_laranja[0, 2]
    saved_o2 = face_laranja[0, 2]
    saved_o3 = face_laranja[2, 2]
    
    # fix this below:
    face_branca[0, 0] = face_laranja[0, 2]
    face_branca[0, 1] = face_laranja[1, 2]
    face_branca[0, 2] = face_laranja[2, 2]

    face_vermelha[0, 0] = face_branca[0, 2]
    face_vermelha[1, 0] = face_branca[1, 2]
    face_vermelha[2, 0] = face_branca[2, 2]

    face_amarela[2, 0] = face_vermelha[0, 0]
    face_amarela[2, 1] = face_vermelha[1, 0]
    face_amarela[2, 2] = face_vermelha[2, 0]

    face_laranja[0, 2] = face_amarela[2, 0]
    face_laranja[1, 2] = face_amarela[2, 1]
    face_laranja[2, 2] = face_amarela[2, 2]
    # until here


# In[89]:


#print(face_azul)
print(face_vermelha)
#print(face_laranja)
print(face_branca)
#print(face_amarela)


# In[90]:


girar(face_azul)

print(face_vermelha)


# In[ ]:





# In[ ]:




