from math import radians, cos, sin, asin, sqrt, log1p
import networkx as nx
from scipy import stats
import numpy as np

G1= nx.Graph()
G2= nx.Graph()
G3= nx.Graph()
G4= nx.Graph()

stars=['be','bd','av','ai','s','j','g','al','bh','ax']

w1=.25
w2=.15
w3=.40
w4=.25

locations = {'a': [42.391699, -71.124304], 'b': [42.373744, -71.125843], 'c': [42.374961, -71.096084],'d': [42.409411, -71.050450], 'e': [42.381610, -71.098520], 'f': [42.375851, -71.111250], 'g': [42.375851, -71.111250], 'h': [42.348149, -71.125259], 'i': [42.398327, -71.109156], 'j': [42.341359, -71.129262], 'k': [42.330109, -71.102265], 'l': [42.366198, -71.055161], 'm': [42.363127, -71.052871], 'n': [42.336784, -71.028233], 'o': [42.331657, -71.044171], 'p': [42.404476, -71.110355], 'q': [42.380539, -71.216191], 'r': [42.345135, -71.200482], 's': [42.339158, -71.219086], 't': [42.311545, -71.116703], 'u': [42.350621, -71.133100], 'v': [42.338938, -71.066616], 'w': [42.381778, -71.065056], 'x': [42.402704, -71.144459], 'y': [42.402197, -71.129005], 'z': [42.377465, -71.066695],'aa': [42.329602, -71.053268],'ab': [42.332605, -71.107962],'ac': [42.370678, -71.114778],'ad': [42.751980, -71.081939],'ae': [42.388819, -71.109396],'af': [42.386214, -71.081533],'ag': [42.386960, -71.091940],'ah': [42.379989, -71.128479],'ai': [42.416092, -71.096651],'aj': [42.423499, -71.117057],'ak': [42.307191, -71.083465],'al': [42.313450, -71.050200],'am': [42.325038, -71.148503],'an': [42.352371, -71.081293],'ao': [42.346362, -71.073634],'ap': [42.311370, -71.108404],'aq': [42.393887, -71.132892],'ar': [42.369272, -71.036049],'as': [42.368170, -71.056085],'at': [42.482519, -71.249729],'au': [42.441446, -71.190283],'av': [42.369760, -71.081262],'aw': [42.364578, -71.113695],'ax': [42.309149, -71.201579],'ay': [42.326711, -71.081940],'az': [42.350352, -71.093758],'ba': [42.337270, -71.048534],'bb': [42.311745, -71.126090],'bc': [42.324418, -71.063621],'bd': [42.391968, -71.113379],'be': [42.338822, -71.178091],'bf': [42.302771, -71.080862],'bg': [42.378291, -71.159026],'bh': [42.428807, -71.128179]}
pract = [4,9,14,19,24,29,34,39,44]
out='True'

def haversine(lon1, lat1, lon2, lat2):
	"""
	Calculate the great circle distance between two points 
	on the earth (specified in decimal degrees)
	"""
	# convert decimal degrees to radians 
	lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
	# haversine formula 
	dlon = lon2 - lon1 
	dlat = lat2 - lat1 
	a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
	c = 2 * asin(sqrt(a)) 
	km = 6367 * c
	return km
	
