def solution(n, costs):
    parent = [i for i in range(n)]
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a, b):
        root_a = find(a)
        root_b = find(b)
        
        if root_a != root_b:
            parent[root_b] = root_a
            return True
        return False
    
    total = 0
    costs.sort(key=lambda x:x[2])
    for a, b, cost in costs:
        if union(a, b): # 사이클이 없다면
            total += cost
    
    return total