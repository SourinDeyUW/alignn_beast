import pandas as pd
import numpy as np
import random
import copy
import pickle
infile = 'features_summary.csv'
df  = pd.read_csv(infile)
import os
df = df[(df['eig_HSE'] < 10) & (df['eig_HSE'] > -10)]

numb = 93
indx = "system"
def get_random_sublist(df,indx, numb):
    list1=pd.unique(df[indx]).tolist()
    sub_list=random.sample(list1,numb)
    return df[df[indx].isin(sub_list)], df[~df[indx].isin(sub_list)]

train_df, test_df = get_random_sublist(df,indx, numb)
print(train_df.shape)
print("len of db",len(train_df),'original df shape',len(df))

def prep_dict(dfs):
    inputs = ['1s_PBE', '2s_PBE', '2p_PBE', '3s_PBE', '3p_PBE', '3d_PBE', '4s_PBE', '4p_PBE', \
              '4d_PBE', '5s_PBE', '5p_PBE', '5d_PBE', '6s_PBE', '6p_PBE','eig_HSE']
    out_dict = {} 

    idx = 0
    for ncount, c in enumerate(np.unique(dfs['cif_ind'].tolist())):
    #     if ncount > 2:
    #         break
        tmp_df = df[df['cif_ind'] == c]
        for b in np.unique(tmp_df['ib'].tolist()):
            tmp_dict = {"mat":[],"eig_PBE":[], "targets": [], "kpoints": [], "node_feats": {},'system':[]}
            tmp_df2 = tmp_df[tmp_df['ib'] == b]
            for at in tmp_df2['atom_index'].tolist():
                tmp_df3 = tmp_df2[tmp_df2['atom_index'] == at]
                at_type = str(tmp_df3['atom_type'].tolist()[0])+"_"+str(tmp_df3['atom_index'].tolist()[0])
                tmp_dict["targets"].append( tmp_df3['eig_HSE'].tolist()[0] )
                tmp_dict["node_feats"][at_type] = [ tmp_df3[i].tolist()[0] for i in inputs ]
                tmp_dict["kpoints"].append( tmp_df3['ik'].tolist()[0] )
                tmp_dict["mat"].append( tmp_df3['cif_ind'].tolist()[0] )
                tmp_dict["eig_PBE"].append( tmp_df3['eig_PBE'].tolist()[0] )
                tmp_dict['system'].append(tmp_df3['system'].tolist()[0])
            out_dict[idx] = copy.deepcopy(tmp_dict)
            idx += 1
            
    return out_dict


dict_train=prep_dict(train_df)
print(len(dict_train))
#os.chdir('/work/sourin/phononDoS_tutorial/second/alignn')
import pickle
with open("nmc_train_alignn_eig_HSE_indiv_node_v3_pbe_april23.pkl", "wb") as input_file:
        pickle.dump(dict_train,input_file)

'''
dict_test=prep_dict(test_df)

def dos(dicts,name):
	with open(name, 'wb') as f:
    	    pickle.dump(dicts, f)

dos(dict_train,'nmc_train_alignn_eig_HSE_indiv_node.pkl')
dos(dict_test,'nmc_test_alignn_eig_HSE.pkl')       
print(' size is:',len(dict_train))
'''
