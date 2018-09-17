#original reference: https://www.youtube.com/watch?v=7pOcOvhG7xQ 13:50

from bioservices import UniProt #specify provider

u = UniProt() #for calling user query

res = u.search('taxibp1 AND htlv',frmt='tab',columns='entry name, length, id, genes')
#res for result, query parameter is the keyword you want to search for
#frmt for format, tab for table, columns for specify your table header

print res