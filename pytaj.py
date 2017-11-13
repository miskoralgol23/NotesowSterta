

with open('pytania.txt','r') as f:
    a_list = f.readlines()

import random as rnd
print(rnd.sample(a_list,1))
