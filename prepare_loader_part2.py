import os
import csv
import os
import sys
import time
from jarvis.core.atoms import Atoms
#from alignn.data import get_train_val_loaders
#from alignn.train import train_dgl
#from alignn.config import TrainingConfig
#from jarvis.db.jsonutils import loadjson
import argparse
import numpy as np

#os.chdir('/work/sourin/phononDoS_tutorial/second/alignn')
import pickle
with open("nmc_train_alignn_eig_HSE_indiv_node_v3_pbe_april23.pkl", "rb") as input_file:
        dict_test= pickle.load(input_file)

os.chdir('/mnc_cif')

#atoms = Atoms.from_cif('29.cif')

import sys
dataset=[]
cn=0
for i1 in range(len(dict_test)):
     info={}
     cn+=1
     xi2=dict_test[i1]['node_feats'].keys()
     x2=str(dict_test[i1]['mat'][0])+'.cif'
     print(x2)
#     x3="_"+dict_test[i1]['system'][0]     
 #    x4="_band_"+str(dict_test[i1]['band'][0])
     info["jid"]=x2+'_'+str(i1)#+x3+x4
     atoms = Atoms.from_cif(x2)
     info["atoms"]=atoms.to_dict()
     info['nf']=[]
     info['eig_PBE']=dict_test[i1]['eig_PBE'][0]
     info['target']=dict_test[i1]['targets'][0]
     info['system']=dict_test[i1]['system'][0]
     #print(dict_test[i1]['mat'])
     for xi3,xi4 in enumerate(dict_test[i1]['node_feats']):
          # print(xi4,dict_test[i1]['node_feats'][xi4])
           info['nf'].append(dict_test[i1]['node_feats'][xi4])
     dataset.append(info)
#sys.exit(1)   
    #sys.exit(1)
#print(dataset)

import pickle
import pandas as pd
os.chdir('..')


with open('alignn_nmc_eig_HSE_individual_node_v3_april23_pbe.pickle','wb') as handle:
    pickle.dump(dataset,handle,protocol=pickle.HIGHEST_PROTOCOL)
print('ok')

#dataset=pd.DataFrame(dataset)
#dataset.to_csv('mnc_dataset_alignn_format.csv',index=False)
#print('cn=',cn)    
