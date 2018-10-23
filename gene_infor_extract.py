from bioservices import UniProt
import pandas as pd
import re
import numpy as np

u = UniProt(verbose=False)
index = pd.ExcelFile('individual hits analysis_yeast_1.xlsx')
dfs = pd.read_excel(index, sheet_name=1)
ele = dfs['Histatin-5_unique']

total_data = []

for i in ele[0:]:
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
    data_list1.append(ele[i])
    for j in count:
        data_list1.append(total_data[i][j])
   
features = ['genes name','entry name','length','id','genes','organism',"function"]
data_list2 = np.reshape(data_list1,[a,len(features)])
data_list3 = pd.DataFrame(data_list2, columns=features)
data_list3.to_csv("gene_informaiton.csv")
print('Done!')