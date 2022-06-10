import os
import numpy as np
import shutil
from os.path import exists

path_annotations = '/mnt/datosnas/Users/cmejia/EMOTION-DETECTION/AFFECTNET-raw/train_set/annotations/'
path_images = '/mnt/datosnas/Users/cmejia/EMOTION-DETECTION/AFFECTNET-raw/train_set/images/'
path_target = '/mnt/datosnas/Users/cmejia/EMOTION-DETECTION/AFFECTNET/train_set/'
i=0
j=0
for file in os.listdir(path_annotations):
    name1, name2 = file.split('_')
    if(name2 == 'exp.npy'):
        category = np.load(path_annotations + file)
        original = path_images + name1 + ".jpg"
        target = path_target + str(category) + "/" + name1 + ".jpg"
        print("Verificando " + target)
        if not exists(target):
            shutil.move(original, target)
            print("Moving " + original + " to " + target)
            #input()
            i=i+1
            print("Moved: " + str(i))
        j=j+1
        print("Verificados: " + str(j))
