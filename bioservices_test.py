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

# =============================================================================
# In here we can use package "bioservices" to extract the information from 
# Unipro database. Most of the information that we want can be get.
# Now we need to specify the search query so that we search the correct information
# e.g. protein name "YER030W" in Saccharomyces cerevisiae.
# =============================================================================

#%% Rain180920 UniProt data
from bioservices import UniProt
import pandas as pd

index = pd.ExcelFile('individual hits analysis_yeast_1.xlsx')
dfs = pd.read_excel(index, sheet_name=0)
print(dfs)

u = UniProt()
data = u.search("YCL030C Saccharomyces cerevisiae", frmt="tab", limit=20,columns="entry name,length,\
                id, genes, organism")
print(data)

# =============================================================================
# So here we need to enter, first, the gene name e.g. "YCL030C" then append the
# word "Saccharomyces cerevisiae" to get the result we want.
# =============================================================================
