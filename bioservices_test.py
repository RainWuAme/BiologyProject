from bioservices import UniProt
u = UniProt(verbose=False)
data = u.search("tax1bp1", frmt="tab", limit=6,columns="entry name,length,id, genes")
print(data) 