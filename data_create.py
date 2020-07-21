import os
import cv2
#from keras.utils import np_utils
from sklearn import preprocessing 

dataset = []
data_dir=r'E:\Dance-hackerearth\Forms'
for directory in os.listdir(data_dir):
    path = os.path.join(data_dir, directory)
    if not os.path.isdir(path):
        continue
    for item in os.listdir(path):
        # to make sure no hidden files get in our way
        if item.startswith("."):
            continue
        img = cv2.imread(os.path.join(path, item))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (200, 200))
        dataset.append([img, directory])
        
#print(dataset[:10])

data,labels=zip(*dataset)

label_encoder = preprocessing.LabelEncoder() 
labels= label_encoder.fit_transform(labels) 

#print(labels)