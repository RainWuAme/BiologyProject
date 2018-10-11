from bioservices import UniProt
import pandas as pd
import re
import numpy as np

u = UniProt(verbose=False)
index = pd.ExcelFile('individual hits analysis_yeast_1.xlsx')
dfs = pd.read_excel(index, sheet_name=1)
print(dfs)
ele = dfs['Histatin-5_unique']

total_data = []

for i in ele[0:]:
    data = u.search(i+" Saccharomyces cerevisiae", frmt="tab", limit=1,\
                    columns="entry name,length, id, genes, organism,comment(FUNCTION)")
    test = re.split('\n|\t',data)
    del test[-1]
    total_data.append(test)
    
    print(data)

a = len(total_data)
data_list1 = [] 
count = [6,7,8,9,10,11]

for i in range(0,a):
    for j in count:
        data_list1.append(total_data[i][j])
    
data_list2 = np.reshape(data_list1,[a,6])
data_list3 = pd.DataFrame(data_list2, columns=['entry name','length','id','genes','organism',"function"])
data_list3.to_csv("test_nick.csv")