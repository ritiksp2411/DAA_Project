from connected import connected
import random

def calc_num(n):
	ans = n*(n-1)/2
	return int(ans)

def find_num(n):
	ans = 2**calc_num(n)
	return ans

def make_combination(num_nodes):
	edge_mat = [get_combination(i, num_nodes) for i in range(find_num(num_nodes))]
	return edge_mat

def get_combination(n, num_nodes):
	combination = [i for i in range(calc_num(num_nodes))]
	ne = len(combination)
	for i in range(ne - 1, -1, -1):
		combination[i] = n % 2
		n /= 2
	return combination

def calc_reliability(edge_mat, num_nodes):
	print "0.0\t0.0"
	for p in drange(0.05, 1, 0.05):
		comb_reliability = 0.0
		for i in edge_mat:
			adj_mat = [[0 for x in range(num_nodes)] for x in range(num_nodes)]
			adj_i, adj_j = 0, 1
			for j in range(calc_num(num_nodes)):
				if adj_j == num_nodes and adj_i < num_nodes-2:
					adj_i=adj_i+1
					adj_j=adj_i+1

				if adj_j <= num_nodes-1:
					adj_mat[adj_i][adj_j] = i[j]
					adj_mat[adj_j][adj_i] = i[j]
					adj_j += 1

			if connected(adj_mat, num_nodes):
				comb_reliability += get_reliability(i, p)
		print p, "\t", comb_reliability

def get_reliability(edge_mat, p):
	rel = 1.0
	for col in edge_mat:
		if col == 1:
			rel = rel * p
		else:
			rel = rel * (1.0 - p)
	return rel

def calc_reliability2(edge_mat, num_nodes, p):
	comb_reliability = 0.0
	for i in edge_mat:
		adj_mat = [[0 for x in range(num_nodes)] for x in range(num_nodes)]
		adj_i, adj_j = 0, 1
		for j in range(calc_num(num_nodes)):
			if adj_j == num_nodes and adj_i < num_nodes-2:
				adj_i=adj_i+1
				adj_j=adj_i+1
				
			if adj_j <= num_nodes-1:
				adj_mat[adj_i][adj_j] = i[j]
				adj_mat[adj_j][adj_i] = i[j]
				adj_j += 1

		if connected(adj_mat, num_nodes):
			comb_reliability += get_reliability2(i, p)
			
	return comb_reliability

def get_reliability2(edge_mat, p):
	rel = 1.0
	num=0
	for col in edge_mat:
		num+=1
		if col == 1:
			rel = rel * p[num-1]
		else:
			rel = rel * (1.0 - p[num-1])
	return rel



def drange(start, stop, step):
	r = start
	while r < stop:
		yield r
		r += step

def run_exp1(edge_mat, num_nodes):
	print 'p\tReliability'
	calc_reliability(edge_mat, num_nodes)
	print

def run_exp2(edge_mat, num_nodes, p):
	print 'Reliability'
	comb_reliability = calc_reliability2(edge_mat, num_nodes, p)
	print "The reliabilty for this combination is: ", comb_reliability
	print

def run_exp3(edge_mat, num_nodes, p, q):
	a = []
	for i in range(calc_num(num_nodes)):
		a.append(p)
	comb_reliability = calc_reliability2(edge_mat, num_nodes, a)
	if(comb_reliability>=q):
		print "YES\n"
	else:
		print "NO\n"

def main():
	while(1):
		ch = int(input('''Enter your choice
			1. Give custom probabilty for each edge.
			2. Calculate the reliabilty for each probabilty.
			3. Decision version of problem.
			4. Exit.\n'''))

		if ch == 1:
			num_nodes = int(input("Enter the number of nodes: "))
			if(num_nodes < 0):
				print "Invalid number of nodes"
				exit(0)
			edge_mat = make_combination(num_nodes)
			p = []
			for i in range(num_nodes):
				for j in range(i+1, num_nodes):
					x = float(input("Enter probabilty of link from node " + str(i) + " to node " + str(j) + ": "))
					if(0>x or x> 1):
						print "Invalid probabilty"
						exit(0)
					p.append(x)            
			run_exp2(edge_mat, num_nodes, p)
		
		elif ch == 2:
			num_nodes = int(input("Enter the number of nodes: "))
			if(num_nodes < 0):
				print "Invalid number of nodes"
				exit(0)
			edge_mat = make_combination(num_nodes)
			run_exp1(edge_mat, num_nodes)

		elif ch == 3:
			num_nodes = int(input("Enter the number of nodes: "))
			if(num_nodes < 0):
				print "Invalid number of nodes"
				exit(0)
			edge_mat = make_combination(num_nodes)
			p = float(input("Enter the probabitly of link: "))
			q = float(input("Enter the expected minimum reliabilty: "))
			run_exp3(edge_mat, num_nodes, p, q)

		else:
			print "Goodbye!"
			exit(0)

if __name__ == '__main__':
	main()
