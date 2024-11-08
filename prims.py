def mst_find(G,s): 
	distance=[float ("inf")]*len(G) 
	distance[s]=0 
	itr=[False]*len(G)
	c=0
	while True: 
		min_weight=float('inf') 
		m_idx=-1
		for i in range (len(G)): 
			if itr[i]==False:
				if distance[i]<min_weight: 
					min_weight=distance[i] 
					m_idx=i
		if m_idx==-1: 
			break
		c+=min_weight 
		itr[m_idx]=True
		for i,j in G[m_idx].items(): 
			distance[i]=min(distance[i],j)
	return c
def solve(n,edge,s):
		G = {i: {} for i in range(n)} 
		for item in edge:
			u = item[0] 
			v = item[1]

			w = item[2] 
			u -= 1
			v -= 1
			try:
				min_weight = min(G[u][v], w) 
				G[u][v] = min_weight
				G[v][u] = min_weight 
			except KeyError:
				G[u][v] = w
				G[v][u] = w
		return mst_find(G, s)

print(solve(4, [(1, 2, 5), (1, 3, 5), (2, 3, 7), (1, 4, 4)], 3))
