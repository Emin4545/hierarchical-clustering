from sklearn.datasets import load_iris
from scipy.spatial import distance
import numpy as np

def create_data():
    all_data = load_iris()
    data=all_data.data
    clusters=list()
    for i in range(len(data)):
        clusters.append(data[i]) 
    for i in range(len(clusters)):
        clusters[i]=clusters[i].reshape(1,len(clusters[i]))
    return clusters

def find_max_distance(data1,data2):
    max_dictance=0
    for i in range(len(data1)):
        for x in range(len(data2)):
                dictance=distance.euclidean(data1[i], data2[x])
                if dictance>max_dictance:
                    max_dictance=dictance
    return max_dictance


def find_min_distance_clusters(data3):
    min_of_max_distanes=np.inf
    for i in range(len(data3)) :
        for x in range(len(data3)):
            if i==x or x<i:
                continue
            else:
                max_dis=find_max_distance(data3[i],data3[x])
                if max_dis<min_of_max_distanes:
                    min_of_max_distanes=max_dis
                    cluster_ind1=i
                    cluster_ind2=x
    return cluster_ind1,cluster_ind2

def marging_data(data_new,ind_clust1,ind_clust2): 
    temp=np.concatenate((data_new[ind_clust1], data_new[ind_clust2]),axis=0)
    if ind_clust1>ind_clust2:
        del data_new[ind_clust1]
        del data_new[ind_clust2]
    else:
        del data_new[ind_clust2]
        del data_new[ind_clust1]
    data_new.append(temp)
    return data_new

def main(num_clusters):
    start_data=create_data()
    while len(start_data)>num_clusters:
        index_1,index_2=find_min_distance_clusters(start_data)
        secound_data=marging_data(start_data,index_1,index_2)
        start_data=secound_data
    return start_data

list_of_clusters=main(3)
#%%
#import matplotlib.pyplot as plt
#for i in range(len(list_of_clusters)):
#    plt.scatter(list_of_clusters[i][:,0],list_of_clusters[i][:,1])
#plt.show()        
  
                
            
            
            
        
            
            
    
    
    



