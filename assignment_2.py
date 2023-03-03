#!/usr/bin/env python
# coding: utf-8

# In[24]:


import numpy as np
import pandas as pd


# In[25]:


matrix = np.array([[1,2,3], [4,5,6]])
matrixA = 2 * matrix
print(matrixA)


# In[26]:


identity_matrix = np.identity(3)
print(identity_matrix)


# In[27]:


array1 = np.arange(28)
print(array1)


# In[28]:


array2 = array1.reshape(2,2,7)
print(array2)


# In[29]:


array_1 = np.arange(1,7).reshape(2,3)
array_2 = np.arange(7,13).reshape(2,3)
print(array_1)
print(array_2)


# In[30]:


horizontal_stack = np.hstack((array_1,array_2))
vertical_stack = np.vstack((array_1,array_2))
print("Horizontal Stack")
print(horizontal_stack)
print("Vertical Stack")
print(vertical_stack)


# In[31]:


sequence = np.arange(0,105,5)
print(sequence)


# In[32]:


students =pd.DataFrame({'Names':["Joel","George","James","Grace","Edwina"]})
print(students)


# In[34]:


team_names = ["Aduana Stars","Accra Hearts of Oaks","Kumasi Asante Kotoko","Bechem United","Accra Lions","Bibiani Gold Stars",
             "Berekum Chelsea","Medeama","Dreams FC","FC Samartex","Accra Great Olympics","Real Tamale United",
            "Nsoatreman","Legon Cities","Karela United","King Faisal","Tamale City","Kotoku Royals"]

goals_scored = [[0,0,1,0,2,2,1,1,0,0,1,1,0,1,1,0,1,3],
                [2,0,0,3,1,0,1,2,1,3,0,0,0,0,0,0,1,1],
                [0,3,0,0,2,2,1,0,2,2,1,0,2,1,2,1,0,1],
                [2,0,4,0,0,2,1,2,1,0,1,1,0,3,0,1,3,0],
                [1,0,0,6,3,2,1,3,0,0,0,2,2,0,1,2,0,3]]

teams = {'Teams':team_names, 'Match 1':goals_scored[0], 'Match 2':goals_scored[1], 'Match 3':goals_scored[2],
           'Match 4':goals_scored[3], 'Match 5':goals_scored[4]}
teams_1 = pd.DataFrame(teams)


# In[35]:


west_africa_countries = ["Ghana","Nigeria","Cote d'Ivoire","Niger","Burkina Faso","Mali","Senegal",
                        "Guinea","Benin","Togo","Sierra Leone","Liberia","Mauritania","Gambia","Guinea Bissau","Cape Verde"]

capital = ["Accra","Abuja","Yamoussoukro","Niamey","Ouagadougou","Bamako","Dakar","Conakry","Porto-Novo",
           "Lome","Freetown","Monrovia","Nouakchott","Banjul","Bissau","praia"] 

population = [31.07,206.14,26.38,24.21,20.90,20.25,16.74,13.13,12.12,8.28,7.98,5.06,4.65,2.42,1.97,0.55]

countries = pd.DataFrame({'Countries':west_africa_countries, 'Capital City':capital, 'Population(in millions)':population})
countries


# In[36]:


data = {1:{'Team':'Hearts of Oak','GF':120,'GA':35,'PTS':80}, 2:{'Team':'Asante kotoko','GF':90,'GA':55,'PTS':60},
       3:{'Team':'Ebusua Dwarfs','GF':90,'GA':60,'PTS':60}, 4:{'Team':'Sekondi Hassacas','GF':80,'GA':43,'PTS':55},
       5:{'Team':'Okwahu United','GF':78,'GA':39,'PTS':53}, 6:{'Team':'Tano Bofoakwa','GF':70,'GA':50,'PTS':49},
       7:{'Team':'BA United','GF':71,'GA':55,'PTS':44}}
data = pd.DataFrame(data )
data


# In[37]:


for key, value in data.items():
    print(f"{value['Team']}: GF = {value['GF']}, GA = {value['GA']}, PTS = {value['PTS']}")


# In[38]:


for key, value in data.items():
    if value['GA'] > 30: 
        print(pd.DataFrame(value))


# In[39]:


for key, value in data.items():
    if value['GF'] < 80:
        print(pd.DataFrame(value))


# In[40]:


for key, value in data.items():
    if value['PTS'] < 60:
        print(pd.DataFrame(value))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




