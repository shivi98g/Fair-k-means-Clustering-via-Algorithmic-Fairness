import numpy as np
import os
from sklearn.datasets import make_blobs
import sys
import requests, zipfile, io
import pandas

#import random
#random.seed(0)
#np.random.seed(0)

__datasets = ['Adult', 'Bank', 'Synthetic', 'Synthetic-unequal', 'CensusII','Diabetes','BankFull']

def dataset_names():

    return __datasets


def read_dataset(name, data_dir,args):

    data = []
    sex_num = []
    K = []
    if name not in __datasets:
        raise KeyError("Dataset not implemented:",name)
        
    elif name == 'Synthetic':
        
        n_samples = 400

        centers = [(1, 1), (2.1, 1), (1, 5), (2.1, 5)]
        data, sex_num = make_blobs(n_samples=n_samples, n_features=2, cluster_std=0.1,
                  centers=centers, shuffle=False, random_state=1)
        
        index = n_samples//2
        sex_num[0:index] = 0
        sex_num[index:n_samples] = 1
        K = args.K
    elif name == 'Synthetic-unequal':
        
        n_samples = 400

        sample_list = [150,150,50,50]
        centers = [(1, 1), (2.1, 1), (1, 3.5), (2.1, 3.5)]
        data, sex_num = make_blobs(n_samples=sample_list, n_features=2, cluster_std=0.13,
                  centers=centers, shuffle=False, random_state=1)
        
        index = sample_list[0]+sample_list[1]
        sex_num[0:index] = 0
        sex_num[index:] = 1
        K = args.K
        
    elif name == 'Adult':
        print("Inside adult")
        _path = 'adult_p.csv'
        data_path = os.path.join(data_dir,_path)
        K = args.K
        df = pandas.read_csv(data_path, sep=',',header=[0])
        print(df.head())
        print(df.columns)
        sex_num = np.array(df['gender'])
        df = df.drop(columns=['gender'])
        print(df.head())
        
        data = np.array(df.values, dtype=float)

    elif name == 'Bank':
        K = args.K
        _path = 'bank-full_p_nodiv_6col.csv' # Big dataset with 41108 samples
        data_path = os.path.join(data_dir,_path)
        df = pandas.read_csv(data_path,sep=',')
        print(df.columns)
        sex_num = df['type']
        sex_num = np.array(sex_num)
        df = df.drop(columns=['type'])
        data = np.array(df, dtype=float)

    elif name == 'BankFull':
        K = args.K
        _path = 'bank-full_p_6col.csv' # Big dataset with 41108 samples
        data_path = os.path.join(data_dir,_path)
        df = pandas.read_csv(data_path,sep=',')
        print(df.columns)
        sex_num = df['type']
        sex_num = np.array(sex_num)
        df = df.drop(columns=['type'])
        data = np.array(df, dtype=float)



    elif name=='CensusII':
        _path = 'USCensus1990_p.csv'
        data_path = os.path.join(data_dir, _path)
        df = pandas.read_csv(data_path, sep=',', header = [0])
        sex_num = df['type']
        df = df.drop(columns=['type'])
        data = np.array(df, dtype=float)
        K = args.K

    elif name=='Diabetes':
        _path = 'diabetic_data_p.csv'
        data_path = os.path.join(data_dir, _path)
        df = pandas.read_csv(data_path, sep=',', header = [0])
        sex_num = df['gender']
        df = df.drop(columns=['gender'])
        data = np.array(df, dtype=float)
        K = args.K

    else:
        pass

    return data, sex_num, K
    
    
if __name__=='__main__':

    pass
    #dataset = 'CensusII'
    #datas = np.load('../data/CensusII.npz')['data']
    #X_org = datas['X_org']
    #demograph = datas['demograph']

    #V_list =  [np.array(demograph == j) for j in np.unique(demograph)]
    #V_sum =  [x.sum() for x in V_list]
    #print('Balance of the dataset {}'.format(min(V_sum)/max(V_sum)))
    #u_V = [x/X_org.shape[0] for x in V_sum]

    
    
    
    
    
    