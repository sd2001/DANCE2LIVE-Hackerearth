import os
dance_dir='Forms'
for i in os.listdir(dance_dir):
    c=0
    for i2 in os.listdir(os.path.join(dance_dir,i)):
        c+=1
    print(i," : ",c)