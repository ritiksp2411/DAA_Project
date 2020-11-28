def connected(adj_mat, num_nodes):
    seen = [False for i in range(num_nodes)]
    dfs(adj_mat, seen, 0, num_nodes)
    for i in seen:
        if i is False:
            return False
    return True

def dfs(adj_mat, seen, j, num_nodes):
    seen[j] = True
    for k in range(num_nodes):
        if adj_mat[j][k] == 1 and seen[k] == False:
            dfs(adj_mat, seen, k, num_nodes)