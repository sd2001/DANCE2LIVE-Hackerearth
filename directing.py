import os
import pandas as pd
import shutil
data=pd.read_csv(r'DanceForms/train.csv')
train_img_dir='DanceForms/train'

#print(data.head(10))


for i in os.listdir(train_img_dir):
    for img in data['Image']:
        if str(i)==str(img):
            name=data.loc[data['Image']==img]
            dance_name=(str(name['Target'].item()))
            mov_dir=os.path.join('Forms',dance_name)
            shutil.move(os.path.join(train_img_dir,img),mov_dir)
            
    
            
