#%% Nick180919 Test package bioservices
from bioservices import UniProt
u = UniProt(verbose=False)
data = u.search("YER030W or YPL190C or YGR086C", frmt="tab", limit=20,columns="entry name,length,id, genes,comment(FUNCTION)")
print(data)
#%% Pramod180919 Test package bioservices
from bioservices import UniProt
u = UniProt(verbose=False)
data = u.search("YER030W", frmt="tab", limit=20,columns="entry name,length,\
                id, genes, organism-id")
print(data)

#%% Nick181008 Get all data from Rain's code

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
                    columns="entry name,length, id, genes, organism")
    test = re.split('\n|\t',data)
    del test[-1]
    total_data.append(test)
    
    print(data)

a = len(total_data)
data_list1 = [] 
count = [5,6,7,8,9]

for i in range(0,a):
    for j in count:
        data_list1.append(total_data[i][j])
    
data_list2 = np.reshape(data_list1,[a,5])
data_list3 = pd.DataFrame(data_list2, columns=['entry name','length','id','genes','organism'])
data_list3.to_csv("test_nick.csv")


# =============================================================================
# In here we can use package "bioservices" to extract the information from 
# Unipro database. Most of the information that we want can be get.
# Now we need to specify the search query so that we search the correct information
# e.g. protein name "YER030W" in Saccharomyces cerevisiae.
# =============================================================================

#%% Rain181004 UniProt data
from bioservices import UniProt
import pandas as pd
import re
import numpy as np

u = UniProt(verbose=False)
index = pd.ExcelFile('individual hits analysis_yeast_1.xlsx')
dfs = pd.read_excel(index, sheet_name=1)
#print(dfs)
ele = dfs['Histatin-5_unique']

for i in ele[0:19]:
    data = u.search(i+" Saccharomyces cerevisiae", frmt="tab", limit=1,\
                    columns="entry name,length, id, genes, organism,comment(FUNCTION)")
#    print(data)

#data.to_csv("test_rain",columns=['entry name','length','id','genes','organism'])
# Change the data to list
#test = data.split('\n')
test = re.split('\n|\t',data)
del test[-1]
test_resh = np.reshape(test,[2,int(len(test)/2)])

data_list = pd.DataFrame(test_resh,columns=['entry name','length','id',\
                                            'genes','organism','function'])
data_list.to_csv("test_rain.csv")
print('Done!')
# =============================================================================
# So here we need to enter, first, the gene name e.g. "YCL030C" then append the
# word "Saccharomyces cerevisiae" to get the result we want.
# =============================================================================
#%% Pramod180927 UniProt data

test = re.split('\n|\t',data)
del test[-1]
test_resh = np.reshape(test,[2,5])

data_list = pd.DataFrame(test_resh,columns=['entry name','length','id','genes','organism'])
data_list.to_csv("test_rain.csv")

#%% Pramod181023
from bioservices import UniProt
import pandas as pd
import re
import numpy as np

u = UniProt(verbose=False)
index = pd.ExcelFile('individual hits analysis_yeast_1.xlsx')
dfs = pd.read_excel(index, sheet_name=1)
#print(dfs)
ele = dfs['Histatin-5_unique']

for i in ele[0:19]:
    data = u.search(i+" Saccharomyces cerevisiae", frmt="tab", limit=1,\
                    columns="entry name,length, id, genes, organism,comment(FUNCTION), citation, comment(SUBCELLULAR LOCATION)")
    print(data)