def algorithm(w1,w2,w3,w4,G1,G2,G3,G4):
	try:
		cc=np.array([nx.average_clustering(G1,weight='weight'),nx.average_clustering(G2,weight='weight'),nx.average_clustering(G3,weight='weight'),nx.average_clustering(G4,weight='weight')])
		spl=np.array([nx.average_shortest_path_length(G1,weight='weight'),nx.average_shortest_path_length(G2,weight='weight'),nx.average_shortest_path_length(G3,weight='weight'),nx.average_shortest_path_length(G4,weight='weight')])
		nds=np.array([nx.number_of_nodes(G1),nx.number_of_nodes(G2),nx.number_of_nodes(G3),nx.number_of_nodes(G4)])
		edgs= np.array([nx.number_of_edges(G1),nx.number_of_edges(G2),nx.number_of_edges(G3),nx.number_of_edges(G4)])
		try:
			cc=stats.zscore(cc)
		except:
			cc=np.array([.1,.1,.1,.1])
		cc= cc-min(cc)+.1
		try:
			spl=stats.zscore(spl)
		except:
			spl=np.array([.1,.1,.1,.1])
		spl= spl-min(spl)+.1
		try:
			nds=stats.zscore(nds)
		except:
			nds=np.array([.1,.1,.1,.1])
		nds = nds-min(nds)+.1
		try:
			edgs=stats.zscore(edgs)
		except:
			edgs=np.array([.1,.1,.1,.1])
		edgs=edgs-min(edgs)+.1
		r1=(w1*cc[0]+w2*spl[0]+w3*nds[0]+w4*edgs[0])*1000
		r2=(w1*cc[1]+w2*spl[1]+w3*nds[1]+w4*edgs[1])*1000
		r3=(w1*cc[2]+w2*spl[2]+w3*nds[2]+w4*edgs[2])*1000
		r4=(w1*cc[3]+w2*spl[3]+w3*nds[3]+w4*edgs[3])*1000
		d={'Player 1:': r1, 'Player 2:': r2,'Player 3:': r3, 'Player 4:': r4}
		rank = sorted(d.items(), key=lambda x: x[1], reverse=True)
		print "USAU RANKINGS"
		print rank[0][0], int(rank[0][1])
		print rank[1][0], int(rank[1][1])
		print rank[2][0], int(rank[2][1])
		print rank[3][0], int(rank[3][1])
	except:
		print "Unable to compute until graphs are valid"
	
	
def process_nodes(nodes,graph):
	for i in range(len(nodes)):
		if nodes[i][0]=='-':
			graph.remove_node(nodes[i][1:])
		else:
			graph.add_node(nodes[i])
def process_edges(edges,graph):
	for i in range(len(edges)):
		l=edges[i].split(':')			
		if edges[i][0]=='-':
			try:
				graph.remove_edge(l[0][1:],l[1])
			except:
				continue
		else:
			#compute edge weights
			dist=haversine(locations[l[0]][1],locations[l[0]][0],locations[l[1]][1],locations[l[1]][0])+1.1
			if l[0] in stars and l[1] in stars:
				wt= (1.0/log1p(dist))*4.0
			elif l[0] in stars or l[1] in stars:
				wt= (1.0/log1p(dist))*2.0
			else:
				wt= (1.0/log1p(dist))
			graph.add_edge(l[0],l[1],{'weight':wt})	 
def process_meta(rsp):
	ns=rsp.find('(')
	ne=rsp.find(')')
	es=rsp.rfind('(')
	ee=rsp.rfind(')')
	if ns==es:
		print "Need parentheses for nodes and edges. ex. p1 (<nodes>)(<edges>)"
	else:
		nodes=rsp[ns+1:ne].split(',')
		edges=rsp[es+1:ee].split(',')
		if nodes[0]=='':
			nodes.remove('')
		if edges[0]=='':
			edges.remove('')					
		if rsp[:2]=='p1':
			if rsp[3:13]=='centrality':
				print "yes"
				val=nx.betweenness_centrality(G1,weight='weight')
				print "the most central node is " + max(val, key=val.get)			
			else:
				process_nodes(nodes,G1)
				process_edges(edges,G1)
		if rsp[:2]=='p2':
			if rsp[3:13]=='centrality':
				val=nx.betweenness_centrality(G2,weight='weight')
				print "the most central node is " + max(val, key=val.get)
			else:
				process_nodes(nodes,G2)
				process_edges(edges,G2)
		if rsp[:2]=='p3':
			if rsp[3:13]=='centrality':
				val=nx.betweenness_centrality(G3,weight='weight')
				print "the most central node is " + max(val, key=val.get)
			else:
				process_nodes(nodes,G3)
				process_edges(edges,G3)
		if rsp[:2]=='p4':
			if rsp[3:13]=='centrality':
				val=nx.betweenness_centrality(G4,weight='weight')
				print "the most central node is " + max(val, key=val.get)
			else:
				process_nodes(nodes,G4)
				process_edges(edges,G4)		   
