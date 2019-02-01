from bioservices import UniProt
import pandas as pd
import re
import numpy as np
import os

#directory = input()
cwd = os.getcwd()
directory = os.path.join("C:/Users/user/BiologyProject/gene_name_index")
f = []
for (dirpath, dirnames, filenames) in os.walk(directory):
    f.extend(filenames)

iteration = 1
for j in f:
    os.chdir(directory)
    file = j
    u = UniProt(verbose=False)
    index = pd.ExcelFile(file)
    dfs = pd.read_excel(index, sheet_name=0, header=None)
    dfs = list(dfs[0])
    
    
    total_data = []
    
    
    for i in dfs[0:]:
        data = u.search(i+" Saccharomyces cerevisiae", frmt="tab", limit=1,\
                        columns="entry name,length, id, genes, organism,\
                        comment(FUNCTION)")
        data_split = re.split('\n|\t',data)
        del data_split[-1]
        total_data.append(data_split)
    
    a = len(total_data)
    data_list1 = [] 
    count = list(range(int(len(total_data[0])/2),int(len(total_data[0]))))
    
    for i in range(0,a):
        data_list1.append(dfs[i])
        for j in count:
            data_list1.append(total_data[i][j])
       
    features = ['genes name','entry name','length','id','genes','organism',"function"]
    data_list2 = np.reshape(data_list1,[a,len(features)])
    data_list3 = pd.DataFrame(data_list2, columns=features)
    os.chdir(cwd)
    data_list3.to_csv(file[:file.index(".")]+"_result.csv")
    print('File '+str(iteration)+' done!')
    iteration += 1
