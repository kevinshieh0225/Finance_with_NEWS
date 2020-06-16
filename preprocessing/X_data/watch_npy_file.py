import numpy as np
import os.path

path = './save_topic_training_data.npy'
"""
save = {}
np.save(path,save)
y = np.load(path).item()
print(y)
dict.update(y,{'12':40})
np.save(path,y) #save the new"""
c = np.load(path)
#print(c)
print(type(c))
print(c.item().get('20160312').shape)