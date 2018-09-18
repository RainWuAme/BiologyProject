from bioservices import UniProt
u = UniProt(verbose=False)
data = u.search("YER030W or YPL190C or YGR086C", frmt="tab", limit=20,columns="entry name,length,id, genes,comment(FUNCTION)")
print(data) 