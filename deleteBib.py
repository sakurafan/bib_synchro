import re
from pprint import pprint

def safe_open(filename,mode='r',*rubbish_args,**rubbish_keywords):
	try:
		if mode == 'r':
			open(filename,mode,encoding='utf8').read()
		return open(filename,mode,encoding='utf8')
	except:
		return open(filename,mode,encoding='gbk')
		
def createKeys(filename):
	text=safe_open(filename,encoding='utf-8').read()
	patternblock="(\@.*?\}[ \n\,]*\})"
	patternkey="(?:\@.*?\{)(\w+)(?:\,)"

	return re.findall(patternkey,text,re.DOTALL),  re.findall(patternblock,text,re.DOTALL)

def search(keywords,string):
	#return re.search(pattern,string,re.MULTILINE|re.DOTALL)
	res = string.find(keywords)
	if res <0:
		return None
	else:
		return 1 
bibFilename='C:\\Users\\dell\\Desktop\\semi_hyper_visualization_paper\\JSTARS_visualization\\JSTARS_visualization_v4\\visualization v7\\visualization_JSTARS_final\\HSIvisualization.bib'
texFilename='C:\\Users\\dell\\Desktop\\semi_hyper_visualization_paper\\JSTARS_visualization\\JSTARS_visualization_v4\\visualization v7\\visualization_JSTARS_final\\JSTARS-2017-00367-v8.tex'


keylist,biblist=createKeys(bibFilename)
dic={}
dic.update(zip(keylist,biblist))  # (shortkey, block)

#print (biblist[20])

tex = safe_open(texFilename).read()

tex_pattern = "cite\{\s*(\w+)(?:\s*\,\s*\w+)*\s*\}"
sub_pattern = "(\w+)"
cited=[]
for one_match in  re.finditer(tex_pattern,tex):
	#pprint(one_match.group())
	#pprint(one_match.groups())
	cite_str = one_match.group()
	res = re.findall(sub_pattern,cite_str)
	#pprint(res[1:])
	cited+=res[1:]
cited = list(set(cited))
print(len(keylist))
finalbib=[]
for s in cited:
	finalbib.append(dic[s])
print(len(finalbib))
pprint(cited[0])
pprint(str(dic[s]))
finalbib="\n".join(finalbib)
newbibFilename='C:\\Users\\dell\\Desktop\\semi_hyper_visualization_paper\\JSTARS_visualization\\JSTARS_visualization_v4\\visualization v7\\visualization_JSTARS_final\\newHSIvisualization.bib'

safe_open(newbibFilename,'w').write(finalbib)
