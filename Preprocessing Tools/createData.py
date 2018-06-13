import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append("/rhome/dshaw003/bigdata/caffe/caffe-master/python")
import caffe
import os
import h5py
import shutil
import tempfile
import sklearn
import sklearn.datasets
import sklearn.linear_model
import sklearn.cross_validation
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import roc_curve, auc
from sklearn import preprocessing
import pandas as pd

import random









file='./examples/dann/isogeneExprLabel_ERP000418_BP_0035914' 
auc_all=[];

example_set=np.loadtxt(file, dtype=float, delimiter="\t")
random.shuffle(example_set)

source_bags=example_set[0:20000,[13,14,15,16,17,18,19,20,21,22,13,14,15,16,17,18,19,20,21,22]]
target_bags = example_set[0:20000,[2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22]]
labels = example_set[0:20000,12]
labels[labels<1]=-1


#undersampling
print(source_bags.shape)
print(target_bags.shape)
print(labels[labels>0])

arr = [x for x in range(target_bags.shape[0])]   

rsample=random.sample(arr,18500) 
delsample=[]

for i in range(len(rsample)):
    if labels[rsample[i]]==1:
        delsample.append(i)
    
rsample=np.delete(rsample,delsample)  
    
source_data=np.delete(source_bags, rsample, 0)
target_bags=np.delete(target_bags,rsample,0)
source_labels=np.delete(labels,rsample,0)
target_labels=np.delete(labels,rsample,0)




print(source_data.shape)
print(target_bags.shape)
print(target_labels[target_labels>0])
 
  
target_data, test_data, target_labels, test_labels = sklearn.cross_validation.train_test_split(target_bags,target_labels)


print('Size of source, target and test')
print(source_data.shape)
print(target_data.shape)
print(test_data.shape)

lvsize=1;


# Write out the data to HDF5 files in a temp directory.
# This file is assumed to be caffe_root/examples/hdf5_classification.ipynb
dirname = os.path.abspath('./examples/dann/data/')
if not os.path.exists(dirname):
	os.makedirs(dirname)

source_filename = os.path.join(dirname, 'source.h5')
target_filename = os.path.join(dirname, 'target.h5')
test_filename = os.path.join(dirname, 'test.h5')


# HDF5DataLayer source should be a file containing a list of HDF5 filenames.
# To show this off, we'll list the same data file twice.
with h5py.File(source_filename, 'w') as f:
        f.create_dataset('source_data', (source_data.shape[0],source_data.shape[1]),  data=source_data)
        f.create_dataset('lp_label', (source_data.shape[0],lvsize),  data=source_labels)
with open(os.path.join(dirname, 'source.txt'), 'w') as f:
        f.write(source_filename + '\n')

#31628
# HDF5 is pretty efficient, but can be further compressed.
comp_kwargs = {'compression': 'gzip', 'compression_opts': 1}
with h5py.File(target_filename, 'w') as f:
        f.create_dataset('target_data',(target_data.shape[0],target_data.shape[1]), data=target_data)
        #f.create_dataset('label',(Xt.shape[0],1,1,lvsize), data=yt.astype(np.float32))
with open(os.path.join(dirname, 'target.txt'), 'w') as f:
        f.write(target_filename + '\n')

comp_kwargs = {'compression': 'gzip', 'compression_opts': 1}
with h5py.File(test_filename, 'w') as f:
        f.create_dataset('data',(test_data.shape[0],test_data.shape[1]), data=test_data)
        f.create_dataset('lp_label',(test_data.shape[0],lvsize), data=test_labels)
with open(os.path.join(dirname, 'test.txt'), 'w') as f:
        f.write(test_filename + '\n')




#X, Xt, S, St, y, yt = sklearn.cross_validation.train_test_split(X,S,y)
 
# Train and test the scikit-learn SGD logistic regression.
#clfe = sklearn.linear_model.SGDClassifier(
#        loss='log', n_iter=1000, penalty='l2', alpha=5e-4 , class_weight='auto')

#clfe.fit(X,y)
#yt_prede=clf.predict(Xt)

#clfs = sklearn.linear_model.SGDClassifier(
#        loss='log', n_iter=1000, penalty='l2', alpha=5e-4 , class_weight='auto')

#clfs.fit(S,y)
#yt_preds=clf.predict(St)


#print('Acuracy: {:.3f}'.format(sklearn.metrics.accuracy_score(yt_prede, yt_preds)))

