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


